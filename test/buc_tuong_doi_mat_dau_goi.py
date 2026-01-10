import sys
import os
import threading
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.locators import buc_tuong_doi_mat_dau_goi as lo


def crawl_worker(chapter_data, folder_name):
    """
    Worker function to process a chunk of chapters.
    chapter_data: list of tuples (url, chapter_number)
    """
    crawl = base(False)
    try:
        crawl.create_folder(folder_name)
    except:
        pass
    passwords = ["GIUGINVESINHTHATTOT", "01072021", "2011"]

    for chap_url, chap_num in chapter_data:
        crawl.go_to_webpage(chap_url)
        if not crawl.wait_for_page_load(10):
            print(f"Page {chap_url} did not load correctly. Skipping.")
            continue

        if crawl.is_element_visible(lo.password_field):
            print(f"Password field found for Chap {chap_num}. Trying passwords...")
            password_correct = False
            for password in passwords:
                # Re-find element to avoid StaleElementReferenceException
                password_input = crawl.find_element(lo.password_field)
                if not password_input:
                    print("Could not find password field after a password attempt. Skipping chapter.")
                    break  # breaks inner password loop

                crawl.input_text(password_input, password)
                crawl.click_element(lo.submit_password_btn)
                # Using a short sleep is sometimes necessary for pages with JS redirects.
                crawl.sleep(5)
                crawl.wait_for_page_load(10)

                # If the invalid password message is NOT visible, the password was correct.
                if not crawl.is_element_visible(lo.invalid_password_message):
                    password_correct = True
                    print(f"Password accepted for Chap {chap_num}.")
                    break  # breaks inner password loop

            if not password_correct:
                print(f"All passwords failed for {chap_url}. Skipping.")
                continue  # continues to next chapter in outer loop
        else:
            print(f"No password required for Chap {chap_num}.")

        print(f"Crawling: {chap_url}")
        title = crawl.get_element_text(lo.chap_title)
        content = crawl.get_element_text(lo.chap_content)

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

    main_url = "https://thibanmayao.wordpress.com/2021/07/01/buc-tuong-doi-mat-dau-goi-on-nhu-nhat-dao/"
    crawl.go_to_webpage(main_url)
    crawl.wait_for_page_load(10)
    chap_list = crawl.find_element(lo.chap_urls_list)
    urls_list = crawl.find_elements(lo.a_tag, chap_list)

    chapters_list = [crawl.get_attribute_from_element(url, "href") for url in urls_list]
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
    main("buc_tuong_doi_mat_dau_goi")

'''Note: run this code using cmd: python3 test/buc_tuong_doi_mat_dau_goi.py'''
