import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.locators import tulip_trong_gio


def main(folder_name):
        print("=======Create folder=======")
        crawl = base(False)
        try:
            crawl.create_folder(folder_name)
            print("=======Created folder successfully======")
        except Exception as e:
            print(f"Error creating folder: {e}")

        # Use requests/BeautifulSoup for initial page to get chapter links
        main_page_url = "https://mybothomngon.wordpress.com/2021/11/21/tulip-trong-gio-dai-duong-chieu-nghi/"
        
        crawl.go_to_webpage(main_page_url)
        # Initialize chap_urls outside the if block
        chap_urls = []
        xpath_A_str = tulip_trong_gio.beginning_chapter_block[1]
        xpath_B_str = tulip_trong_gio.endding_chapter_block[1]

        locators_between = (
            f"{xpath_A_str}"                 # The Start Node
            "/following-sibling::*"                        # Look at siblings after it
            "["                                            # Condition start:
            f"following-sibling::{xpath_B_str}" # Must have the 'End' node after it
            "]"
        )

        chapter_urls_ = crawl.find_elements((By.XPATH, locators_between))

        for chap_url_ in chapter_urls_:
            a_tags = crawl.find_elements(tulip_trong_gio.a_tag, chap_url_)
            for a_tag in a_tags:
                url = crawl.get_attribute_from_element(a_tag, 'href')
                chap_urls.append(url)
                print(url)
       

        index = 0
        for chap_ in chap_urls:
            print(f"Crawling chap: {chap_}")

            print(f"Downloading {chap_}...")
            try:
                crawl.go_to_webpage(chap_)
                if (crawl.wait_for_element_visible((tulip_trong_gio.pass_word_input_field), 5)):
                    crawl.input_text(tulip_trong_gio.pass_word_input_field, "LuHydeNgoDan")
                    crawl.click_element(tulip_trong_gio.password_submit_button)

                title = crawl.get_element_text(tulip_trong_gio.title)
                content = crawl.get_element_text(tulip_trong_gio.content)
                crawl.add_text_to_doc_file(title, content, "chapter_" + str(index))
                print(index)
                index += 1
                    
            except Exception as e:
                raise Exception(f"Error: {e}")
        crawl.quit_driver()

if __name__ == '__main__':
    main("tulip_trong_gio")
