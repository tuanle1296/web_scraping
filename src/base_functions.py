import time
from typing import Literal, Tuple, Optional, List, Union, Any

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from curl_cffi import requests as curl_requests
import os
from seleniumbase import Driver

# Import new FileManager
from src.file_manager import FileManager, get_config_folder_id


class Base(FileManager):
    """
    Base class for web scraping and automation.
    Inherits file management capabilities from FileManager.
    """

    def __init__(self, is_headless_mode: bool = True, timeout: int = 5, use_seleniumbase: bool = False, page_load_strategy: str = "eager") -> None:
        """
        Initializes the browser and file manager.
        """
        # Initialize FileManager (sets self.path)
        super().__init__()
        
        self.timeout = timeout

        if use_seleniumbase:
            print(f"Starting browser with SeleniumBase (UC Mode, strategy={page_load_strategy})...")
            self.driver = Driver(
                uc=True,
                headless=is_headless_mode,
                no_sandbox=True,
                disable_gpu=True, # Thêm flag này cho Docker
                page_load_strategy=page_load_strategy,
                window_size="1920,1080"
            )
        else:
            print(f"Starting browser with Selenium (strategy={page_load_strategy})...")
            options = webdriver.ChromeOptions()
            options.add_argument('--deny-permission-prompts')
            if is_headless_mode:
                options.add_argument('--headless=new')
            options.add_argument('--disable-dev-shm-usage') # Đã có - rất quan trọng
            options.add_argument('--no-sandbox') # Đã có - rất quan trọng
            options.add_argument('--disable-gpu') # Thêm flag này
            options.add_argument('--disable-software-rasterizer') # Thêm flag này
            options.add_argument('--window-size=1920,1080')
                
            self.driver = webdriver.Chrome(options=options)
        
        self.driver.implicitly_wait(timeout)
        self.driver.set_page_load_timeout(20)

    def __enter__(self) -> 'Base':
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.quit_driver()

    def maximize_browser(self) -> None:
        """Maximizes the browser window."""
        self.driver.maximize_window()

    def verify_element(self, element: Tuple[str, str], timeout: int = 5) -> bool:
        """Checks if an element is visible on the page."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(element))
            return True
        except TimeoutException:
            return False

    def capture_full_screen(self, file_name: str) -> None:
        """Safely captures a full-page screenshot from top to bottom."""
        if not self.path:
            raise ValueError("Working path not set. Call set_path or create_folder first.")
            
        full_file_path = os.path.join(self.path, f"{file_name}.png")
        print(f"Capturing full screen to: {full_file_path}")
        
        self.scroll_web_page_to_the_end(pause_time=1, max_scrolls=20)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)

        try:
            if hasattr(self.driver, "save_page_screenshot"):
                self.driver.save_page_screenshot(full_file_path)
            else:
                metrics = self.driver.execute_cdp_cmd('Page.getLayoutMetrics', {})
                content_width = metrics['contentSize']['width']
                content_height = metrics['contentSize']['height']
                screenshot_dict = self.driver.execute_cdp_cmd(
                    'Page.captureScreenshot', {
                        'format': 'png',
                        'captureBeyondViewport': True,
                        'clip': {'width': content_width, 'height': content_height, 'x': 0, 'y': 0, 'scale': 1}
                    }
                )
                import base64
                with open(full_file_path, "wb") as f:
                    f.write(base64.b64decode(screenshot_dict['data']))
                print("Completed with Chrome CDP!")
        except Exception as e:
            print(f"An error occurred while capturing the full screen: {e}")

    def switch_frame(self, frame_reference: Union[WebElement, str, int]) -> None:
        """Switch to a frame by WebElement, name, or index."""
        self.driver.switch_to.frame(frame_reference)

    def switch_back_to_default(self) -> None:
        """Switches back to the main content from an iframe."""
        self.driver.switch_to.default_content()

    def go_to_webpage(self, url: str, bypass_cloudflare: bool = False, reconnect_time: int = 4) -> None:
        """Navigates to a webpage."""
        try:
            if bypass_cloudflare and hasattr(self.driver, "uc_open_with_reconnect"):
                self.driver.uc_open_with_reconnect(url, reconnect_time=reconnect_time)
            else:
                self.driver.get(url)
        except Exception as e:
            print(f"Error while loading {url}: {e}")

    def get_current_url(self) -> str:
        """Returns the current URL of the webpage."""
        return self.driver.current_url

    def click_element(self, element: Union[WebElement, Tuple[str, str]], force_js: bool = False) -> bool:
        """Clicks an element, optionally using JavaScript."""
        try:
            target_element = element
            if isinstance(element, tuple):
                target_element = WebDriverWait(self.driver, self.timeout).until(
                    EC.presence_of_element_located(element)
                )
            if not isinstance(target_element, WebElement):
                raise TypeError("Element should be (By, str) tuple or WebElement.")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target_element)
            if force_js:
                self.driver.execute_script("arguments[0].click();", target_element)
            else:
                WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(target_element))
                target_element.click()
            return True
        except Exception as e:
            print(f"Click error: {e}")
            self.driver.execute_script("arguments[0].click();", target_element)
            return True

    def reload_current_page(self) -> None:
        """Reloads the current page."""
        self.driver.refresh()

    def get_page_source(self) -> str:
        """Returns the HTML source code of the current page."""
        return self.driver.page_source

    def wait_for_page_load(self, timeout: Optional[int] = None, poll_frequency: float = 0.5) -> bool:
        """Wait until document.readyState == 'complete'."""
        wait_time = timeout if timeout is not None else self.timeout
        try:
            WebDriverWait(self.driver, wait_time, poll_frequency=poll_frequency).until(
                lambda d: d.execute_script('return document.readyState') == 'complete'
            )
            return True
        except TimeoutException:
            return False

    def wait_for_js_condition(self, js_condition: str, timeout: Optional[int] = None) -> bool:
        """Wait until the supplied JavaScript condition evaluates to a truthy value."""
        wait_time = timeout if timeout is not None else self.timeout
        try:
            WebDriverWait(self.driver, wait_time).until(lambda d: d.execute_script(js_condition))
            return True
        except TimeoutException:
            return False

    def wait_for_jquery(self, timeout: Optional[int] = None) -> bool:
        """Wait until jQuery active requests are finished."""
        wait_time = timeout if timeout is not None else self.timeout
        try:
            def _jq_inactive(d):
                try:
                    return d.execute_script('return (typeof jQuery !== "undefined") ? jQuery.active == 0 : true')
                except Exception:
                    return True
            WebDriverWait(self.driver, wait_time).until(_jq_inactive)
            return True
        except TimeoutException:
            return False
    
    def wait_for_element_visible(self, element: Union[WebElement, Tuple[str, str]], timeout: Optional[int] = None) -> bool:
        """Wait until the element is visible."""
        wait_time = timeout if timeout is not None else self.timeout
        try:
            if isinstance(element, tuple):
                WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(element))
                return True
            elif isinstance(element, WebElement):
                WebDriverWait(self.driver, wait_time).until(EC.visibility_of(element))
                return True
            return False
        except TimeoutException:
            return False

    def press_enter(self, element: Union[WebElement, Tuple[str, str]]) -> None:
        """Sends an ENTER key to an element."""
        target = element if isinstance(element, WebElement) else self.find_element(element)
        if target:
            target.send_keys(Keys.ENTER)

    def input_text(self, element: Union[WebElement, Tuple[str, str]], text: str) -> None:
        """Clears existing content and types new text into an element."""
        target = element if isinstance(element, WebElement) else self.find_element(element)
        if target:
            target.clear()
            target.send_keys(text)

    def open_new_tab(self, url: str) -> None:
        """Opens a new tab and navigates to the specified URL."""
        self.driver.execute_script("window.open('');")
        new_handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_handle)
        self.driver.get(url)

    def switch_tab(self, tab_number: int) -> None:
        """Switches to a tab by its index."""
        self.driver.switch_to.window(self.driver.window_handles[tab_number])

    def get_attribute_from_all_elements(self, elements: Union[Tuple[str, str], List[WebElement]], attribute_name: str) -> List[Optional[str]]:
        """Retrieves a specific attribute from all elements in a list."""
        list_of_elements = self.find_elements(elements) if isinstance(elements, tuple) else elements
        return [item.get_attribute(attribute_name) for item in list_of_elements]

    def get_attribute_from_element(self, element: Union[WebElement, Tuple[str, str]], attribute_name: str) -> Optional[str]:
        """Retrieves a specific attribute from an element."""
        target = element if isinstance(element, WebElement) else self.find_element(element)
        return target.get_attribute(attribute_name) if target else None

    @staticmethod
    def replace_text(base_string: str, text_be_replaced: str, text_to_replace: str) -> str:
        """Replaces text within a string."""
        return str(base_string).replace(text_be_replaced, text_to_replace)

    @staticmethod
    def split_string(base_string: str, condition_split: str) -> List[str]:
        """Splits a string based on a condition."""
        return str(base_string).split(condition_split)

    @staticmethod
    def crawl_data(
        url: str, 
        return_type: Literal["soup", "text", "content"] = "soup",
        impersonate: Optional[str] = "chrome120"
    ) -> Union[BeautifulSoup, str, bytes, None]:
        """Crawls a URL using curl_requests and returns the data."""
        try:
            request_args = {"timeout": 20}
            if impersonate:
                request_args["impersonate"] = impersonate
            else:
                request_args["headers"] = {'User-Agent': 'Mozilla/5.0'}
            response = curl_requests.get(url, **request_args)
            if response.status_code == 200:
                if return_type == "soup": return BeautifulSoup(response.content, "html.parser")
                elif return_type == "text": return response.text
                elif return_type == "content": return response.content
            return None
        except Exception as e:
            print(f"Error crawling {url}: {e}")
            return None

    @staticmethod
    def crawl_text_from_soup(data: Union[BeautifulSoup, str, None], css_locator: str) -> str:
        """Extracts text and preserves image placeholders from Soup or HTML string."""
        if not data: return ""
        soup = BeautifulSoup(data, "html.parser") if isinstance(data, str) else data
        element = soup.select_one(css_locator)
        if not element: return ""
        for hidden_span in element.find_all('span', style=lambda v: v and 'font-size:0' in v.replace(' ', '')):
            hidden_span.decompose()
        for img in element.find_all('img'):
            src = img.get('src') or img.get('data-src') or img.get('data-original')
            if src:
                if src.startswith("//"): src = "https:" + src
                placeholder = f"\n[IMAGE_MARKER_START]{src}[IMAGE_MARKER_END]\n"
                img.replace_with(placeholder)
        return element.get_text(separator='\n', strip=True)

    @staticmethod
    def get_element_by_tag(soup: BeautifulSoup, tag: str, class_name: str) -> Optional[Any]:
        """Finds an element based on tag and class name."""
        return soup.find(tag, class_=class_name)

    @staticmethod
    def get_element_by_class(soup: BeautifulSoup, class_name: str) -> Optional[Any]:
        """Finds an element based on class name."""
        return soup.find(class_=class_name)

    @staticmethod
    def sleep(delay_time: float) -> None:
        """Pauses execution for the specified duration."""
        time.sleep(delay_time)

    def scroll_web_page_to_the_end(self, pause_time: float = 2, max_scrolls: int = 50) -> bool:
        """Scrolls to the bottom of the page."""
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        scroll_count = 0
        while scroll_count < max_scrolls:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(pause_time)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                time.sleep(1)
                if self.driver.execute_script("return document.body.scrollHeight") == last_height: return True
            last_height = new_height
            scroll_count += 1
        return False

    def is_element_visible(self, element: Union[WebElement, Tuple[str, str]]) -> bool:
        """Checks if an element is currently displayed."""
        target = element if isinstance(element, WebElement) else self.find_element(element)
        try: return target.is_displayed() if target else False
        except Exception: return False

    def scroll_into_view(self, element: WebElement) -> bool:
        """Scrolls the page to center the element."""
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
            time.sleep(0.8)
            return self.is_element_visible(element)
        except Exception: return False

    def find_element(self, locator: Tuple[str, str], parent_element: Optional[WebElement] = None) -> Optional[WebElement]:
        """Finds a single element based on a locator."""
        target = parent_element if parent_element else self.driver
        try: return target.find_element(*locator)
        except NoSuchElementException: return None 

    def find_elements(self, locator: Tuple[str, str], parent_element: Optional[WebElement] = None) -> List[WebElement]:
        """Finds all elements matching a locator."""
        target = parent_element if parent_element else self.driver
        return target.find_elements(*locator)

    def get_element_text(self, element: Union[WebElement, Tuple[str, str]], extract_hidden: bool = False) -> str:
        """Extracts cleaned text from an element, including support for images."""
        target_element = element if isinstance(element, WebElement) else self.find_element(element)
        if not target_element: return ""
        if extract_hidden:
            raw = target_element.get_attribute("textContent")
            return raw.strip() if raw else ""
        js_script = """
        var target = arguments[0];
        function extractText(node) {
            if (node.nodeType === 3) { 
                var parentStyle = window.getComputedStyle(node.parentNode);
                if (parseFloat(parentStyle.fontSize) === 0 || styleVisible(parentStyle)) return "";
                return node.nodeValue;
            }
            if (node.nodeType === 1) { 
                var style = window.getComputedStyle(node);
                if (styleVisible(style)) return "";
                if (node.tagName === 'IMG') {
                    var src = node.src || node.getAttribute('data-src') || node.getAttribute('data-original');
                    return src ? "\\n[IMAGE_MARKER_START]" + src + "[IMAGE_MARKER_END]\\n" : "";
                }
                var text = "";
                if (node.tagName === 'BR' || style.display === 'block' || node.tagName === 'P') text += "\\n";
                var before = window.getComputedStyle(node, '::before');
                if (before && before.content && before.content !== 'none' && parseFloat(before.fontSize) > 0) text += before.content.replace(/^["']|["']$/g, '');
                for (var i = 0; i < node.childNodes.length; i++) text += extractText(node.childNodes[i]);
                var after = window.getComputedStyle(node, '::after');
                if (after && after.content && after.content !== 'none' && parseFloat(after.fontSize) > 0) text += after.content.replace(/^["']|["']$/g, '');
                return text;
            }
            return "";
        }
        function styleVisible(s) { return s.display === 'none' || s.visibility === 'hidden' || s.opacity === '0' || s.color === 'transparent'; }
        return extractText(target).replace(/[ \\t]+/g, ' ').replace(/\\n\\s+/g, '\\n').replace(/\\n{3,}/g, '\\n\\n').trim();
        """
        return self.driver.execute_script(js_script, target_element)

    def close_browser(self) -> None:
        """Closes the current tab."""
        self.driver.close()

    def quit_driver(self) -> None:
        """Quits the browser session."""
        self.driver.quit()
