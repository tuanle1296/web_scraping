
import sys
import os
import threading
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.locators import sao_tren_troi_rat_xa_sao_cua_anh_that_gan as lo



def main(folder_name):
    print("=======Create folder=======")
    crawl = base(False)
    try:
        crawl.create_folder(folder_name)
        print("=======Created folder successfully======")
    except Exception as e:
        print(f"Error creating folder: {e}")

    main_url = "https://kenhtruyenfull.com/doc-truyen/sao-tren-troi-rat-xa-sao-cua-anh-that-gan/chuong-1-1"
    crawl.go_to_webpage(main_url)
    status = True
    while status:
        
        crawl.wait_for_page_load(10)

        title = crawl.get_element_text(lo.chapter_title)
        content = crawl.get_element_text(lo.chapter_content)
        current_url = crawl.get_current_url()
        file_name = current_url.split('/')[-1]
        crawl.add_text_to_doc_file(title, content, file_name)

        class_attribute = crawl.get_attribute_from_element(lo.next_chap_btn, "class")
        if "disabled" in class_attribute:
            status = False
        else:
            crawl.click_element(lo.next_chap_btn)
        
    
    
    
    print("=======Completed=======")

if __name__ == '__main__':
    main("sao_tren_troi_rat_xa_sao_cua_anh_that_gan")

'''Note: run this code using cmd: uv run test/sao_tren_troi_rat_xa_sao_cua_anh_that_gan.py'''
