from concurrent.futures import thread
import threading
from src.base_functions import *
from src.locators import chi_yeu_minh_anh


url_1 = "https://nhuoclinh.wordpress.com/truyen-dai/hi%e1%bb%87n-d%e1%ba%a1i/du-an-chi-yeu-minh-anh/?fbclid=IwAR299zfBfrFHwnhVyx_x45uzH4G64mSFSv9vnaAtporVkQjIQPaxh55dHFk"
url_2 = "https://chihoavancac.wordpress.com/home/truyen-trong-nha/on-going/hien-dai-chi-yeu-minh-anh-na-khau-trung/?fbclid=IwAR21Zg3-f2SmS0r9T0lgJCe30EMcrpEr8t5T6gdFs-xAH3sOIrRAb2RkPxE"


def main(folder_name, url, chap_locator):
    print("=======Create folder=======")
    crawl = base()
    try:
        crawl.create_folder(folder_name)
        print("=======Created folder successfully======")
    except Exception as e:
        print(e)
    locators = chi_yeu_minh_anh
    crawl.go_to_webpage(url)
    print("=========Start crawling==========")
    chap_url = crawl.get_attribute_from_all_elements(chap_locator, "href")
    for item in chap_url:
        crawl.go_to_webpage(item)
        soup = crawl.crawl_data(item)
        chap_title = crawl.get_title_by_class(soup, locators.title)
        chap_content = crawl.get_body_by_class(soup, locators.content)
        print(chap_title.text)
        is_content = crawl.wait_until_page_contains(locators.is_content_img, 2)
        print("is content image: ", is_content)
        if is_content is True:
            img_name = crawl.define_img_name(chap_title.text)
            crawl.capture_screen(img_name)
        else:
            crawl.save_doc(chap_title, chap_content)
    print("=====FINISHED=====")
    crawl.quit_driver()
        

def main_2(folder_name, url):
    print("=======Create folder=======")
    crawl = base()
    try:
        crawl.create_folder(folder_name)
        print("=======Created folder successfully======")
    except Exception as e:
        print(e)
    locators = chi_yeu_minh_anh
    crawl.go_to_webpage(url)
    print("=========Start crawling==========")
    chap_list = []
    for ii in range(19, 64):
        cur_chap = crawl.replace_text(locators.chap_19_to_63, "INPUT", str(ii))
        cur_chap_temp = crawl.replace_text(locators.chap_, "INPUT", str(ii))
        try:
            chap_url = crawl.get_attribute_from_element((By.XPATH, cur_chap), "href")
        except:
            chap_url = crawl.get_attribute_from_element((By.XPATH, cur_chap_temp), "href")
        chap_list.append(chap_url)
    for i in range(len(chap_list)):
        print(chap_list[i])
        if "facebook" in chap_list[i]:
            print("Skip")
        crawl.go_to_webpage(chap_list[i])

        soup = crawl.crawl_data(chap_list[i])
        try:
            chap_title = crawl.get_title_by_class(soup, locators.title)
            chap_content = crawl.get_body_by_class(soup, locators.content)
            print(chap_title.text)
            is_content = crawl.wait_until_page_contains(locators.is_content_img, 2)
            print("is content image: ", is_content)
            if is_content is True:
                img_name = crawl.define_img_name(chap_title.text)
                crawl.capture_screen(img_name)
            else:
                crawl.save_doc(chap_title, chap_content)
        except:
            pass
    print("=====FINISHED=====")
    crawl.quit_driver()


if __name__ == '__main__':
    lo = chi_yeu_minh_anh
    c = base
    threads = []
    chap_1_to_18 = [lo.chap_1_2, lo.chap_3_to_6, lo.chap_7_to_11, lo.chap_12_to_14, lo.chap_15_16, lo.chap_17_18]
    
        

    for i in range(len(chap_1_to_18)):
        process = threading.Thread(target=main, args=("Chi yeu minh anh", url_1, chap_1_to_18[i]))
        process.start()
        threads.append(process)
    process = threading.Thread(target=main, args=("Chi yeu minh anh", url_1, lo.chap_gioi_thieu))
    process.start()
    threads.append(process)
    process = threading.Thread(target=main_2, args=("Chi yeu minh anh", url_2))
    process.start()
    threads.append(process)

    for process in threads:
        process.join()



'''Note: run this code using cmd: python3 -m test.chi_yeu_minh_anh'''