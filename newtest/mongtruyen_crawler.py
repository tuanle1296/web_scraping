import sys
import os
import math

import concurrent.futures
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.file_manager import get_config_folder_id
from src.newlocators import mongtruyen as lo
from src.drive_manager import DriveManager


storyName = "ca_khong_co_chan"
main_url = "https://mongtruyen.com/ca-khong-co-chan.html"
login_url = "https://mongtruyen.com/dang-nhap.html"
username = "tuantest"
password_signin = "04121996"
passwords_dict = {}
passwords_string = "6868"


def crawl_worker(chapter_data, folder_name):
    """
    Worker function to process a chunk of chapters.
    chapter_data: list of tuples (url, chapter_number)
    """
    with Base(False) as crawl:
        try:
            crawl.set_path(folder_name)
        except Exception as e:
            print(f"Error while setting folder path: {e}")
        
        # Sign in first to enter password in any chapters if needed
        
        crawl.go_to_webpage(login_url)
        if (crawl.wait_for_page_load(10) is False):
            print(f"Page {login_url} did not load correctly. Stopping worker.")
            return

        crawl.input_text(lo.username_signin_field, username)
        crawl.input_text(lo.password_signin_field, password_signin)
        crawl.click_element(lo.signin_submit_btn)
        crawl.sleep(5)

        try:
            for chap_url, chap_num in chapter_data:
                print(f"Crawling: {chap_url}")
                
                crawl.go_to_webpage(chap_url)

                if not crawl.wait_for_page_load(10):
                    print(f"Page {chap_url} did not load correctly. Skipping.")
                    continue

                if (crawl.is_element_visible(lo.accept_warning_btn)):
                    crawl.click_element(lo.accept_warning_btn)
                    crawl.sleep(2)
                if (crawl.wait_for_page_load(10) is False):
                    print(f"Chapter {chap_url} did not load correctly. Skipping")
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
    print(f"=======Create {folder_name} folder=======")
    
    # Create folder once at the start
    temp_crawl = Base(True) # Use a temporary instance just to create the folder
    try:
        temp_crawl.create_folder(folder_name)
        print(f"=======Created folder {folder_name} successfully======")
    except Exception as e:
        print(f"Error creating folder: {e}")
        return
    finally:
        temp_crawl.quit_driver()

    chapters_list = []
    urls = []

    with Base(False) as crawl:
        crawl.go_to_webpage(main_url)
        
        if (crawl.is_element_visible(lo.accept_warning_btn)):
            crawl.click_element(lo.accept_warning_btn)

        if crawl.wait_for_page_load(10) is True:
            # check if page has pagination
            if (crawl.is_element_visible(lo.pagination) == False):
                urls.append(main_url)
            else:
                total_pages = crawl.find_elements(lo.page_link)[-2].text
                for i in range (1, int(total_pages) + 1):
                    urls.append(main_url + f"?page={i}")
        

        for target_url in urls:
            print(f"Opening: {target_url}")
        
            crawl.go_to_webpage(target_url)
            crawl.sleep(2)
            if crawl.wait_for_page_load(10) is True:
                chap_list = crawl.find_elements(lo.chap_list)
                for chap in chap_list:
                    anchors = crawl.find_elements(lo.a_tag, chap)
                    for anchor in anchors:
                        chapters_list.append(crawl.get_attribute_from_element(anchor, "href"))
            else:
                print(f"Page {target_url} did not load correctly. Skipping.")
                continue

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
