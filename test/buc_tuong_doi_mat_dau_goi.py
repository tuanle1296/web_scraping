import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.locators import buc_tuong_doi_mat_dau_goi as lo


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

        chapters_list = crawl.get_attribute_from_all_elements(urls_list, "href")

        password_1 = "GIUGINVESINHTHATTOT"
        password_2 = "01072021"
        chap = 1
        for chap_url in chapters_list:
            crawl.go_to_webpage(chap_url)
            is_loaded = crawl.wait_for_page_load(5)
            if (is_loaded is True):
                is_password_visible = crawl.is_element_visible(lo.password_field)

                if (is_password_visible is True):
                    crawl.input_text(lo.password_field, password_1)
                    crawl.click_element(lo.submit_password_btn)
                    crawl.sleep(5)
                    crawl.wait_for_page_load(10)
                    is_visible = crawl.is_element_visible(lo.invalid_password_message)

                    if (is_visible is True):
                        crawl.input_text(lo.password_field, password_2)
                        crawl.click_element(lo.submit_password_btn)
                        crawl.sleep(5)
                        crawl.wait_for_page_load(10)
                else:
                    print("No password required.")
                    
                print(f"Crawling: {chap_url}")
                title = crawl.get_element_text(lo.chap_title)
                content = crawl.get_element_text(lo.chap_content)
                
                crawl.add_text_to_doc_file(title, content, "chapter_" + str(chap))
                chap += 1

        crawl.quit_driver()

if __name__ == '__main__':
    main("buc_tuong_doi_mat_dau_goi")
