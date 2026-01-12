import sys
import os
import threading
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.locators import co_chap as lo


def crawl_worker(chapter_data, folder_name):
    """
    Worker function to process a chunk of chapters.
    chapter_data: list of tuples (url, chapter_number)
    """
    crawl = base()
    try:
        crawl.create_folder(folder_name)
    except:
        pass

    for chap_url, chap_num in chapter_data:
        crawl.go_to_webpage(chap_url)
        if not crawl.wait_for_page_load(15):
            print(f"Page {chap_url} did not load correctly. Skipping.")
            continue
        
        print(f"Crawling: {chap_url}")
        title = crawl.get_element_text(lo.chapter_title)
        content = crawl.get_element_text(lo.chapter_content)

        crawl.add_text_to_doc_file(title, content, "chapter_" + str(chap_num))

    crawl.quit_driver()


def main(folder_name):
    print("=======Create folder=======")
    crawl = base(False)
    try:
        crawl.create_folder(folder_name)
        print("=======Created folder successfully======")
    except Exception as e:
        print(f"Error creating folder: {e}")

    main_url_1 = "https://truyenfull.vision/co-chap-mong-tieu-nhi/trang-1/#list-chapter"
    main_url_2 = "https://truyenfull.vision/co-chap-mong-tieu-nhi/trang-2/#list-chapter"
    crawl.go_to_webpage(main_url_1)
    crawl.wait_for_page_load(10)
    chap_list = crawl.find_elements(lo.chap_list)
    urls_list_1 = []
    for chap in chap_list:
        urls_list_1.extend(crawl.find_elements(lo.a_tag, chap))
    
    chapters_list_1 = [crawl.get_attribute_from_element(url, "href") for url in urls_list_1]

    crawl.go_to_webpage(main_url_2)
    crawl.wait_for_page_load(10)
    chap_list = crawl.find_elements(lo.chap_list)
    urls_list_2 = []
    for chap in chap_list:
        urls_list_2.extend(crawl.find_elements(lo.a_tag, chap))
        
    chapters_list_2 = [crawl.get_attribute_from_element(url, "href") for url in urls_list_2]
    
    chapters_list = chapters_list_1 + chapters_list_2
    crawl.quit_driver()  # Close the initial driver

    # Prepare data: list of (url, chapter_number)
    indexed_chapters = []
    for i, url in enumerate(chapters_list):
        indexed_chapters.append((url, i + 1))

    # Split into chunks for parallel processing
    num_threads = 3  # Adjust number of threads as needed
    chunk_size = math.ceil(len(indexed_chapters) / num_threads)
    chunks = [indexed_chapters[i:i + chunk_size] for i in range(0, len(indexed_chapters), chunk_size)]

    threads = []
    print(f"Starting {len(chunks)} threads...")
    for chunk in chunks:
        t = threading.Thread(target=crawl_worker, args=(chunk, folder_name))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print("=======All threads finished=======")

if __name__ == '__main__':
    main("co_chap")

'''Note: run this code using cmd: python3 test/co_chap.py'''
