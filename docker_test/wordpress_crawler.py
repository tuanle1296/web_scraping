import sys
import os
import concurrent.futures
import math
import json
import argparse
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.file_manager import get_config_folder_id
from src.newlocators import wordpress as lo
from src.drive_manager import DriveManager

forbidden_words = ["facebook", "onebook", "ngoai-le"]

def crawl_worker(chapter_data, folder_name, passwords_dict, default_pass):
    """
    Worker function to process a chunk of chapters.
    """
    with Base(True, timeout=5) as crawl:
        try:
            crawl.set_path(folder_name)
        except Exception as e:
            print(f"Error while setting folder path: {e}")
        
        for chap_url, chap_num in chapter_data:
            try:
                print(f"--- Crawling: Chapter {chap_num} | URL: {chap_url} ---")
                crawl.go_to_webpage(chap_url)

                if not crawl.wait_for_page_load(10):
                    print(f"Skip: Chapter {chap_num} did not load correctly.")
                    continue

                if crawl.is_element_visible(lo.password_input_field):
                    password_to_try = passwords_dict.get(str(chap_num)) or default_pass
                    
                    if password_to_try:
                        print(f"Chapter {chap_num}: Password required. Trying: {password_to_try}")
                        crawl.input_text(lo.password_input_field, password_to_try)
                        crawl.click_element(lo.password_submit_btn)
                        crawl.sleep(2)
                    else:
                        print(f"Warning: Chapter {chap_num} is locked but no password is provided in config.")

                title = crawl.get_element_text(lo.chapter_title)
                content = crawl.get_element_text(lo.chapter_content)
                if content:
                    crawl.add_text_to_doc_file(title, content, f"chapter_{chap_num}")
                    print(f"Successfully saved Chapter {chap_num}")
                else:
                    print(f"Error: Failed to extract content for chapter {chap_num}")
            
            except Exception as e:
                print(f"Exception during chapter {chap_num} crawl: {e}")


def main():
    parser = argparse.ArgumentParser(description='WordPress Crawler (Docker Optimized)')
    parser.add_argument('--url', type=str, required=True, help='Main story URL')
    parser.add_argument('--name', type=str, required=True, help='Output folder name')
    parser.add_argument('--pass-file', type=str, default="passwords/wordpress_passwords.json", help='Path to JSON password file')
    args = parser.parse_args()

    main_url = args.url
    storyName = args.name
    
    # Load passwords from JSON file
    passwords_dict = {}
    default_pass = None
    if os.path.exists(args.pass_file):
        try:
            with open(args.pass_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                default_pass = data.pop('default', None)
                passwords_dict = data
            print(f"Loaded password file: {len(passwords_dict)} specific passwords, Default pass: {default_pass}")
        except Exception as e:
            print(f"Error reading password file: {e}")

    print(f"======= Starting crawl for: {storyName} =======")
    
    # Initialize storage folder
    with Base(True) as temp_crawl:
        try:
            temp_crawl.create_folder(storyName)
        except Exception as e:
            print(f"Error creating folder: {e}")
            return

    chapters_list = []

    with Base(True) as crawl:
        crawl.go_to_webpage(main_url)
        if not crawl.wait_for_page_load(10):
            print(f"Error: Main page {main_url} did not load correctly.")
            return
        
        soup = BeautifulSoup(crawl.get_page_source(), "html.parser")
        
        # 1. Try finding anchors in p_chap_list first
        entry_content_ps = soup.select(lo.p_chap_list[1])
        for p in entry_content_ps:
            for anchor in p.find_all(lo.a_tag[1]):
                url = anchor.get('href')
                if url and not any(word in url for word in forbidden_words) and (url not in chapters_list):
                    chapters_list.append(url)
        
        # 2. If no chapters found, try finding anchors in normal_chap_list
        if not chapters_list:
            print("No links found in p_chap_list, trying normal_chap_list...")
            entry_content = soup.select_one(lo.normal_chap_list[1])
            if entry_content:
                for anchor in entry_content.find_all(lo.a_tag[1]):
                    url = anchor.get('href')
                    if url and not any(word in url for word in forbidden_words) and (url not in chapters_list):
                        chapters_list.append(url)

    if not chapters_list:
        print("Error: No chapters found to crawl. Exiting.")
        return

    # Prepare data for multithreading
    indexed_chapters = [(url, i + 1) for i, url in enumerate(chapters_list)]
    num_threads = 3
    chunk_size = math.ceil(len(indexed_chapters) / num_threads)
    chunks = [indexed_chapters[i:i + chunk_size] for i in range(0, len(indexed_chapters), chunk_size)]

    print(f"Launching {len(chunks)} threads for {len(chapters_list)} chapters...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(lambda chunk: crawl_worker(chunk, storyName, passwords_dict, default_pass), chunks)
        
    print("======= Finished crawling all chapters =======")

    # Zip and Upload to Drive
    try:
        with Base(True) as zip_crawl:
            zip_path = zip_crawl.zip_folder(storyName)
            if zip_path:
                print(f"Folder zipped successfully: {zip_path}")
                drive = DriveManager()
                drive.upload_zip(zip_path, folder_id=get_config_folder_id())
                print("======= Successfully uploaded to Google Drive =======")
    except Exception as e:
        print(f"Error during zipping or uploading: {e}")

if __name__ == '__main__':
    main()
