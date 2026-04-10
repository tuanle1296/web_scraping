import sys
import os
import math

import concurrent.futures
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.newlocators import mongtruyen as lo


storyName = "anh_den_cung_rang_dong"
main_url = "https://mongtruyen.com/anh-den-cung-rang-dong.html"
login_url = "https://mongtruyen.com/dang-nhap.html"
username = "tuantest"
password_signin = "04121996"
passwords = {"": ""}


def crawl_worker(chapter_data, folder_name):
    """
    Worker function to process a chunk of chapters.
    chapter_data: list of tuples (url, chapter_number)
    """
    crawl = base()
    try:
        crawl.set_path(folder_name)
    except Exception as e:
        print(f"Error while setting folder path: {e}")
    

    try:
        for chap_url, chap_num in chapter_data:
            print(f"Crawling: {chap_url}")
            crawl.go_to_webpage(chap_url)
            crawl.wait_for_page_load(10)
            # crawl.sleep(3)

            if crawl.is_element_visible(lo.password_input_field):
                # sign in first
                print(f"Password field found for Chap {chap_num}. Signing in and trying passwords...")
                crawl.go_to_webpage(login_url)
                crawl.wait_for_page_load(10)
                crawl.input_text(lo.username_signin_field, username)
                crawl.input_text(lo.password_signin_field, password_signin)
                crawl.click_element(lo.signin_submit_btn)
                if not crawl.wait_for_page_load(10):
                    print(f"Page {chap_url} did not load correctly. Skipping.")
                    continue

                # access the chap_url again to input password
                crawl.go_to_webpage(chap_url)
                if not crawl.wait_for_page_load(10):
                    print(f"Page {chap_url} did not load correctly. Skipping.")
                    continue
                
                password = ""
                print(f"Password field found for Chap {chap_num}. Trying passwords...")
                for key, value in passwords.items():
                    if str(chap_num) == key:
                        password = value
                    crawl.input_text(lo.password_input_field, password)
                    crawl.click_element(lo.password_submit_btn)
                    crawl.sleep(5)
                    if not crawl.wait_for_page_load(10):
                        print(f"Page {chap_url} did not load correctly. Skipping.")
                        continue
                    if crawl.is_element_visible(lo.password_input_field) is False:
                            print(f"Password \"{password}\" for Chap \"{chap_num}\" is correct.") 

            title = crawl.get_element_text(lo.chapter_title)
            content = crawl.get_element_text(lo.chapter_content)
            crawl.add_text_to_doc_file(title, content, "chapter_" + str(chap_num))
        
    except Exception as e:
        print(f"Error crawling {chap_url}: {e}")
    finally:
        crawl.quit_driver()


def main(folder_name):
    print(f"=======Create {folder_name} folder=======")
    crawl = base(False)
    try:
        crawl.create_folder(folder_name)
        print(f"=======Created folder {folder_name} successfully======")
    except Exception as e:
        return(f"Error creating folder: {e}")

    chapters_list = []
    urls = []

    crawl.go_to_webpage(main_url)
    if crawl.wait_for_page_load(10) is True:

        # check if page has pagination
        if (crawl.is_element_visible(lo.pagination) == False):
            urls.append(main_url)
        else:
            total_pages = crawl.find_elements(lo.page_link)[1:-1]
            page_range = len(total_pages)
            for i in range (1, page_range + 1):
                urls.append(main_url + f"?page={i}")
    

    for target_url in urls:
        print(f"Opening: {target_url}")
    
        crawl.go_to_webpage(target_url)
        if crawl.wait_for_page_load(10) is True:
            chap_list = crawl.find_elements(lo.chap_list)
            for chap in chap_list:
                anchors = crawl.find_elements(lo.a_tag, chap)
                for anchor in anchors:
                    chapters_list.append(crawl.get_attribute_from_element(anchor, "href"))
        else:
            print(f"Page {target_url} did not load correctly. Skipping.")
            continue
    crawl.quit_driver()  # Close the initial driver

    # Prepare data: list of (url, chapter_number)
    indexed_chapters = []
    for i, url in enumerate(chapters_list):
        indexed_chapters.append((url, i + 1))

    # Split into chunks for parallel processing
    # Careful when increasing number of threads, some page might be broken
    num_threads = 3  # Adjust number of threads as needed
    chunk_size = math.ceil(len(indexed_chapters) / num_threads)
    chunks = [indexed_chapters[i:i + chunk_size] for i in range(0, len(indexed_chapters), chunk_size)]

    print(f"Starting {num_threads} threads...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Truyền cả chunk_size vào hàm crawl_worker
        executor.map(lambda chunk: crawl_worker(chunk, folder_name), chunks)
        
    print("=======All threads finished=======")

if __name__ == '__main__':
    main(storyName)

'''Note: run this code using cmd: uv run test/mongtruyen_crawler.py'''
