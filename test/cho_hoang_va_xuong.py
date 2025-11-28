from src.base_functions import *
from src.locators import cho_hoang_va_xuong
from dataclasses import dataclass


'''==========================='''

'''Will implement in the future to make code shorter'''

@dataclass()
class Data:
    chap_1_url : str = "https://aztruyen.com/chapter/edit-cho-hoang-va-xuong-huu-do-thanh-chuong-1-xuong-1276895520.html"
    test_text : str = "test"
    href_attribute : str = "href"
    story_name : str = "cho_hoang_va_xuong"
    hashtag_icon : str = "#"

data = Data()

def start_crawl(folder_name):
    print("=======Create folder=======")
    crawl = base(False)
    try:
        crawl.create_folder(folder_name)
        print("=======Created folder successfully======")
    except Exception as e:
        print(e)
    locators = cho_hoang_va_xuong()
    print("=======Start crawling=======")
    crawl.go_to_webpage(data.chap_1_url)
    chap_url = data.test_text

    while (chap_url != data.hashtag_icon):
        try:
            crawl.switch_frame()
            crawl.wait_until_page_contains(locators.close_ads_btn)
            crawl.click_element(locators.close_ads_btn)
            crawl.switch_back_to_default()
        except:
            pass
        url = crawl.get_current_url()
        soup = crawl.crawl_data(url)
        chap_title = crawl.get_element_by_class(soup, locators.title)
        chap_content = crawl.get_element_by_class(soup, locators.content)
        print("url from chap: " + str(chap_title.text) + " " + str(url))
        crawl.save_doc(chap_title, chap_content)

        chap_url = crawl.get_attribute_from_element(locators.next_chap, data.href_attribute)
        try:
            crawl.go_to_webpage(chap_url)
        except:
            pass
    print("======FINISHED=======")
    crawl.quit_driver()


if __name__ == '__main__':
    start_crawl(data.story_name)


'''Note: run this code using cmd: python3 -m test.cho_hoang_va_xuong'''