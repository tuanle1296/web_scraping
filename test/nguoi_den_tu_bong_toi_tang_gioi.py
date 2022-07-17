from src.base_functions import *
from src.locators import nguoi_den_tu_bong_toi_tang_gioi


url = "https://fjveel.wordpress.com/nguoi-den-tu-bong-toi-tang-gioi/?fbclid=IwAR0DY8p4N4XPOQcKAfMQerTuvnXahpHHSj3TsrvnOQ-RKnt3rob9hE4lBFg"

def main(folder_name):
    print("=======Create folder=======")
    crawl = base()
    try:
        crawl.create_folder(folder_name)
        print("=======Created folder successfully======")
    except Exception as e:
        print(e)
    locators = nguoi_den_tu_bong_toi_tang_gioi
    crawl.go_to_webpage(url)
    crawl.click_element(locators.accept_cookies_btn)
    print("=========Start crawling==========")
    chap_url = crawl.get_attribute_from_all_elements(locators.chap_url_list, "href")
    for item in chap_url:
        crawl.go_to_webpage(item)
        soup = crawl.crawl_data(item)
        chap_title = crawl.get_title_by_class(soup, locators.cur_title)
        chap_content = crawl.get_body_by_class(soup, locators.cur_content)
        print(chap_title.text)
        is_content = crawl.wait_until_page_contains(locators.is_content_img)
        print("is content image: ", is_content)
        if is_content is True:
            img_name = crawl.define_img_name(chap_title.text)
            crawl.scroll_web_page_to_the_end()
            time.sleep(5)
            crawl.capture_screen(img_name)
        else:
            crawl.save_doc(chap_title, chap_content)
    print("=====FINISHED=====")
    crawl.quit_driver()
        


if __name__ == '__main__':
    main("Nguoi den tu bong toi tang gioi")



'''Note: run this code using cmd: python3 -m test.nguoi_den_tu_bong_toi_tang_gioi'''