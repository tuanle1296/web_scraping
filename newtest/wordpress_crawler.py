import sys
import os
import concurrent.futures
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.file_manager import get_config_folder_id
from src.newlocators import wordpress as lo
from src.drive_manager import DriveManager


storyName = "tuyet_bien_ngap_ngan"
main_url = "https://luclacnho2810.wordpress.com/tuyet-bien-ngap-ngan-nghiem-tuyet-gioi-2/"
forbidden_words = []
passwords_dict = {}
passwords_string = ""


def crawl_worker(chapter_data, folder_name):
    """
    Worker function to process a chunk of chapters.
    chapter_data: list of tuples (url, chapter_number)
    """
    with Base() as crawl:
        try:
            crawl.set_path(folder_name)
        except Exception as e:
            print(f"Error while setting folder path: {e}")
        
        try:
            for chap_url, chap_num in chapter_data:
                print(f"Crawling: {chap_url}")
                
                crawl.go_to_webpage(chap_url)

                if not crawl.wait_for_page_load(10):
                    print(f"Page {chap_url} did not load correctly. Skipping.")
                    continue

                if crawl.is_element_visible(lo.password_input_field):
                    print(f"Password field found for Chap {chap_num}. Trying passwords...")
                    
                    if (passwords_dict) and (passwords_string is None):
                        password = ""
                        for key, value in passwords_dict.items():
                            if str(chap_num) == key:
                                password = value
                    elif (not passwords_dict) and (passwords_string is not None):
                        password = passwords_string

                        crawl.input_text(lo.password_input_field, password)
                        crawl.click_element(lo.password_submit_btn)
                        if (crawl.wait_for_element_visible(lo.chapter_content), 5):
                            print(f"Password \"{password}\" for Chap \"{chap_num}\" is correct.") 

                title = crawl.get_element_text(lo.chapter_title)
                content = crawl.get_element_text(lo.chapter_content)
                crawl.add_text_to_doc_file(title, content, "chapter_" + str(chap_num))
            
        except Exception as e:
            print(f"Error crawling {chap_url}: {e}")


def main(folder_name):
    print("=======Create folder=======")
    
    # Create folder once
    temp_crawl = Base(True)
    try:
        temp_crawl.create_folder(folder_name)
        print(f"=======Created folder {folder_name} successfully======")
    except Exception as e:
        print(f"Error creating folder: {e}")
        return
    finally:
        temp_crawl.quit_driver()

    chapters_list = []

    with Base(False) as crawl:
        crawl.go_to_webpage(main_url)
        if not crawl.wait_for_page_load(10):
            print(f"Page {main_url} did not load correctly.")
            return
        
        # 1. Try finding anchors in p_chap_list first
        chap_list = crawl.find_elements(lo.p_chap_list)
        for chap in chap_list:
            anchors = crawl.find_elements(lo.a_tag, chap)
            for anchor in anchors:
                url = crawl.get_attribute_from_element(anchor, "href")
                if url and not any(word in url for word in forbidden_words) and (url not in chapters_list):
                    chapters_list.append(url)
        
        # 2. If no chapters found, try finding anchors in normal_chap_list
        if not chapters_list:
            print("No links found in p_chap_list, trying normal_chap_list...")
            normal_chaps = crawl.find_elements(lo.normal_chap_list)
            for chap in normal_chaps:
                anchors = crawl.find_elements(lo.a_tag, chap)
                for anchor in anchors:
                    url = crawl.get_attribute_from_element(anchor, "href")
                    if url and not any(word in url for word in forbidden_words) and (url not in chapters_list):
                        chapters_list.append(url)

    if not chapters_list:
        print("Error: No chapters found to crawl. Exiting.")
        return

    # Prepare data: list of (url, chapter_number)
    indexed_chapters = []
    for i, url in enumerate(chapters_list):
        indexed_chapters.append((url, i + 1))

    # Split into chunks for parallel processing
    num_threads = 3  # Adjust number of threads as needed
    chunk_size = math.ceil(len(indexed_chapters) / num_threads)
    chunks = [indexed_chapters[i:i + chunk_size] for i in range(0, len(indexed_chapters), chunk_size)]

    print(f"Starting {num_threads} threads...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(lambda chunk: crawl_worker(chunk, folder_name), chunks)
    print("=======All threads finished=======")
    print(f"===========Zipping {storyName} folder===========")
    zip_path = None
    try:
        with Base(True) as zip_crawl:
            zip_path = zip_crawl.zip_folder(storyName)
    except Exception as e:
        print(f"Folder {storyName} zip unsuccessfully: {e}")
        return
    
    if zip_path:
        print(f"Zip folder {storyName} completed: {zip_path}")
        print("=======Uploading to Google Drive=======")
        try:
            drive = DriveManager()
            drive.upload_zip(zip_path, folder_id=get_config_folder_id())
        except Exception as e:
            print(f"Upload to Google Drive failed: {e}")

if __name__ == '__main__':
    main(storyName)
