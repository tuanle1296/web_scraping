import sys
import os
import threading
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.locators import thuyen_cua_tay_giang_cuu_nguyet_hi as lo


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
    finally:
        crawl.quit_driver()  # Close browser immediately as we use API for crawling

    failed_chapters = []
    for chap_url, chap_num in chapter_data:
        try:
            print(f"Crawling: {chap_url}")
            soup = crawl.crawl_data(chap_url)
            title = crawl.crawl_text_from_soup(soup, lo.chapter_title[1])
            content = crawl.crawl_text_from_soup(soup, lo.chapter_content[1])
            crawl.add_text_to_doc_file(title, content, "chapter_" + str(chap_num))

        except Exception as e:
            failed_chapters.append((chap_url, chap_num))
            print(f"====== Warning: Error crawling {chap_url}")
            print(e)

    crawl.quit_driver()

    if failed_chapters:
        print(f"Failed chapters in this worker: {failed_chapters}")



def main(folder_name):
    print("=======Create folder=======")
    crawl = base(False)
    try:
        crawl.create_folder(folder_name)
        print("=======Created folder successfully======")
    except Exception as e:
        print(f"Error creating folder: {e}")

    chapters_list = []
    for i in range (1, 4):
        main_url = f"https://truyenfull.vision/thuyen-cua-tay-giang-cuu-nguyet-hi/trang-{i}/#list-chapter"
        print(main_url)
    
        crawl.go_to_webpage(main_url)
        crawl.wait_for_page_load(10)
        chap_list = crawl.find_elements(lo.chap_list)
        for chap in chap_list:
            anchors = crawl.find_elements(lo.a_tag, chap)
            for anchor in anchors:
                chap_url = crawl.get_attribute_from_element(anchor, "href")
                if chap_url and "#list-chapter" not in chap_url:
                    chapters_list.append(chap_url)
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
    main("thuyen_cua_tay_giang_cuu_nguyet_hi")

'''Note: run this code using cmd: uv run test/thuyen_cua_tay_giang_cuu_nguyet_hi.py'''
