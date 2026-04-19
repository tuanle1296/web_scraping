import sys
import os
import math

import concurrent.futures
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.file_manager import get_config_folder_id
from src.newlocators import truyenfullvision as lo
from src.drive_manager import DriveManager


storyName = "duoi_mai_hien"
main_url = "https://truyenfull.vision/duoi-mai-hien/"

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
        
        # Close browser immediately as we use API for crawling, but keep instance for self.path
        crawl.quit_driver()

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
    urls = []

    with Base(False) as crawl:
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
            print(f"Page {main_url} did not load correctly. Stopping.")
            return
        

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

    # Prepare data: list of (url, chapter_number)
    indexed_chapters = []
    for i, url in enumerate(chapters_list):
        indexed_chapters.append((url, i + 1))

    # Split into chunks for parallel processing
    num_threads = 5  # Adjust number of threads as needed
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
