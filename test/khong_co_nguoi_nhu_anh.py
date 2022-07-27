from src.base_functions import *
from src.locators import kcnna

url = "https://mmtd1314.wordpress.com/2021/06/21/khong-co-nguoi-nhu-anh-tue-kien/?fbclid=IwAR1_Ehlw5qffeAiUx3xl8jgxu15roAFwtWxRXDC6lIikulK2jJEyPamD7uk"


def crawl_truyen(folder_name):
    print("=======Create folder=======")
    crawl = base()
    try:
        crawl.create_folder(folder_name)
        print("=======Created folder successfully======")
    except Exception as e:
        print(e)
    locators = kcnna
    crawl.go_to_webpage(url)
    print("=========Start crawling==========")
    chap_url = crawl.get_attribute_from_all_elements(locators.chap_locators, "href")
    for item in chap_url:
        crawl.go_to_webpage(item)
        check = crawl.verify_element(locators.password_field)
        if check is True:
            crawl.input_text(locators.password_field ,locators.password_1)
            crawl.click_element(locators.submit_pass_btn)
            re_check = crawl.verify_element(locators.password_field)
            if re_check is True:
                crawl.input_text(locators.password_field, locators.password_2)
                crawl.click_element(locators.submit_pass_btn)
                time.sleep(2)
        page = crawl.get_page_source()
        crawl.pass_data_to_file(page, "datafile.html")
        with open("datafile.html", 'r') as file:
            beautifulSoupText = BeautifulSoup(file.read(), 'html.parser')
            chap_title = crawl.get_title_by_class(beautifulSoupText, locators.chap_title)
            chap_content = crawl.get_body_by_class(beautifulSoupText, locators.chap_content)
            crawl.save_doc(chap_title, chap_content)
        print("Chap title: ", str(chap_title.text).strip())
    crawl.remove_file_if_exists("datafile.html")
    print("=====FINISHED=====")
    crawl.quit_driver()


    
    

if __name__ == '__main__':
    crawl_truyen("Khong co nguoi nhu anh")

    
'''Note: run this code using cmd: python3 -m test.khong_co_nguoi_nhu_anh'''