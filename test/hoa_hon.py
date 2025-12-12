from dataclasses import dataclass
from src.base_functions import *
from src.locators import hoa_hon

@dataclass
class PreData:
    main_web_page : str = "https://www.wattpad.com/story/278567194-ho%C3%A0n-h%E1%BB%8Fa-h%C3%B4n-tang-gi%E1%BB%9Bi"
    href_attribute : str = "href"

pre_data = PreData()
def crawl_chap_1_test():

    crawl_1 = base()

    print("========Go to webpage=========")
    crawl_1.go_to_webpage(pre_data.main_web_page)

    print("=======Create folder=======")
    crawl_1.create_folder("Hoa hon")
    locators_1 = hoa_hon()

    print("==========Get all chapter link===========")

    chapter_list = crawl_1.find_element(locators_1.story_parts)
    all_links = crawl_1.find_elements(locators_1.all_links, chapter_list)
    chap_urls = []
    for link in all_links:
        chapter_link = link.get_attribute(pre_data.href_attribute)
        chap_urls.append(chapter_link)

    print("=======Start crawling=======")
    for chap_url in chap_urls:
        crawl_1.go_to_webpage(chap_url)
        status = crawl_1.verify_element(locators_1.body_part, 10)
        if status is True:
            story_reading = crawl_1.find_element(locators_1.body_part)
            if story_reading is None:
                raise Exception(f"No element found with locator {locators_1.body_part}")
            header = crawl_1.find_element(locators_1.header, story_reading)
            part = crawl_1.find_element(locators_1.part, story_reading)
            if header is None or part is None:
                raise Exception(f"No element found with locator {locators_1.header} or {locators_1.part}")

            """Need to scroll to the end of the page to make all content display"""

            crawl_1.scroll_web_page_to_the_end()

            elements = crawl_1.find_elements(locators_1.page, part)
            line = []
            for element in elements:
                pre_tag = crawl_1.find_element(locators_1.pre_tage, element)
                line.append(crawl_1.get_element_text(pre_tag))

            text = " ".join(line)
            crawl_1.add_text_to_doc_file(header.text, text)

    crawl_1.quit_driver()


if __name__ == '__main__':
    crawl_chap_1_test()

'''Note: run this code using cmd: python3 -m test.hoa_hon'''