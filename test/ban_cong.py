import sys
import os
import math

import concurrent.futures
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.locators import ban_cong as lo


def crawl_worker(chapter_data, folder_name):
    """
    Worker function to process a chunk of chapters.
    chapter_data: list of tuples (url, chapter_number)
    """
    crawl = base(is_headless_mode=True)
    try:
        crawl.create_folder(folder_name)
    except:
        pass
    finally:
        crawl.set_path(folder_name)
    
    try:
        for chap_url, chap_num in chapter_data:
            try:
                print(f"Crawling: {chap_url}")
                crawl.go_to_webpage(chap_url)
                crawl.sleep(3)
                if (crawl.is_element_visible(lo.age_submit_btn)):
                    crawl.click_element(lo.age_submit_btn)
                    crawl.sleep(5)
                crawl.wait_for_page_load(10)
                title = crawl.get_element_text(lo.chapter_title)
                content = crawl.get_element_text(lo.chapter_content)
                crawl.add_text_to_doc_file(title, content, "chapter_" + str(chap_num))
            except Exception as e:
                print(f"====== Warning: Error crawling {chap_url}", e)
    except Exception as faltal_error:
        print(f"Fatal error cause crash worker: {faltal_error}")
    finally:
            crawl.quit_driver()
        




def main(folder_name):
    print("=======Create folder=======")
    crawl = base(False)
    try:
        crawl.create_folder(folder_name)
        print("=======Created folder successfully======")
    except Exception as e:
        print(f"Error creating folder: {e}")

    chapters_list = []
    main_url = "https://suonxaochuangot.net/ban-cong/"
    
    crawl.go_to_webpage(main_url)
    crawl.wait_for_page_load(10)
    crawl.sleep(5)
    if (crawl.is_element_visible(lo.age_submit_btn)):
        crawl.click_element(lo.age_submit_btn)
        crawl.sleep(5)
    chap_list = crawl.find_elements(lo.chap_list)
    for chap in chap_list:
        anchors = crawl.find_elements(lo.a_tag, chap)
        for anchor in anchors:
            chapters_list.append(crawl.get_attribute_from_element(anchor, "href"))
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

    print(f"Starting {len(chunks)} threads...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Truyền cả chunk_size vào hàm crawl_worker
        executor.map(lambda chunk: crawl_worker(chunk, folder_name), chunks)
    print("=======All threads finished=======")

if __name__ == '__main__':
    main("ban_cong")

'''Note: run this code using cmd: uv run test/ban_cong.py'''
