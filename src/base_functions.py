import pathlib
from typing import Tuple, Optional, List

import docx
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.keys import Keys
import os


class base(object):

    def __init__(self, is_headless_mode=True, timeout=15):
        options = webdriver.ChromeOptions()
        options.add_argument('--deny-permission-prompts')
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

    def switch_frame(self, frame_reference):
        """Switch to a frame by WebElement, name, or index."""
        self.driver.switch_to.frame(frame_reference)

    def switch_back_to_default(self):
        self.driver.switch_to.default_content()

    @staticmethod
    def remove_file_if_exists(file):
        try:
            if os.path.exists(file):
                os.remove(file)
        except Exception:
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

    def wait_for_page_load(self, timeout: Optional[int] = None) -> bool:
        """Wait until document.readyState == 'complete'. Returns True if loaded, False on timeout."""
        wait_time = timeout if timeout is not None else self.timeout
        try:
            WebDriverWait(self.driver, wait_time).until(
                lambda d: d.execute_script('return document.readyState') == 'complete'
            )
            return True
        except Exception:
            return False

    def wait_for_js_condition(self, js_condition: str, timeout: Optional[int] = None) -> bool:
        """Wait until the supplied JavaScript condition evaluates to a truthy value.

        Example: wait_for_js_condition('return window.someVar === true')
        """
        wait_time = timeout if timeout is not None else self.timeout
        try:
            WebDriverWait(self.driver, wait_time).until(
                lambda d: d.execute_script(js_condition)
            )
            return True
        except Exception:
            return False

    def wait_for_jquery(self, timeout: Optional[int] = None) -> bool:
        """Wait until jQuery active requests are finished (if jQuery is present).

        Falls back to True if jQuery is not present on the page.
        """
        wait_time = timeout if timeout is not None else self.timeout
        try:
            def _jq_inactive(d):
                try:
                    return d.execute_script('return (typeof jQuery !== "undefined") ? jQuery.active == 0 : true')
                except Exception:
                    return True

            WebDriverWait(self.driver, wait_time).until(_jq_inactive)
            return True
        except Exception:
            return False

    def wait_for_element_visible(self, style_tuple: Tuple[By, str], timeout: Optional[int] = None) -> WebElement:
        """Wait until the element located by `style_tuple` is visible and return it."""
        wait_time = timeout if timeout is not None else self.timeout
        return WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(style_tuple))

    def pass_data_to_file(self, source, file_name):
        try:
            f = open(file_name, "w")
            f.write(source)
        finally:
            f.close()

    def press_enter(self, element):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(element)).send_keys(Keys.ENTER)

    def input_text(self, element, text):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(element)).send_keys(text)

    def open_new_tab(self, url, tab_number=1):
        # Open a new blank tab and switch to the newly created window handle
        self.driver.execute_script("window.open('');")
        new_handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_handle)
        self.driver.get(url)

    def count_number_of_tabs(self):
        length = len(self.driver.window_handles)
        return length

    def switch_tab(self, tab_number):
        self.driver.switch_to.window(self.driver.window_handles[tab_number])

    def wait_until_page_contains(self, element, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(element))
        except:
            return False
        return True

    def get_attribute_from_all_elements(self, element, tag):
        attrs = []
        list_of_elements = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_all_elements_located(element))
        for i in list_of_elements:
            attrs.append(i.get_attribute(tag))
        return attrs

    def get_attribute_from_element(self, element, tag):
        e = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(element)).get_attribute(tag)
        return e
    
    def get_element_attribute(self, element: WebElement, tag: str) -> str:
        attr = element.get_attribute(tag)
        return attr

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

    def add_text_to_doc_file(self, title, text):
        document = docx.Document()
        try:
            document.add_heading(title)
            document.add_paragraph(text)
        except Exception as e:
            raise Exception("Exception while adding text to doc file.", e)
        finally:
            document.save(os.path.join(self.path, title + ".docx"))

    def scroll_web_page_to_the_end(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Adjust based on network/content load speed

            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def is_element_visible(self, element) -> bool:
        is_visible = (
                element.is_displayed() and
                self.driver.execute_script("""
                        const rect = arguments[0].getBoundingClientRect();
                        return (
                            rect.top >= 0 &&
                            rect.left >= 0 &&
                            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
                        );
                    """, element)
        )
        return is_visible

    def scroll_into_view(self, element):
        is_visible = self.is_element_visible(element)
        while not is_visible:
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
            is_visible = self.is_element_visible(element)

    def find_element(self, style_tuple: Tuple[By, str], parent_element: Optional[WebElement] = None) -> Optional[WebElement]:
        locator_strategy, locator_value = style_tuple
        if parent_element:
            element = parent_element.find_element(locator_strategy, locator_value)
        else:
            element = self.driver.find_element(locator_strategy, locator_value)
        return element

    def find_elements(self, style_tuple: Tuple[By, str], parent_element: Optional[WebElement] = None) -> List[WebElement]:
        locator_strategy, locator_value = style_tuple
        if parent_element:
            elements = parent_element.find_elements(locator_strategy, locator_value)
        else:
            elements = self.driver.find_elements(locator_strategy, locator_value)
        return elements

    @staticmethod
    def get_element_text(element) -> str:
        try:
            text = element.text.strip()
            return text
        except Exception as e:
            raise Exception("An exception occurred while getting element text.") from e

    def close_browser(self):
        self.driver.close()

    def quit_driver(self):
        self.driver.quit()
