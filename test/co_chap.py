import sys
import os
import concurrent.futures
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.locators import co_chap as lo


def crawl_worker(chap_data, folder_name):
   
    crawl = base()
    try:
        crawl.create_folder(folder_name)
    except:
        pass
    finally:
        crawl.set_path(folder_name)
    
    # try:
    
    for chap_url, chap_num in chap_data:
        try:
            print(f"Crawling: {chap_url}")
                
                # Dùng hàm crawl_data (BS4/Requests) của bạn
            soup = crawl.crawl_data(chap_url)
            if soup:
                title = crawl.crawl_text_from_soup(soup, lo.chapter_title[1])
                content = crawl.crawl_text_from_soup(soup, lo.chapter_content[1])
                    
                crawl.add_text_to_doc_file(title, content, "chapter_" + str(chap_num))
                # return f"Complete chapter: {chap_num}"
            else:
                print(f"Failed to crawl chapter: {chap_num}")

        except Exception as e:
            print(f"====== Warning: Error crawling {chap_url}: {e}")
            
    # finally:
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
    for i in range (1, 3):
        main_url = f"https://truyenfull.vision/co-chap-mong-tieu-nhi/trang-{i}/#list-chapter"
    
        crawl.go_to_webpage(main_url)
        crawl.wait_for_page_load(10)
        crawl.sleep(3)
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
    main("co_chap")

'''Note: run this code using cmd: uv run test/co_chap.py'''
