from selenium.webdriver.common.by import By
from dataclasses import dataclass

@dataclass
class truyenfullvision:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")