from src.base_functions import *
from src.locators import cho_hoang_va_xuong


'''==========================='''

'''Will implement in the future to make code shorter'''

chap_1_url = "https://aztruyen.com/chapter/edit-cho-hoang-va-xuong-huu-do-thanh-chuong-1-xuong-1276895520.html"


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
    crawl.go_to_webpage(chap_1_url)
    chap_url = "test"

    while (chap_url != "#"):
        try:
            crawl.switch_frame()
            crawl.wait_until_page_contains(locators.close_ads_btn)
            crawl.click_element(locators.close_ads_btn)
            crawl.switch_back_to_default()
        except:
            pass
        url = crawl.get_current_url()
        soup = crawl.crawl_data(url)
        chap_title = crawl.get_title_by_class(soup, locators.title)
        chap_content = crawl.get_body_by_class(soup, locators.content)
        print("url from chap: " + str(chap_title.text) + " " + str(url))
        crawl.save_doc(chap_title, chap_content)

        chap_url = crawl.get_attribute_from_element(locators.next_chap, 'href')
        try:
            crawl.go_to_webpage(chap_url)
        except:
            pass
    print("======FINISHED=======")
    crawl.quit_driver()


if __name__ == '__main__':
    start_crawl("cho_hoang_va_xuong")


'''Note: run this code using cmd: python3 -m test.cho_hoang_va_xuong'''