import pathlib
import docx
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import os


class base(object):

    def __init__(self, timeout=5):
        self.path = None
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.timeout = timeout
        self.driver.implicitly_wait(10)

    def create_folder(self, folder_name):
        cur_dir = os.path.abspath(os.getcwd())
        dir_name = folder_name
        self.path = os.path.join(cur_dir, dir_name)
        pathlib.Path(self.path).mkdir(parents=True, exist_ok=True)

    def capture_screen(self, name):
        s = lambda x: self.driver.execute_script('return document.body.parentNode.scroll' + x)
        self.driver.set_window_size(s('Width'), s('Height'))  # May need manual adjustment
        self.driver.find_element(By.TAG_NAME, 'body').screenshot(name)

    def define_img_name(self, title):
        file_name = os.path.join(self.path, title + ".png")
        return file_name

    def open_chrome_in_headless_mode(self, url):
        self.driver.get(url)

    def get_current_url(self):
        url = self.driver.current_url
        return url

    def click_element(self, element):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(element)).click()

    def reload_current_page(self):
        self.driver.get(self.driver.current_url)

    def wait_until_page_contains(self, element):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(element))

    def get_attribute_from_tag(self, element, tag):
        attribute = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(element)
                                                                   ).get_attribute(tag)
        return attribute

    @staticmethod
    def replace_text(base_string, text_be_replaced, text_to_replace):
        new_string = str(base_string).replace(text_be_replaced, text_to_replace)
        return new_string

    @staticmethod
    def split_string(base_string, condition_split):
        data = str(base_string).split(condition_split)
        return data

    @staticmethod
    def crawl_data(url):
        req = requests.get(url)
        soup = BeautifulSoup(req.content, "html.parser")
        return soup

    def save_doc(self, title, body):
        document = docx.Document()
        document.add_heading(title.get_text())
        document.add_paragraph(body.get_text(separator='\n', strip=True))
        document.save(os.path.join(self.path, str(title.get_text()) + ".docx"))

    @staticmethod
    def get_title_by_class(soup, title_element):
        title = soup.find(class_=title_element)
        return title

    @staticmethod
    def get_body_by_class(soup, body_element):
        body = soup.find(class_=body_element)
        return body

    @staticmethod
    def get_title_by_id(soup, title_element):
        title = soup.find(id=title_element)
        return title

    @staticmethod
    def get_body_by_id(soup, body_element):
        body = soup.find(id=body_element)
        return body

    def close_browser(self):
        self.driver.close()

    def quit_driver(self):
        self.driver.quit()
