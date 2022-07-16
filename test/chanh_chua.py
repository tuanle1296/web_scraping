from src.base_functions import *
from src.locators import onlytlinh

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
chap_url = "https://onlytlinh.wordpress.com/2021/08/20/chanh-chua-thap-tra/?fbclid=IwAR2_iBV6O2J3989Ci9wd0LxlJyiDt" \
           "r7IKuFGTujnjP9RhTtOXxiH1Z5s1-4 "


def main(folder_name):
    global chap_url
    print("=======Create folder=======")
    crawl = base(False)
    locators = onlytlinh()
    try:
        crawl.create_folder(folder_name)
        print("=======Created folder successfully======")
    except Exception as e:
        print(e)
    print("=======Start crawling=======")
    flag = "false"
    crawl.go_to_webpage(chap_url)
    i = 0
    chuong_ngoai = 1
    while flag == "false":
        try:
            crawl.click_element(locators.accept_cookies_btn)
        except:
            pass
        if i >= 1:
            if i <= 20 or 26 <= i <= 36:
                url = crawl.get_current_url()
                print(url)
                soup = crawl.crawl_data(url)
                chap_title = crawl.get_title_by_class(soup, locators.cur_title)
                chap_content = crawl.get_body_by_class(soup, locators.cur_content)
                crawl.save_doc(chap_title, chap_content)
            if 21 <= i <= 25:
                try:
                    crawl.input_text(locators.pass_input_field, locators.pass_1)
                    time.sleep(2)
                    crawl.press_Enter(locators.pass_input_field)
                    time.sleep(5)
                except:
                    pass
            if 37 <= i <= 73:
                try:
                    crawl.input_text(locators.pass_input_field, locators.pass_2)
                    time.sleep(2)
                    crawl.press_Enter(locators.pass_input_field)
                    time.sleep(5)
                except:
                    pass
            if 74 <= i <= 85:
                try:
                    crawl.input_text(locators.pass_input_field, locators.pass_3)
                    time.sleep(2)
                    crawl.press_Enter(locators.pass_input_field)
                    time.sleep(5)
                except:
                    pass

            if 21 <= i <= 25 or 37 <= i <= 85:
                page = crawl.get_page_source()
                crawl.pass_data_to_file(page, "testdata.html")
                with open("testdata.html", 'r') as file:
                    beautifulSoupText = BeautifulSoup(file.read(), 'html.parser')
                    chap_title = crawl.get_title_by_class(beautifulSoupText, locators.cur_title)
                    chap_content = crawl.get_body_by_class(beautifulSoupText, locators.cur_content)
                    crawl.save_doc(chap_title, chap_content)
            # else:
            #     soup = crawl.crawl_data(url)
            #     chap_title = crawl.get_title_by_class(soup, locators.cur_title)
            #     chap_content = crawl.get_body_by_class(soup, locators.cur_content)
                # img_name = crawl.define_img_name(chap_title.text)
                # try:
                #     crawl.wait_until_page_contains(xiao_link.is_content_img)
                #     if chap_content.get_text() == "":
                #         crawl.reload_current_page()
                #     crawl.capture_screen(img_name)
                # except:
                #     crawl.save_doc(chap_title, chap_content)
                # crawl.save_doc(chap_title, chap_content)
                # print(str(chap_title.text))
            print(str(chap_title.text))
            crawl.switch_tab(0)
        i = i + 1
        if 1 <= i <= 73:
            next = locators.next_chap
            next = crawl.replace_text(next, "INPUT", str(i))
            chap_url = crawl.get_attribute_from_tag((By.XPATH, next), 'href')
        if 74 <= i <= 85:
            next = locators.next_chap_ngoai
            if 1 <= chuong_ngoai < 10:
                next = crawl.replace_text(next, "INPUT", "0" + str(chuong_ngoai))
                chap_url = crawl.get_attribute_from_tag((By.XPATH, next), 'href')
            else:
                next = crawl.replace_text(next, "INPUT", str(chuong_ngoai))
                chap_url = crawl.get_attribute_from_tag((By.XPATH, next), 'href')
            chuong_ngoai = chuong_ngoai + 1
            if chuong_ngoai > 12:
                flag = "true"
        try:
            crawl.open_new_tab(chap_url)
            crawl.switch_tab(1)
        except:
            flag = "true"
    print("=======FINISHED=======")
    crawl.quit_driver()
    

if __name__ == '__main__':
    f = base()
    try:
        main(folder_name="Chanh chua")
    except KeyboardInterrupt:
        print("=======ENDED BY INTERRUPTING=======")
        f.quit_driver()

'''Note: run this code using cmd: python3 -m test.chanh_chua'''