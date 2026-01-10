from src.base_functions import *
from src.locators import khi_gio_noi_len

main_url = "https://phongphongtam2.com/2025/01/25/khi-gio-noi-len-mong-tieu-nhi/"


def main(folder_name):
    global main_url
    crawl = base(False)
    locators = khi_gio_noi_len()

    print("=======Go to main webpage=======")
    crawl.go_to_webpage(main_url)
    if not crawl.wait_for_page_load(timeout=20):
        print("Page did not finish loading in 20s — handle fallback or retry")
    elements = crawl.find_elements(locators.list_chap)

    print("=======Get all chapter links=======")
    hrefs = []
    for el in elements[1:]:
        anchors = crawl.find_elements(locators.chap_tag, parent_element=el)
        for a in anchors:
            href = crawl.get_element_attribute(a, 'href')
            hrefs.append(href)
    
    hrefs = list(dict.fromkeys(hrefs))
    print(f"Total chapters found: {len(hrefs)}")

    print("=======Create folder=======")
    try:
        crawl.create_folder(folder_name)
        print("=======Created folder successfully======")
    except Exception as e:
        print(e)
    print("=======Start crawling=======")
    for href in hrefs:
        print(f"Crawling chap: {href}")

        crawl.go_to_webpage(href)
        
        if not crawl.wait_for_page_load(timeout=20):
            print("Page did not finish loading in 20s — handle fallback or retry")
        soup = crawl.crawl_data(href)
        chap_title = crawl.get_element_by_class(soup, locators.header)
        chap_content = crawl.get_element_by_class(soup, locators.content)
        crawl.save_doc(chap_title, chap_content)
    
    print("=======FINISHED=======")
    crawl.quit_driver()
    

if __name__ == '__main__':
    f = base()
    try:
        main(folder_name="Khi gio noi len")
    except KeyboardInterrupt:
        print("=======ENDED BY INTERRUPTING=======")
        f.quit_driver()

'''Note: run this code using cmd: python3 test/khi_gio_noi_len.py'''