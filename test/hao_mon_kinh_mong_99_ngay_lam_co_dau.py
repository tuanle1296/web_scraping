import sys
import os
import threading
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.locators import hao_mon_kinh_mong_99_ngay_lam_co_dau as lo


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

    failed_chapters = []
    for chap_url, chap_num in chapter_data:
        try:
            print(f"Crawling: {chap_url}")
            crawl.go_to_webpage(chap_url)
            if (crawl.wait_for_page_load(10)):
            # crawl.scroll_web_page_to_the_end()
                crawl.sleep(3)
                
                title = crawl.find_element(lo.chapter_title)
                content = crawl.find_element(lo.chapter_content)
                
                title_text = crawl.get_element_text(title)
                content_text = crawl.get_element_text(content)
                
                crawl.add_text_to_doc_file(title_text, content_text, "chapter_" + str(chap_num))
            else:
                print(f"Page {chap_url} did not load correctly. Skipping.")
                failed_chapters.append((chap_url, chap_num))

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
    for i in range (1, 6):
        main_url = f"https://truyenfull.vision/hao-mon-kinh-mong-99-ngay-lam-co-dau/trang-{i}/#list-chapter"
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
    main("hao_mon_kinh_mong_99_ngay_lam_co_dau")

'''Note: run this code using cmd: uv run test/hao_mon_kinh_mong_99_ngay_lam_co_dau.py'''
