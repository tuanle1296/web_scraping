import threading
import time
from src.base_functions import *
from selenium.webdriver.common.by import By


next_btn = (By.XPATH, "//a[@rel='next']")
# next_btn_2 = (By.XPATH, "//a[contains(text(), 'CHƯƠNG ')]")
cur_title = 'entry-title'
cur_content = 'entry-content'
is_content_img = (By.XPATH, "//div[@class='entry-content']//img")


'''============Multi thread=========='''
# def crawl_data(folder_name):
#     print("=======Create folder " + folder_name + " =======")
#     time.sleep(2)
#     crawl = base()
#     crawl.create_folder(folder_name)
#     print("=======Created folder " + folder_name + " successfully======")
#
#
# def main():
#     threads = []
#     comic_name = ["Quan nhan trong khoi lua", "OnePiece", "One Punch Man"]
#     for i in range(len(comic_name)):
#         process = threading.Thread(target=crawl_data, args=(comic_name[i],))
#         process.start()
#         threads.append(process)
#
#     for process in threads:
#         process.join()

'''==========================='''


def main():
    print("=======Create folder=======")
    crawl = base()
    crawl.create_folder("Quan nhan trong khoi lua")
    print("=======Created folder successfully======")
    print("=======Start crawling=======")
    chap_url = "https://xiaoyang0811.wordpress.com/2019/06/09/chuong-67/"
    flag = "false"
    new_title = "test"
    while flag == "false":
        crawl.open_chrome_in_headless_mode(chap_url)
        time.sleep(5)
        url = crawl.get_current_url()
        soup = crawl.crawl_data(url)
        chap_title = crawl.get_title_by_class(soup, cur_title)
        chap_content = crawl.get_body_by_class(soup, cur_content)
        img_name = crawl.define_img_name(chap_title.text)
        try:
            crawl.wait_until_page_contains(is_content_img)
            if chap_content.get_text() == "":
                crawl.reload_current_page()
            time.sleep(5)
            crawl.capture_screen(img_name)
        except:
            crawl.save_doc(chap_title, chap_content)
        if new_title == chap_title.text:
            flag = "true"
        time.sleep(1)
        print(str(chap_title.text))
        try:
            chap_url = crawl.get_attribute_from_tag(next_btn, 'href')
            time.sleep(5)
            print(crawl.get_current_url())
        except:
            flag = "true"
        # crawl.close_browser()
    crawl.quit_driver()
    print("=======FINISHED=======")


if __name__ == main():
    main()
