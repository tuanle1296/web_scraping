import sys
import os
import math
import argparse
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.file_manager import get_config_folder_id
from src.newlocators import vuaduongotp as lo
from src.drive_manager import DriveManager

def crawl_worker(chapter_data, folder_name):
    """
    Worker function to process a chunk of chapters.
    """
    with Base(True) as crawl:
        try:
            crawl.set_path(folder_name)
        except Exception as e:
            print(f"Error while setting folder path: {e}")
        
        # Close browser immediately as we use API for crawling
        crawl.quit_driver()

        for chap_url, chap_num in chapter_data:
            try:
                print(f"--- Crawling: Chapter {chap_num} | URL: {chap_url} ---")
                soup = crawl.crawl_data(chap_url)
                if soup:
                    title = crawl.crawl_text_from_soup(soup, lo.chapter_title[1])
                    content = crawl.crawl_text_from_soup(soup, lo.chapter_content[1])
                    crawl.add_text_to_doc_file(title, content, f"chapter_{chap_num}")
                    print(f"Successfully saved Chapter {chap_num}")
                else:
                    print(f"Error: Failed to fetch data for chapter {chap_num}")
            except Exception as e:
                print(f"Exception during chapter {chap_num} crawl: {e}")

def main():
    parser = argparse.ArgumentParser(description='VuaDuongOTP Crawler (Docker Optimized)')
    parser.add_argument('--url', type=str, required=True, help='Main story URL')
    parser.add_argument('--name', type=str, required=True, help='Output folder name')
    args = parser.parse_args()

    main_url = args.url
    storyName = args.name

    print(f"======= Starting crawl for: {storyName} =======")
    
    # Initialize storage folder
    with Base(True) as temp_crawl:
        try:
            temp_crawl.create_folder(storyName)
        except Exception as e:
            print(f"Error creating folder: {e}")
            return

    chapters_list = []

    with Base(True) as crawl:
        crawl.go_to_webpage(main_url)
        if crawl.wait_for_element_visible(lo.chapter_tab, 15):
            crawl.click_element(lo.chapter_tab)
            if crawl.wait_for_element_visible(lo.chap_list, 5):
                chap_list_elems = crawl.find_elements(lo.chap_list)
                for container in chap_list_elems:
                    anchors = crawl.find_elements(lo.a_tag, container)
                    for anchor in anchors:
                        href = crawl.get_attribute_from_element(anchor, "href")
                        if href and href not in chapters_list:
                            chapters_list.append(href)
            else:
               print("Error: Chapter list not loaded after clicking tab.")
               return
        else:
            print(f"Error: Chapter tab not found on {main_url}")
            return

    # Prepare data for multithreading
    indexed_chapters = [(url, i + 1) for i, url in enumerate(chapters_list)]
    num_threads = 5
    chunk_size = math.ceil(len(indexed_chapters) / num_threads)
    chunks = [indexed_chapters[i:i + chunk_size] for i in range(0, len(indexed_chapters), chunk_size)]

    print(f"Launching {len(chunks)} threads for {len(chapters_list)} chapters...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(lambda chunk: crawl_worker(chunk, storyName), chunks)
        
    print("======= Finished crawling all chapters =======")
    
    # Zip and Upload to Drive
    try:
        with Base(True) as zip_crawl:
            zip_path = zip_crawl.zip_folder(storyName)
            if zip_path:
                print(f"Folder zipped successfully: {zip_path}")
                drive = DriveManager()
                drive.upload_zip(zip_path, folder_id=get_config_folder_id())
                print("======= Successfully uploaded to Google Drive =======")
    except Exception as e:
        print(f"Error during zipping or uploading: {e}")

if __name__ == '__main__':
    main()
