import sys
import os
import math

import concurrent.futures
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.newlocators import truyenfullvision as lo


storyName = "gia_lai_co_mot_nguoi_nhu_em"
main_url = "https://truyenfull.vision/gia-lai-co-mot-nguoi-nhu-em/"



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
            print(f"====== Warning: Error crawling {chap_url}", e)

    if failed_chapters:
        print(f"Failed chapters in this worker: {failed_chapters}")


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
    if crawl.wait_for_page_load(10):
        
        # check if page has pagination
        paginition = crawl.find_element(lo.pagination)
        if (paginition is None):
            urls.append(main_url)
        else:
            total_pages = crawl.find_elements(lo.page_link, paginition)[:-1]
            page_range = len(total_pages)
            for i in range (1, page_range + 1):
                urls.append(main_url + f"trang-{i}/#list-chapter")
    else:
        return(f"Page {main_url} did not load correctly. Stopping.")
    

    for target_url in urls:
        print(f"Opening: {target_url}")
    
        crawl.go_to_webpage(target_url)
        if crawl.wait_for_page_load(10):
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

'''Note: run this code using cmd: uv run test/truyenfullvision_crawler.py'''
