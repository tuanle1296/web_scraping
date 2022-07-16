import pathlib
import docx
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.keys import Keys
import os


class base(object):

    def __init__(self, is_headless_mode=True, timeout=10):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        options.headless = is_headless_mode
        self.driver = webdriver.Chrome(options=options)
        self.path = None
        self.timeout = timeout
        self.driver.implicitly_wait(self.timeout)

    def create_folder(self, folder_name):
        cur_dir = os.path.abspath(os.getcwd())
        dir_name = folder_name
        self.path = os.path.join(cur_dir, dir_name)
        pathlib.Path(self.path).mkdir(parents=True, exist_ok=True)

    def maximize_browser(self):
        self.driver.maximize_window()

    def verify_element(self, element, timeOut=5):
        try:
            WebDriverWait(self.driver, timeOut).until(EC.visibility_of_element_located(element))
        except:
            return False
        return True

    def count_elements(self, element):
        length = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located(element))
        return len(length)

    def capture_screen(self, name):
        s = lambda x: self.driver.execute_script('return document.body.parentNode.scroll' + x)
        self.driver.set_window_size(s('Width'), s('Height'))  # May need manual adjustment
        self.driver.find_element(By.TAG_NAME, 'body').screenshot(name)

    def scroll_web_page_to_the_end(self):
        pause_time = 0.5
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(pause_time)
            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    @staticmethod
    def remove_file_if_exists(file):
        try:
            os.path.exists(file)
            os.remove(file)
        except:
            pass

    def define_img_name(self, title):
        file_name = os.path.join(self.path, title + ".png")
        return file_name

    def go_to_webpage(self, url):
        self.driver.get(url)

    def get_current_url(self):
        url = self.driver.current_url
        return url

    def click_element(self, element):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(element)).click()

    def reload_current_page(self):
        self.driver.refresh()

    def get_page_source(self):
        source = self.driver.page_source
        return source

    def pass_data_to_file(self, source, file_name):
        try:
            f = open(file_name, "w")
            f.write(source)
        finally:
            f.close()

    def press_Enter(self, element):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(element)).send_keys(Keys.ENTER)

    def input_text(self, element, text):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(element)).send_keys(text)

    def open_new_tab(self, url, tab_number=1):
        self.driver.execute_script('''window.open('about:blank', ''' +
                                   str(tab_number) + ''');''')
        self.driver.switch_to.window(str(tab_number))
        self.driver.get(url)

    def count_number_of_tabs(self):
        length = len(self.driver.window_handles)
        return length

    def switch_tab(self, tab_number):
        self.driver.switch_to.window(self.driver.window_handles[tab_number])

    def wait_until_page_contains(self, element, timeout=5):
        self.timeout = timeout
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(element))

    def get_attribute_from_all_elements(self, element, tag):
        list = []
        list_of_elements = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_all_elements_located(element))
        for i in list_of_elements:
            list.append(i.get_attribute(tag))
        return list

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
        try:
            document.add_heading(title.get_text())
            document.add_paragraph(body.get_text(separator='\n', strip=True))
            document.save(os.path.join(self.path, str(title.get_text()) + ".docx"))
        except:
            document.add_heading(title.text)
            document.add_paragraph(body.get_text(separator='\n', strip=True))
            document.save(os.path.join(self.path, str(title.text) + ".docx"))

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
