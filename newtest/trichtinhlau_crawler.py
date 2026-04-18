import sys
import os
import threading
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.base_functions import *
from src.newlocators import trichtinhlau as lo


def crawl_worker(chapter_data, folder_name):
    """
    Worker function to process a chunk of chapters.
    Each thread creates its own browser instance.
    """
    # CORRECT: Instantiate Base INSIDE the worker to ensure each thread has its own browser
    with Base(is_headless_mode=False) as crawl:
        try:
            crawl.set_path(folder_name)
        except:
            pass
            
        crawl.maximize_browser()
        failed_chapters = []

        for chap_url, chap_num in chapter_data:
            try:
                # Password logic based on chapter number
                password = "1" if chap_num <= 100 else "2"

                print(f"Crawling: {chap_url}")
                
                crawl.go_to_webpage(chap_url)
                crawl.wait_for_page_load(10)
                crawl.sleep(3)

                # Handle password-protected content
                if crawl.is_element_visible(lo.password_input_field):
                    crawl.input_text(lo.password_input_field, password)
                    crawl.sleep(2)
                    crawl.click_element(lo.password_submit_btn, force_js=True)
                    crawl.wait_for_page_load(10)
                    crawl.sleep(3)

                # Ensure content is visible before extraction
                crawl.wait_for_element_visible(lo.chapter_content, timeout=10)

                print(f"Extracting text for chapter {chap_num}...")
                title = crawl.get_element_text(lo.chapter_title, extract_hidden=False)
                content = crawl.get_element_text(lo.chapter_content, extract_hidden=False)
                
                # Save as a .docx file inside the specified folder
                crawl.add_text_to_doc_file(title, content, "chapter_" + str(chap_num))

                crawl.sleep(3)

            except Exception as e:
                failed_chapters.append((chap_url, chap_num))
                print(f"====== Warning: Error crawling {chap_url}: {e}")

        if failed_chapters:
            print(f"Failed chapters in this worker: {failed_chapters}")
        
        # Base context manager will call quit_driver() automatically on exit


def main(folder_name):
    print("=======Initializing Master Browser to collect chapter links=======")
    # Step 1: Use a master browser to collect all chapter links first
    chapters_list = []
    with Base(is_headless_mode=False) as master_crawl:
        try:
            master_crawl.create_folder(folder_name)
            print("=======Folder setup complete======")
        except Exception as e:
            print(f"Error during folder setup: {e}")

        # Loop through pages to gather URLs
        for i in range(1, 5):
            main_url = f"https://trichtinhlau.com/xem-truyen/khach-tro?page={i}"
            print(f"Gathering links from page {i}...")
            master_crawl.go_to_webpage(main_url)
            master_crawl.wait_for_page_load(10)
            master_crawl.sleep(2)
            
            chap_list = master_crawl.find_elements(lo.chap_list)
            for chap in chap_list:
                anchors = master_crawl.find_elements(lo.a_tag, chap)
                for anchor in anchors:
                    href = master_crawl.get_attribute_from_element(anchor, "href")
                    if href:
                        chapters_list.append(href)

    if not chapters_list:
        print("Error: No chapters found!")
        return

    # Prepare indexed data for threading
    indexed_chapters = [(url, i + 1) for i, url in enumerate(chapters_list)]

    # Split into chunks for parallel processing
    num_threads = 2  # Adjust as needed (each thread = 1 browser)
    chunk_size = math.ceil(len(indexed_chapters) / num_threads)
    chunks = [indexed_chapters[i:i + chunk_size] for i in range(0, len(indexed_chapters), chunk_size)]

    # Step 2: Start worker threads, each launching its own browser
    threads = []
    print(f"Starting {len(chunks)} parallel browser threads...")
    for chunk in chunks:
        t = threading.Thread(target=crawl_worker, args=(chunk, folder_name))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print("=======All parallel processes finished=======")

if __name__ == '__main__':
    main("khach_tro")

'''Note: run this code using cmd: uv run newtest/trichtinhlau_crawler.py'''
