import sys
import os
import math
import json
import argparse
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.file_manager import get_config_folder_id
from src.newlocators import mongtruyen as lo
from src.drive_manager import DriveManager

# Default login credentials (Can be overridden by Environment Variables)
login_url = "https://mongtruyen.com/dang-nhap.html"
username = os.getenv("SCRAPE_USER", "tuantest")
password_signin = os.getenv("SCRAPE_PASS", "04121996")

def crawl_worker(chapter_data, folder_name, passwords_dict, default_pass):
    """
    Worker function to process a chunk of chapters.
    """
    with Base(True, timeout=2) as crawl:
        try:
            crawl.set_path(folder_name)
        except Exception as e:
            print(f"Error while setting folder path: {e}")
        
        # Sign in to gain access
        crawl.go_to_webpage(login_url)
        if not crawl.wait_for_page_load(10):
            print(f"Error: Failed to load login page {login_url}")
            return

        crawl.input_text(lo.username_signin_field, username)
        crawl.input_text(lo.password_signin_field, password_signin)
        crawl.click_element(lo.signin_submit_btn)
        crawl.sleep(3)

        for chap_url, chap_num in chapter_data:
            try:
                print(f"--- Crawling: Chapter {chap_num} ---")
                crawl.go_to_webpage(chap_url)

                if not crawl.wait_for_page_load(10):
                    print(f"Skip: Chapter {chap_num} did not load correctly.")
                    continue

                # Bypass age restriction warning if present
                if crawl.is_element_visible(lo.accept_warning_btn):
                    crawl.click_element(lo.accept_warning_btn)
                    crawl.sleep(1)

                # Handle chapter password protection
                if crawl.is_element_visible(lo.password_input_field):
                    # Priority: Specific chapter password > Default password
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
                else:
                    print(f"Error: Failed to extract content for chapter {chap_num}")
            
            except Exception as e:
                print(f"Exception during chapter {chap_num} crawl: {e}")

def main():
    parser = argparse.ArgumentParser(description='Mongtruyen Crawler (Docker Optimized)')
    parser.add_argument('--url', type=str, required=True, help='Main story URL')
    parser.add_argument('--name', type=str, required=True, help='Output folder name')
    parser.add_argument('--pass-file', type=str, default="passwords/mongtruyen_passwords.json", help='Path to JSON password file')
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
    urls = []

    # Extract chapter list from the main page (using real browser for pagination)
    with Base(False) as crawl:
        crawl.go_to_webpage(main_url)
        if crawl.is_element_visible(lo.accept_warning_btn):
            crawl.click_element(lo.accept_warning_btn)

        if crawl.wait_for_page_load(15):
            # Check for pagination
            if not crawl.is_element_visible(lo.pagination):
                urls.append(main_url)
            else:
                try:
                    total_pages_elements = crawl.find_elements(lo.page_link)
                    total_pages = int(total_pages_elements[-2].text) if total_pages_elements else 1
                    for i in range(1, total_pages + 1):
                        urls.append(f"{main_url}?page={i}")
                except:
                    urls.append(main_url)

            for target_url in urls:
                print(f"Extracting chapter links from: {target_url}")
                crawl.go_to_webpage(target_url)
                crawl.sleep(2)
                containers = crawl.find_elements(lo.chap_list)
                for container in containers:
                    anchors = crawl.find_elements(lo.a_tag, container)
                    for anchor in anchors:
                        href = crawl.get_attribute_from_element(anchor, "href")
                        if href and href not in chapters_list:
                            chapters_list.append(href)
        else:
            print("Error: Failed to load main page for chapter list extraction.")
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
