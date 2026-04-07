import sys
import os
import threading
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.locators import hoa_hong_ky_uc as lo

# def crawl_worker(chapter_data, folder_name):
#     """
#     Worker function to process a chunk of chapters.
#     chapter_data: list of tuples (url, chapter_number)
#     """
#     crawl = base()
#     try:
#         crawl.create_folder(folder_name)
#     except:
#         pass
#     crawl.quit_driver()
    
#     for chap_url, chap_num in chapter_data:
#         print(f"Crawling: {chap_url}")
#         soup = crawl.crawl_data(chap_url)
#         if soup:
#             title = "chapter_" + str(chap_num)
#             content = crawl.crawl_text_from_soup(soup, lo.chapter_content[1])
#             crawl.add_text_to_doc_file(title, content, title)


def main(folder_name):
    print("=======Create folder=======")
    crawl = base(False)
    try:
        crawl.create_folder(folder_name)
        print("=======Created folder successfully======")
    except Exception as e:
        print(f"Error creating folder: {e}")

    # chapters_list = []

    main_url = "https://vntrungtam.info/thuvien/sach/hoa-hong-ky-uc"
    
    crawl.go_to_webpage(main_url)
    crawl.wait_for_page_load(10)
    chap_list = crawl.find_elements(lo.chap_list)

    # chapters_list = []

    index = 0
    for chap in chap_list:
        anchors = crawl.find_elements(lo.a_tag, chap)
        for anchor in anchors:
            crawl.scroll_into_view(anchor)
            crawl.click_element(anchor)
            crawl.sleep(5)
            crawl.wait_for_page_load(10)

            title = "chapter" + str(index)
            
            print(f"Crawling chapter: {title}")
            content = crawl.get_element_text(lo.chapter_content)
            crawl.add_text_to_doc_file(title, content, title)
            index += 1

            # url = crawl.get_attribute_from_element(anchor, "href")
            # if url and not any(word in url for word in forbidden_words):
            #     chapters_list.append(url)
    crawl.quit_driver()  # Close the initial driver

    
    print("=======All threads finished=======")

if __name__ == '__main__':
    main("hoa_hong_ky_uc")

'''Note: run this code using cmd: uv run test/hoa_hong_ky_uc.py'''