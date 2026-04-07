
import sys
import os
import threading
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.locators import phung_thanh as lo



def main(folder_name):
    print("=======Create folder=======")
    crawl = base(False)
    try:
        crawl.create_folder(folder_name)
        print("=======Created folder successfully======")
    except Exception as e:
        print(f"Error creating folder: {e}")

    main_url = "https://truyencom.com/phung-thanh/chuong-1.html"
    crawl.go_to_webpage(main_url)
    status = True
    while status:
        
        crawl.wait_for_page_load(10)
        crawl.sleep(3)
        title = crawl.get_element_text(lo.chapter_title)
        content = crawl.get_element_text(lo.chapter_content)
        current_url = crawl.get_current_url()
        print(f"Crawling: {current_url}")
        file_name = current_url.split('/')[-1].split('.')[0]
        crawl.add_text_to_doc_file(title, content, file_name)

        class_attribute = crawl.get_attribute_from_element(lo.next_chap_btn, "class")
        if "disabled" in class_attribute:
            status = False
        else:
            crawl.click_element(lo.next_chap_btn)
    
    
    print("=======Completed=======")

if __name__ == '__main__':
    main("phung_thanh")

'''Note: run this code using cmd: uv run test/phung_thanh.py'''
