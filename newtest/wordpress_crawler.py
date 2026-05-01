import sys
import os
import concurrent.futures
import math
from bs4 import BeautifulSoup
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium.webdriver.common.by import By
from src.base_functions import *
from src.file_manager import get_config_folder_id
from src.newlocators import wordpress as lo
from src.drive_manager import DriveManager


storyName = "soi_toi_roi"
main_url = "https://maymay1510.wordpress.com/2018/03/08/soi-toi-roi-2/"
forbidden_words = ["blog"]
forbidden_texts = "password"

# Define passwords dictionary based on ranges
passwords_dict = {}
# 21-30: "ChuDinh"
# for i in range(21, 31): passwords_dict[str(i)] = "ChuDinh"
# # 31-40: "LyHaDuong"
# for i in range(31, 41): passwords_dict[str(i)] = "LyHaDuong"
# # 41-50: "2308"
# for i in range(41, 51): passwords_dict[str(i)] = "2308"
# # 51-60: "VoGioi"
# for i in range(51, 61): passwords_dict[str(i)] = "VoGioi"
# # 61-76: "L"
# for i in range(61, 77): passwords_dict[str(i)] = "L"
# # 77-88: "25042026"
# for i in range(77, 89): passwords_dict[str(i)] = "25042026"

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
        
        for chap_url, chap_num in chapter_data:
            try:
                print(f"Crawling: {chap_url}")
                
                crawl.go_to_webpage(chap_url)

                if not crawl.wait_for_page_load(10):
                    print(f"Page {chap_url} did not load correctly. Skipping.")
                    continue

                password = ""
                if crawl.is_element_visible(lo.password_input_field):
                    print(f"Password field found for Chap {chap_num}. Trying passwords...")
                    
                    if passwords_dict and not passwords_string:
                        for key, value in passwords_dict.items():
                            if str(chap_num) == key:
                                password = value
                    elif not passwords_dict and passwords_string:
                        password = passwords_string

                    if password:
                        crawl.input_text(lo.password_input_field, password)
                        crawl.click_element(lo.password_submit_btn)
                        
                        if crawl.wait_for_element_visible(lo.chapter_content, 5):
                            print(f"Password \"{password}\" for Chap \"{chap_num}\" is correct.") 
                        
                        # Check for Google Drive link after entering password
                        if crawl.wait_for_element_visible(lo.link_after_enter_password, 5):
                            if (crawl.get_element_text(lo.link_after_enter_password) == "Nhấp vào dòng này để đọc truyện"):
                                print(f"Chapter \"{chap_num}\" need to go to drive to download manually. Skipping...")
                                continue
                    else:
                        print(f"No password found for Chap {chap_num}. Skipping password field.")

                title = crawl.get_element_text(lo.chapter_title)
                if (title == ""):
                    title = crawl.get_element_text(lo.chapter_title_2)
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

    with Base(True) as crawl:
        crawl.go_to_webpage(main_url)
        if not crawl.wait_for_page_load(10):
            print(f"Page {main_url} did not load correctly.")
            return
        
        # Use BeautifulSoup to find all anchors much faster than Selenium loops
        soup = BeautifulSoup(crawl.get_page_source(), "html.parser")
        
        # 1. Try finding anchors in p_chap_list first
        # lo.p_chap_list is (By.CSS_SELECTOR, "div.entry-content p")
        entry_content_ps = soup.select(lo.p_chap_list[1])
        for p in entry_content_ps:
            for anchor in p.find_all(lo.a_tag[1]):
                url = anchor.get('href')
                anchor_text = anchor.get_text()
                if url and not any(word in url for word in forbidden_words) and (url not in chapters_list) and (forbidden_texts not in anchor_text):
                    chapters_list.append(url)
        
        # 2. If no chapters found, try finding anchors in normal_chap_list
        # lo.normal_chap_list is (By.CSS_SELECTOR, "div.entry-content")
        if not chapters_list:
            print("No links found in p_chap_list, trying normal_chap_list...")
            entry_content = soup.select_one(lo.normal_chap_list[1])
            if entry_content:
                for anchor in entry_content.find_all(lo.a_tag[1]):
                    url = anchor.get('href')
                    anchor_text = anchor.get_text()
                    if url and not any(word in url for word in forbidden_words) and (url not in chapters_list) and (forbidden_texts not in anchor_text):
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
