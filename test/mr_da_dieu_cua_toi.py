
import sys
import os
import threading
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.locators import mr_da_dieu_cua_toi as lo



def main(folder_name):
    print("=======Create folder=======")
    crawl = base(False)
    try:
        crawl.create_folder(folder_name)
        print("=======Created folder successfully======")
    except Exception as e:
        print(f"Error creating folder: {e}")

    main_url = "https://www.wattpad.com/682814585-mr-%C4%91%C3%A0-%C4%91i%E1%BB%83u-c%E1%BB%A7a-t%C3%B4i-h%C3%A0m-y%C3%AAn-ph%E1%BA%A7n-m%E1%BB%9F-%C4%91%E1%BA%A7u"
    # crawl.go_to_webpage(main_url)
    status = True
    index = 1
    while status:
        crawl.go_to_webpage(main_url)
        crawl.wait_for_page_load(10)
        # crawl.sleep(5)
        title = crawl.get_element_text(lo.chapter_title)
        at_the_end = False
        while at_the_end == False:
            crawl.scroll_web_page_to_the_end()
            crawl.sleep(3)
            at_the_end = crawl.is_element_visible(lo.footer)

        content = crawl.get_element_text(lo.chapter_content)
        
        # crawl.scroll_into_view(lo.next_chap_btn)
        current_url = crawl.get_current_url()
        print(f"Crawling: {current_url}")
        crawl.add_text_to_doc_file(title, content, "chapter_" + str(index))
        index += 1
        crawl.sleep(5)
        next_chap_btn = crawl.find_element(lo.next_chap_btn)

        a_tag = crawl.find_element(lo.a_tag, next_chap_btn)

        class_attribute = crawl.get_attribute_from_element(a_tag, "class")
        if "disabled" in class_attribute:
            status = False
        main_url = crawl.get_attribute_from_element(a_tag, "href")
        # else:
        #     crawl.click_element(lo.next_chap_btn)
    
    
    print("=======Completed=======")

if __name__ == '__main__':
    main("mr_da_dieu_cua_toi")

'''Note: run this code using cmd: uv run test/mr_da_dieu_cua_toi.py'''
