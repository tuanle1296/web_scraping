from src.base_functions import *
from src.locators import co_truong_cat_canh_di
import requests


def main(folder_name):
        print("=======Create folder=======")
        crawl = base()
        try:
            crawl.create_folder(folder_name)
            print("=======Created folder successfully======")
        except Exception as e:
            print(f"Error creating folder: {e}")
        # locators = co_truong_cat_canh_di()

        # Use requests/BeautifulSoup for initial page to get chapter links
        main_page_url = "https://mybothomngon.wordpress.com/2018/11/12/co-truong-cat-canh-di/"
        
        crawl.go_to_webpage(main_page_url)
        # crawl.wait_for_element_visible(co_truong_cat_canh_di.chapter_blocks, timeout=30)
        # Initialize chap_urls outside the if block
        chap_urls = []
        duong_vien_div = crawl.find_element(co_truong_cat_canh_di.chapter_blocks)
        if duong_vien_div:
            print(f"=========Fetching chapter list from {main_page_url}==========")
            a_tags = crawl.find_elements(co_truong_cat_canh_di.a_tag, duong_vien_div)
            for a_tag in a_tags:
                url = crawl.get_element_attribute(a_tag, 'href')
                chap_urls.append(url)
                print(url)
        else:
            print(f"Error: there is no element found with locator {co_truong_cat_canh_di.chapter_blocks}")

        for chap_url in chap_urls:
            print(f"Crawling chap: {chap_url}")
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }

            print(f"Downloading {chap_url}...")
            try:
                response = requests.get(chap_url, headers=headers)
                response.encoding = 'utf-8' # Force Vietnamese encoding

                soup = BeautifulSoup(response.text, 'html.parser')

                title_element = crawl.get_element_by_tag(soup, *co_truong_cat_canh_di.title)
                content_element = crawl.get_element_by_tag(soup, *co_truong_cat_canh_di.content)
 # Save to .docx file using the method from the base class, which handles saving to the correct folder.
                crawl.save_doc(title_element, content_element)
                    
            except Exception as e:
                raise Exception(f"Error: {e}")
        crawl.quit_driver()

if __name__ == '__main__':
    main("co_truong_cat_canh_di")
