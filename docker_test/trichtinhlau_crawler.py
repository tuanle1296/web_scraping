import sys
import os
import concurrent.futures
import math
import json
import argparse
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.base_functions import *
from src.file_manager import get_config_folder_id
from src.newlocators import trichtinhlau as lo
from src.drive_manager import DriveManager

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

                # Handle password-protected content
                if crawl.is_element_visible(lo.password_input_field):
                    password_to_try = passwords_dict.get(str(chap_num)) or default_pass
                    
                    if password_to_try:
                        print(f"Chapter {chap_num}: Password required. Trying: {password_to_try}")
                        crawl.input_text(lo.password_input_field, password_to_try)
                        crawl.sleep(1)
                        crawl.click_element(lo.password_submit_btn, force_js=True)
                        crawl.wait_for_page_load(10)
                    else:
                        print(f"Warning: Chapter {chap_num} is locked but no password is provided in config.")

                # Ensure content is visible before extraction
                if crawl.wait_for_element_visible(lo.chapter_content, timeout=10):
                    print(f"Extracting text for chapter {chap_num}...")
                    title = crawl.get_element_text(lo.chapter_title, extract_hidden=False)
                    content = crawl.get_element_text(lo.chapter_content, extract_hidden=False)
                    crawl.add_text_to_doc_file(title, content, f"chapter_{chap_num}")
                    print(f"Successfully saved Chapter {chap_num}")
                else:
                    print(f"Error: Content not visible for chapter {chap_num}")

            except Exception as e:
                print(f"Exception during chapter {chap_num} crawl: {e}")


def main():
    parser = argparse.ArgumentParser(description='Trichtinhlau Crawler (Docker Optimized)')
    parser.add_argument('--url', type=str, required=True, help='Main story URL (Chapter list page)')
    parser.add_argument('--name', type=str, required=True, help='Output folder name')
    parser.add_argument('--pages', type=int, default=1, help='Number of pagination pages to scan for links')
    parser.add_argument('--pass-file', type=str, default="passwords/trichtinhlau_passwords.json", help='Path to JSON password file')
    args = parser.parse_args()

    main_url_base = args.url # e.g. https://trichtinhlau.com/xem-truyen/khach-tro
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
    with Base(True) as master_crawl:
        # Loop through pages to gather URLs
        for i in range(1, args.pages + 1):
            target_url = f"{main_url_base}?page={i}" if "?" not in main_url_base else f"{main_url_base}&page={i}"
            print(f"Gathering links from: {target_url}")
            master_crawl.go_to_webpage(target_url)
            if not master_crawl.wait_for_page_load(10):
                continue
            
            chap_list = master_crawl.find_elements(lo.chap_list)
            for chap in chap_list:
                anchors = master_crawl.find_elements(lo.a_tag, chap)
                for anchor in anchors:
                    href = master_crawl.get_attribute_from_element(anchor, "href")
                    if href and href not in chapters_list:
                        chapters_list.append(href)

    if not chapters_list:
        print("Error: No chapters found!")
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
