import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.locators import cung_anh_di_den_tan_cung_the_gioi


def main(folder_name):
        print("=======Create folder=======")
        crawl = base(False)
        try:
            crawl.create_folder(folder_name)
            print(f"=======Created folder {folder_name} successfully======")
        except Exception as e:
            print(f"Error creating folder: {e}")

        # Use requests/BeautifulSoup for initial page to get chapter links
        main_page_url = "https://ebookvie.com/doc-sach/cung-anh-di-den-tan-cung-the-gioi/"
        
        crawl.go_to_webpage(main_page_url)
        # The story will start from ref=2
        # Click next until ref=2
        # Last chapter will be ref=67
        # Each chapter_content will be inside iframe
        # Next button will be outside iframe
        # get current ref
        # ref of the 1st page should be = 0
        current_ref = 0
        old_text = ""
        while(current_ref < 68):
            current_ref = int(crawl.get_attribute_from_element(cung_anh_di_den_tan_cung_the_gioi.chapter_recognization, "ref"))
            
            crawl.click_element(cung_anh_di_den_tan_cung_the_gioi.next_button)
            crawl.sleep(1)
            if(crawl.wait_for_page_load(10)):
                iframe = crawl.wait_for_element_visible(cung_anh_di_den_tan_cung_the_gioi.iframe, 10)
                crawl.switch_frame(iframe)
                if (crawl.wait_for_element_visible(cung_anh_di_den_tan_cung_the_gioi.story_content, 15)):
                    element = crawl.find_element(cung_anh_di_den_tan_cung_the_gioi.story_content)
                    new_text = crawl.get_element_text(element)
                    if (new_text != old_text):
                        print(f"Current chapter: {current_ref}")
                        crawl.add_text_to_doc_file(str(current_ref), new_text, str(current_ref))
                        old_text = new_text

                    if (current_ref == 67):
                        if (new_text == old_text):
                            break

            else:
                 raise Exception("An error occurred while waiting for the page to load.")

            crawl.switch_back_to_default()
        
        crawl.quit_driver()

if __name__ == '__main__':
    main("cung_anh_di_den_tan_cung_the_gioi")
