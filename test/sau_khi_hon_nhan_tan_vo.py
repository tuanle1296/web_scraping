import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.locators import sau_khi_hon_nhan_tan_vo


def main(folder_name):
        print("=======Create folder=======")
        crawl = base(False)
        try:
            crawl.create_folder(folder_name)
            print("=======Created folder successfully======")
        except Exception as e:
            print(f"Error creating folder: {e}")
        
        chap = 1

        # Use requests/BeautifulSoup for initial page to get chapter links
        
        while (chap < 68):
            main_page_url = f"https://truyenfull.vision/sau-khi-hon-nhan-tan-vo/chuong-{chap}/"
            print(f"Crawling chap: {main_page_url}")
        
            try:
                crawl.go_to_webpage(main_page_url)
                crawl.wait_for_element_visible(sau_khi_hon_nhan_tan_vo.chap_title, 10)
                crawl.wait_for_element_visible(sau_khi_hon_nhan_tan_vo.chap_content, 10)

                title = crawl.get_element_text(sau_khi_hon_nhan_tan_vo.chap_title)
                content = crawl.get_element_text(sau_khi_hon_nhan_tan_vo.chap_content)
                crawl.add_text_to_doc_file(title, content, "chapter_" + str(chap))
                chap += 1
                    
            except Exception as e:
                raise Exception(f"Error: {e}")
        crawl.quit_driver()

if __name__ == '__main__':
    main("sau_khi_hon_nhan_tan_vo")
