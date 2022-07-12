import sys
from src.base_functions import *
from src.locators import kethonsailam
import threading

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

'''Will implement in the future to make code shorter'''

chap_url_1_to_31 = "https://aishihouse.wordpress.com/2011/11/24/ket-hon-sai-lam-chuong-1/"
chap_url_32_to_57 = "https://trahoaquan20.wordpress.com/2020/03/07/chuong-32-lau-bui-chuyen-xua/"
chap_url_ngoai_truyen_1 = "https://trahoaquan20.wordpress.com/2020/05/29/nt1-nhat-ky-nghich-ngom-dang-yeu-cua-au-tieu-vu/"
chap_url_ngoai_truyen_2 = "https://trahoaquan20.wordpress.com/2020/05/29/ngoai-truyen-2-hai-nguoi-qua-duong-a-va-b/"
chap_url_ngoai_truyen_3 = "https://trahoaquan20.wordpress.com/2020/05/29/nt3-neu-nhu-tinh-yeu-co-the-quay-lai-tu-dau/"


def crawl_from_chap_1_to_31(folder_name):
    print("=======Create folder=======")
    crawl_1 = base()
    try:
        crawl_1.create_folder(folder_name)
        print("=======Created folder successfully======")
    except Exception as e:
        print(e)
    locators_1 = kethonsailam()
    print("=======Start crawling from chap 1 to 31=======")
    crawl_1.go_to_webpage(chap_url_1_to_31)
    for i in range(0, 32):
        try:
            crawl_1.click_element(locators_1.close_cookies_banner)
        except:
            pass
        url = crawl_1.get_current_url()
        soup = crawl_1.crawl_data(url)
        chap_title = crawl_1.get_title_by_class(soup, locators_1.title_from_chap_1_to_31)
        chap_content = crawl_1.get_body_by_class(soup, locators_1.content_from_chap_1_to_31)
        crawl_1.save_doc(chap_title, chap_content)
        print("url from chap: " + str(chap_title.text) + str(url))
        crawl_1.click_element(locators_1.next_from_1_to_31)
        time.sleep(1)

    crawl_1.quit_driver()
    print("======FINISHED from chap 1 to 31=======")


def crawl_from_chap_32_to_57(folder_name):
    print("=======Create folder=======")
    crawl_2 = base()
    try:
        crawl_2.create_folder(folder_name)
        print("=======Created folder successfully======")
    except Exception as e:
        print(e)
    locators_2 = kethonsailam()
    print("=======Start crawling from chap 32 to 57=======")
    crawl_2.go_to_webpage(chap_url_32_to_57)
    for i in range(31, 58):
        try:
            crawl_2.click_element(locators_2.close_cookies_banner)
        except:
            pass
        url = crawl_2.get_current_url()
        soup = crawl_2.crawl_data(url)
        chap_title = crawl_2.get_title_by_class(soup, locators_2.title_from_chap_32_to_57)
        chap_content = crawl_2.get_body_by_class(soup, locators_2.content_from_chap_32_to_57)
        crawl_2.save_doc(chap_title, chap_content)
        print("url from chap: " + str(chap_title.text) + str(url))
        crawl_2.click_element(locators_2.next_from_32_to_57)
        time.sleep(1)

    crawl_2.quit_driver()
    print("======FINISHED from chap 32 to 57=======")


def crawl_ngoai_truyen_1(folder_name, password):
    print("=======Create folder=======")
    crawl_3 = base()
    try:
        crawl_3.create_folder(folder_name)
        print("=======Created folder successfully======")
    except Exception as e:
        print(e)
    locators_3 = kethonsailam()
    print("=======Start crawling from ngoai truyen 1=======")
    crawl_3.go_to_webpage(chap_url_ngoai_truyen_1)
    crawl_3.click_element(locators_3.close_cookies_banner)
    crawl_3.input_text(locators_3.password_field, password)
    crawl_3.click_element(locators_3.submit_password_btn)
    time.sleep(5)
    page = crawl_3.get_page_source()
    crawl_3.pass_data_to_file(page, "testdata")
    with open("testdata.html", 'r') as file:
        beautifulSoupText = BeautifulSoup(file.read(), 'html.parser')
        chap_title = crawl_3.get_title_by_class(beautifulSoupText, locators_3.title_from_chap_32_to_57)
        chap_content = crawl_3.get_body_by_class(beautifulSoupText, locators_3.content_from_chap_32_to_57)
        crawl_3.save_doc(chap_title, chap_content)
    print("===========FINISHED ngoai truyen 1=============")
    crawl_3.quit_driver()
    crawl_3.remove_file_if_exists("testdata.html")


def crawl_ngoai_truyen_2(folder_name, password):
    print("=======Create folder=======")
    crawl_4 = base()
    try:
        crawl_4.create_folder(folder_name)
        print("=======Created folder successfully======")
    except Exception as e:
        print(e)
    locators_4 = kethonsailam()
    print("=======Start crawling from ngoai truyen 2=======")
    crawl_4.go_to_webpage(chap_url_ngoai_truyen_2)
    crawl_4.click_element(locators_4.close_cookies_banner)
    crawl_4.input_text(locators_4.password_field, password)
    crawl_4.click_element(locators_4.submit_password_btn)
    time.sleep(5)
    page = crawl_4.get_page_source()
    crawl_4.pass_data_to_file(page, "testdata2")
    with open("testdata2.html", 'r') as file:
        beautifulSoupText = BeautifulSoup(file.read(), 'html.parser')
        chap_title = crawl_4.get_title_by_class(beautifulSoupText, locators_4.title_from_chap_32_to_57)
        chap_content = crawl_4.get_body_by_class(beautifulSoupText, locators_4.content_from_chap_32_to_57)
        crawl_4.save_doc(chap_title, chap_content)
    print("===========FINISHED ngoai truyen 2==========")
    crawl_4.quit_driver()
    crawl_4.remove_file_if_exists("testdata2.html")


def crawl_ngoai_truyen_3(folder_name, password):
    print("=======Create folder=======")
    crawl_5 = base()
    try:
        crawl_5.create_folder(folder_name)
        print("=======Created folder successfully======")
    except Exception as e:
        print(e)
    locators_5 = kethonsailam()
    print("=======Start crawling from ngoai truyen 3=======")
    crawl_5.go_to_webpage(chap_url_ngoai_truyen_3)
    crawl_5.click_element(locators_5.close_cookies_banner)
    crawl_5.input_text(locators_5.password_field, password)
    crawl_5.click_element(locators_5.submit_password_btn)
    time.sleep(5)
    page = crawl_5.get_page_source()
    crawl_5.pass_data_to_file(page, "testdata3")
    with open("testdata3.html", 'r') as file:
        beautifulSoupText = BeautifulSoup(file.read(), 'html.parser')
        chap_title = crawl_5.get_title_by_class(beautifulSoupText, locators_5.title_from_chap_32_to_57)
        chap_content = crawl_5.get_body_by_class(beautifulSoupText, locators_5.content_from_chap_32_to_57)
        crawl_5.save_doc(chap_title, chap_content)
    print("========FINISHED ngoai truyen 3==========")
    crawl_5.quit_driver()
    crawl_5.remove_file_if_exists("testdata3.html")


if __name__ == '__main__':
    v = kethonsailam()
    process_1 = threading.Thread(target=crawl_ngoai_truyen_1, args=("Ket hon sai lam", v.password_nt_1_2))
    process_2 = threading.Thread(target=crawl_ngoai_truyen_2, args=("Ket hon sai lam", v.password_nt_1_2))
    process_3 = threading.Thread(target=crawl_ngoai_truyen_3, args=("Ket hon sai lam", v.password_nt_3))
    process_4 = threading.Thread(target=crawl_from_chap_1_to_31, args=("Ket hon sai lam",))
    process_5 = threading.Thread(target=crawl_from_chap_32_to_57, args=("Ket hon sai lam",))
    process_1.start()
    process_2.start()
    process_3.start()
    process_4.start()
    process_5.start()
    process_1.join()
    process_2.join()
    process_3.join()
    process_4.join()
    process_5.join()
    sys.exit()

'''Note: run this code using cmd: python3 -m test.ket_hon_sai_lam'''