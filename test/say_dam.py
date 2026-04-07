import sys
import os
import threading
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.locators import say_dam as lo

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

    password = "MOE"
    
    for chap_url, chap_num in chapter_data:
        print(f"Crawling: {chap_url}")
        crawl.go_to_webpage(chap_url)
        crawl.wait_for_page_load(10)
        if crawl.is_element_visible(lo.password_input_field):
            print(f"Password field found for Chap {chap_num}. Trying passwords...")
            crawl.input_text(lo.password_input_field, password)
            crawl.click_element(lo.password_submit_btn)
            # Using a short sleep is sometimes necessary for pages with JS redirects.
            crawl.sleep(5)
            crawl.wait_for_page_load(10)
            if crawl.is_element_visible(lo.password_input_field) is False:
                print(f"Incorrect password for chapter {chap_num}. Skipping...")
                
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

    chapters_list = []

    main_url = "https://phuongmoe1512.wordpress.com/2020/08/09/hoan-hien-dai-19-say-dam/"
    
    crawl.go_to_webpage(main_url)
    crawl.wait_for_page_load(10)
    chap_list = crawl.find_elements(lo.chap_list)

    chapters_list = []
    forbidden_words = ["facebook", "hungole"]

    for chap in chap_list:
        anchors = crawl.find_elements(lo.a_tag, chap)
        for anchor in anchors:
            url = crawl.get_attribute_from_element(anchor, "href")
            if url and not any(word in url for word in forbidden_words):
                chapters_list.append(url)
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
    main("say_dam")

'''Note: run this code using cmd: uv run test/say_dam.py'''