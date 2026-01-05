import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.locators import anh_den_hoa_le


def main(folder_name):
        print("=======Create folder=======")
        crawl = base(False)
        try:
            crawl.create_folder(folder_name)
            print("=======Created folder successfully======")
        except Exception as e:
            print(f"Error creating folder: {e}")
        
        chap = 1
        
        while (chap < 47):
            main_page_url = f"https://truyenfull.vision/anh-den-hoa-le-phat-ha-lao-yeu/chuong-{chap}/"
            print(f"Crawling chap: {main_page_url}")
        
            try:
                crawl.go_to_webpage(main_page_url)
                crawl.wait_for_element_visible(anh_den_hoa_le.chap_title, 10)
                crawl.wait_for_element_visible(anh_den_hoa_le.chap_content, 10)

                title = crawl.get_element_text(anh_den_hoa_le.chap_title)
                content = crawl.get_element_text(anh_den_hoa_le.chap_content)
                crawl.add_text_to_doc_file(title, content, "chapter_" + str(chap))
                chap += 1
                    
            except Exception as e:
                raise Exception(f"Error: {e}")
        crawl.quit_driver()

if __name__ == '__main__':
    main("anh_den_hoa_le")
