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
        # crawl.wait_for_element_visible(co_truong_cat_canh_di.chapter_blocks, timeout=30)
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
        # if chapter_urls_:
        #     print(f"=========Fetching chapter list from {main_page_url}==========")
        for chap_url_ in chapter_urls_:
            # chap_url = crawl.find_element(chap_url_)
            a_tags = crawl.find_elements(tulip_trong_gio.a_tag, chap_url_)
            for a_tag in a_tags:
                url = crawl.get_element_attribute(a_tag, 'href')
                chap_urls.append(url)
                print(url)
        # else:
        #     print(f"Error: there is no element found with locator {locators_between}")

        for chap_ in chap_urls:
            print(f"Crawling chap: {chap_}")
            # headers = {
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            # }

            print(f"Downloading {chap_}...")
            try:
                crawl.go_to_webpage(chap_)

                # response = requests.get(chap_url, headers=headers)
                # response.encoding = 'utf-8' # Force Vietnamese encoding

                # soup = BeautifulSoup(response.text, 'html.parser')
                if (crawl.wait_for_element_visible_and_return_true_false((tulip_trong_gio.pass_word_input_field), 1)):
                    crawl.input_text(tulip_trong_gio.pass_word_input_field, "LuHydeNgoDan")
                    crawl.click_element(tulip_trong_gio.password_submit_button)

                title_element = crawl.find_element_by_tuple(tulip_trong_gio.title)
                content_element = crawl.find_element_by_tuple(tulip_trong_gio.content)

                title = crawl.get_element_text(title_element)
                content = crawl.get_element_text(content_element)
                crawl.add_text_to_doc_file(title, content)
                    
            except Exception as e:
                raise Exception(f"Error: {e}")
        crawl.quit_driver()

if __name__ == '__main__':
    main("tulip_trong_gio")
