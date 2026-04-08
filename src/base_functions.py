import pathlib
import re
from typing import Tuple, Optional, List, Union
import docx
import time
from docx.shared import Inches
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.keys import Keys
import pytesseract
from PIL import Image
import io
import os
from seleniumbase import Driver


class base(object):

    def __init__(self, is_headless_mode=True, timeout=5, use_seleniumbase=False):
        self.path = None
        self.timeout = timeout

        if use_seleniumbase:
            # ---------------------------------------------------------
            # SELENIUMBASE (By pass Cloudflare, Anti-bot)
            # ---------------------------------------------------------
            print("Starting browser with SeleniumBase (UC Mode)...")
            self.driver = Driver(
                uc=True,
                headless=is_headless_mode,
                no_sandbox=True,
                page_load_strategy="eager",
                window_size="1920,1080"
               
            )
        else:
            # ---------------------------------------------------------
            # SELENIUM
            # ---------------------------------------------------------
            print("Starting browser with Selenium...")
            options = webdriver.ChromeOptions()
            options.add_argument('--deny-permission-prompts')
            if is_headless_mode:
                options.add_argument('--headless=new')
            options.page_load_strategy = 'eager'
            options.add_argument('--disable-dev-shm-usage') 
            options.add_argument('--no-sandbox')
            options.add_argument('--window-size=1920,1080')
                
            self.driver = webdriver.Chrome(options=options)
        # Cài đặt Implicit Wait (Chờ tìm Element)
        self.driver.implicitly_wait(timeout)
        
        # BƯỚC 2: THIẾT QUÂN LUẬT - Không cho phép load trang nào quá 20 giây
        self.driver.set_page_load_timeout(20)


    def set_path(self, folder_name):
        """Chỉ định thư mục làm việc mà không cần tạo mới (Dành riêng cho đa luồng)"""
        cur_dir = os.path.abspath(os.getcwd())
        self.path = os.path.join(cur_dir, folder_name)


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
            return True
        except:
            return False

    def capture_full_screen(self, file_name: str):
        """
        Chụp ảnh toàn bộ trang web từ đầu đến cuối một cách an toàn.
        """
        full_file_path = os.path.join(self.path, f"{file_name}.png")
        print(f"Capturing full screen to: {full_file_path}")
        
        # BƯỚC 1: XỬ LÝ LAZY-LOAD (Bắt buộc)
        # Phải cuộn từ từ xuống cuối trang để ép web tải toàn bộ ảnh/nội dung ẩn
        self.scroll_web_page_to_the_end(pause_time=1, max_scrolls=20)
        
        # Cuộn ngược lại lên đầu trang để chuẩn bị chụp
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1) # Đợi các thanh menu cố định (sticky header) thu gọn lại

        try:
            # BƯỚC 2: CHỤP ẢNH TOÀN TRANG TÙY THEO LOẠI DRIVER
            
            # Nếu đang dùng SeleniumBase (Cách xịn nhất, không bị giới hạn OS)
            if hasattr(self.driver, "save_page_screenshot"):
                self.driver.save_page_screenshot(full_file_path)
                print("Completed using SeleniumBase!")
                
            # Nếu đang dùng Selenium thuần (Dùng Chrome DevTools Protocol - CDP)
            else:
                # Lấy thông số layout thực tế bằng CDP (Vượt qua mọi giới hạn màn hình)
                metrics = self.driver.execute_cdp_cmd('Page.getLayoutMetrics', {})
                content_width = metrics['contentSize']['width']
                content_height = metrics['contentSize']['height']
                
                # Gửi lệnh chụp toàn trang ở cấp độ lõi của Chrome
                screenshot_dict = self.driver.execute_cdp_cmd(
                    'Page.captureScreenshot', {
                        'format': 'png',
                        'captureBeyondViewport': True, # Chụp vượt khỏi màn hình
                        'clip': {
                            'width': content_width,
                            'height': content_height,
                            'x': 0,
                            'y': 0,
                            'scale': 1
                        }
                    }
                )
                
                # Lưu file ảnh từ dữ liệu Base64
                import base64
                with open(full_file_path, "wb") as f:
                    f.write(base64.b64decode(screenshot_dict['data']))
                print("Completed with Chrome CDP!")
                
        except Exception as e:
            print(f"An error occurred while capturing the full screen: {e}")


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

    def go_to_webpage(self, url: str, bypass_cloudflare: bool = False, reconnect_time: int = 4):
        """
        Truy cập web. 
        Nếu bypass_cloudflare = True, sẽ dùng UC Mode để vượt khiên.
        Nếu bypass_cloudflare = False, sẽ dùng lệnh get() tiêu chuẩn (rất nhanh).
        """
        
        try:
            # Chỉ ngắt kết nối khi bạn BẬT công tắc và đang xài SeleniumBase
            if bypass_cloudflare and hasattr(self.driver, "uc_open_with_reconnect"):
                self.driver.uc_open_with_reconnect(url, reconnect_time=reconnect_time)
                
            else:
                # Truy cập tốc độ cao, dùng lại Cookie đã có
                self.driver.get(url)
                
        except Exception as e:
            print(f"Error while loading {url}: {e}")

    def get_current_url(self):
        url = self.driver.current_url
        return url

    def click_element(self, element: Union[WebElement, Tuple[str, str]], force_js: bool = False) -> bool:
        try:
            target_element = element
            
            if isinstance(element, tuple):
                target_element = WebDriverWait(self.driver, self.timeout).until(
                    EC.presence_of_element_located(element)
                )
                
            if not isinstance(target_element, WebElement):
                raise TypeError("Element shoule be (By, str) tuple or WebElement.")

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target_element)

            if force_js:
                self.driver.execute_script("arguments[0].click();", target_element)
            else:
                WebDriverWait(self.driver, self.timeout).until(
                    EC.element_to_be_clickable(target_element)
                )
                target_element.click()
                
            return True

        # (FALLBACK)
        except ElementClickInterceptedException:
            print("Element is not interactable. Using JS Click to rescue...")
            self.driver.execute_script("arguments[0].click();", target_element)
            return True
            
        except TimeoutException:
            print(f"Error: Unable to find or click element within {self.timeout} seconds")
            return False
            
        except StaleElementReferenceException:
            print("Warning: Element has been stale.")
            return False
            
        except Exception as e:
            print(f"Unknown error: {e}")
            return False

    def reload_current_page(self):
        self.driver.refresh()

    def get_page_source(self) -> str:
        source = self.driver.page_source
        return source

    def wait_for_page_load(self, timeout: Optional[int] = None, poll_frequency: float = 0.5) -> bool:
        """Wait until document.readyState == 'complete'. Returns True if loaded, False on timeout."""
        wait_time = timeout if timeout is not None else self.timeout
        try:
            WebDriverWait(self.driver, wait_time, poll_frequency=poll_frequency).until(
                lambda d: d.execute_script('return document.readyState') == 'complete'
            )
            return True
        except TimeoutException:
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
    
    def wait_for_element_visible(self, element, timeout: Optional[int] = None) -> WebElement | None:
        """Wait until the element is visible and return it."""
        wait_time = timeout if timeout is not None else self.timeout
        if isinstance(element, tuple):
            try:
                return WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(element))
            except:
                return None
        elif isinstance(element, WebElement):
            try:
                return WebDriverWait(self.driver, wait_time).until(EC.visibility_of(element))
            except:
                return None
        raise TypeError("Invalid element type. Must be a (By, str) tuple or a WebElement.")

    def pass_data_to_file(self, source, file_name):
        try:
            f = open(file_name, "w")
            f.write(source)
        finally:
            f.close()
        
    def press_enter(self, element):
        if isinstance(element, WebElement):
            element.send_keys(Keys.ENTER)
        elif isinstance(element, tuple):
            self.find_element(element).send_keys(Keys.ENTER)
        else:
            raise TypeError("Invalid element type. Must be a (By, str) tuple or a WebElement.")

    def input_text(self, element, text):
        if isinstance(element, WebElement):
            element.clear()
            element.send_keys(text)
        elif isinstance(element, tuple):
            self.find_element(element).clear()
            self.find_element(element).send_keys(text)
        else:
            raise TypeError("Invalid element type. Must be a (By, str) tuple or a WebElement.")

    def open_new_tab(self, url):
        # Open a new blank tab and switch to the newly created window handle
        self.driver.execute_script("window.open('');")
        new_handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_handle)
        self.driver.get(url)

    def switch_tab(self, tab_number):
        self.driver.switch_to.window(self.driver.window_handles[tab_number])

    def get_attribute_from_all_elements(self, elements, attribute_name):
        attrs = []
        list_of_elements = []
        if isinstance(elements, tuple):
            list_of_elements = self.find_elements(elements)
        elif isinstance(elements, list) and all(isinstance(e, WebElement) for e in elements):
            list_of_elements = elements
        else:
            raise TypeError("Invalid elements type. Must be a (By, str) tuple or a list of WebElements.")
        for item in list_of_elements:
            attrs.append(item.get_attribute(attribute_name))
        return attrs

    def get_attribute_from_element(self, element, attribute_name: str) -> str:
        if isinstance(element, WebElement):
            return element.get_attribute(attribute_name)
        elif isinstance(element, tuple):
            return self.find_element(element).get_attribute(attribute_name)
        raise TypeError("Invalid element type. Must be a (By, str) tuple or a WebElement.")

    @staticmethod
    def replace_text(base_string, text_be_replaced, text_to_replace):
        new_string = str(base_string).replace(text_be_replaced, text_to_replace)
        return new_string

    @staticmethod
    def split_string(base_string, condition_split):
        data = str(base_string).split(condition_split)
        return data

    @staticmethod
    def crawl_data(url) -> BeautifulSoup | None:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=20)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            return soup
        else:
            print(f"Page {url} returned status {response.status_code}. Skipping.")
            return None
    
    @staticmethod
    def crawl_text_from_soup(soup: BeautifulSoup, css_locator: str) -> str:
        """Lấy text và giữ nguyên vị trí ảnh bằng Placeholder"""
        element = soup.select_one(css_locator)
        if not element:
            return ""

        # 1. Dọn rác tàng hình (Anti-scraping)
        for hidden_span in element.find_all('span', style=lambda value: value and 'font-size:0' in value.replace(' ', '')):
            hidden_span.decompose()

        # 2. TÌM VÀ ĐÁNH DẤU ẢNH
        for img in element.find_all('img'):
            # Lấy link ảnh (nhiều web dùng data-src để lazyload)
            src = img.get('src') or img.get('data-src') or img.get('data-original')
            if src:
                # Ép kiểu link (nếu web dùng link tương đối dạng //domain.com)
                if src.startswith("//"):
                    src = "https:" + src
                    
                # Tạo chuỗi đánh dấu thay thế cho thẻ img
                placeholder = f"\n[IMAGE_MARKER_START]{src}[IMAGE_MARKER_END]\n"
                img.replace_with(placeholder)

        # 3. Lấy toàn bộ Text (Lúc này ảnh đã biến thành các dòng chữ Marker)
        return element.get_text(separator='\n', strip=True)


    def save_doc(self, title, body) -> None:
        document = docx.Document()
        try:
            document.add_heading(title.get_text())
            document.add_paragraph(body.get_text(separator='\n', strip=True))
            document.save(os.path.join(self.path, str(title.get_text()) + ".docx"))
        except:
            document.add_heading(title.text)
            if hasattr(body, 'get_text'):
                document.add_paragraph(body.get_text(separator='\n', strip=True))
            else:
                document.add_paragraph(body.text)
            document.save(os.path.join(self.path, str(title.text) + ".docx"))

    @staticmethod
    def get_element_by_tag(soup, tag, class_name):
        element = soup.find(tag, class_=class_name)
        return element

    @staticmethod
    def get_element_by_class(soup, class_name):
        element = soup.find(class_=class_name)
        return element

    def add_text_to_doc_file(self, title: str, text: str, file_name: Optional[str] = None):
        document = docx.Document()
        try:
            # Thêm tiêu đề
            document.add_heading(title)
            
            # Tách nội dung thành từng dòng
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if not line:
                    document.add_paragraph("") # Giữ khoảng trống ngắt cảnh
                    continue
                
                # KIỂM TRA: DÒNG NÀY LÀ ẢNH HAY CHỮ?
                if "[IMAGE_MARKER_START]" in line:
                    # Tách link ảnh ra khỏi marker bằng Regex
                    # (Phòng trường hợp HTML lồng chữ và ảnh trên cùng 1 dòng)
                    parts = re.split(r'\[IMAGE_MARKER_START\](.*?)\[IMAGE_MARKER_END\]', line)
                    
                    for part in parts:
                        part = part.strip()
                        if not part: continue
                        
                        # Nếu là link ảnh -> Tải và chèn ảnh
                        if part.startswith("http"):
                            try:
                                res = requests.get(part, timeout=10)
                                if res.status_code == 200:
                                    image_stream = io.BytesIO(res.content)
                                    document.add_picture(image_stream, width=Inches(5.0))
                                else:
                                    document.add_paragraph(f"[Không thể tải ảnh minh họa: Lỗi {res.status_code}]")
                            except Exception:
                                document.add_paragraph(f"[Mất kết nối khi tải ảnh minh họa]")
                        
                        # Nếu là chữ vô tình dính kèm -> Viết chữ bình thường
                        else:
                            document.add_paragraph(part)
                            
                # Nếu chỉ là dòng chữ bình thường
                else:
                    document.add_paragraph(line)
            
            # Lưu file an toàn
            safe_name = file_name if file_name else re.sub(r'[\\/*?:"<>|]', "", title).strip()
            final_path = os.path.join(self.path, safe_name + ".docx")
            document.save(final_path)
            
        except Exception as e:
            raise Exception(f"Lỗi khi ghi nội dung vào file Word '{file_name or title}': {e}")
        
    @staticmethod
    def sleep(delay_time):
        time.sleep(delay_time)

    def scroll_web_page_to_the_end(self, pause_time=2, max_scrolls=50) -> bool:
        """
        Scrolls to the bottom of the page.
        Returns True if it hit the absolute bottom, False if it hit the max_scrolls limit.
        """
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        scroll_count = 0

        while scroll_count < max_scrolls:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            # Wait to load page
            time.sleep(pause_time)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            
            if new_height == last_height:
                # DOUBLE CHECK: Give it one more second to be absolutely sure it's not just a slow network
                time.sleep(1)
                new_height_check = self.driver.execute_script("return document.body.scrollHeight")
                if new_height_check == last_height:
                    print(f"Reached absolute bottom after {scroll_count} scrolls.")
                    return True # Signal: Success
                    
            last_height = new_height
            scroll_count += 1

        print(f"Warning: Stopped scrolling after hitting the maximum limit of {max_scrolls} scrolls.")
        return False # Signal: Reached limit before finding the bottom

    def is_element_visible(self, element) -> bool:
        if isinstance(element, tuple):
            try:
                web_element = self.find_element(element)
            except:
                return False
        elif isinstance(element, WebElement):
            web_element = element
        else:
            raise TypeError("Invalid element type. Must be a (By, str) tuple or a WebElement.")

        return web_element.is_displayed()

    def scroll_into_view(self, element) -> bool:
        """
        Scrolls the page up or down to center the element.
        Returns True if the element becomes visible, False otherwise.
        """
        try:
            # 1. Execute the scroll command EXACTLY ONCE
            self.driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", 
                element
            )
            
            # 2. Pause briefly to allow the smooth scrolling animation to finish
            time.sleep(0.8) # Adjust this if the page is very long/slow
            
            # 3. Check visibility once after arriving
            if self.is_element_visible(element):
                return True
            else:
                print("Warning: Scrolled to element, but it is still hidden (e.g., behind a banner or display: none).")
                return False
                
        except Exception as e:
            print(f"Failed to scroll to element: {e}")
            return False

    def find_element(self, element_, parent_element: Optional[WebElement] = None) -> Optional[WebElement]:
        target = parent_element if parent_element else self.driver
        if isinstance(element_, tuple):
            return target.find_element(*element_)
        elif isinstance(element_, WebElement):
            return element_ # Already a WebElement
        raise TypeError("Invalid element type. Must be a (By, str) tuple or a WebElement.")

    def find_elements(self, style_tuple: Tuple[By, str], parent_element: Optional[WebElement] = None) -> List[WebElement]:
        locator_strategy, locator_value = style_tuple
        if parent_element:
            elements = parent_element.find_elements(locator_strategy, locator_value)
        else:
            elements = self.driver.find_elements(locator_strategy, locator_value)
        return elements

    def get_element_text(self, element: Union[WebElement, Tuple[str, str]], extract_hidden: bool = False) -> str:
        try:
            target_element = element
            if isinstance(element, tuple):
                target_element = self.find_element(element)
                
            if not isinstance(target_element, WebElement):
                raise TypeError("Đầu vào bắt buộc phải là (By, str) tuple hoặc WebElement.")

            if extract_hidden:
                raw_text = target_element.get_attribute("textContent")
                return raw_text.strip() if raw_text else ""
            else:
                # ========================================================
                # BỘ QUÉT VĂN BẢN VÀ ẢNH (TEXT & IMAGE SCANNER)
                # ========================================================
                js_script = """
                var target = arguments[0];
                
                function extractText(node) {
                    // BƯỚC 1: XỬ LÝ TEXT NODE THUẦN TÚY (Chữ nằm giữa các thẻ)
                    if (node.nodeType === 3) { 
                        var parentStyle = window.getComputedStyle(node.parentNode);
                        if (parseFloat(parentStyle.fontSize) === 0 || 
                            parentStyle.display === 'none' || 
                            parentStyle.visibility === 'hidden' || 
                            parentStyle.opacity === '0' ||
                            parentStyle.color === 'rgba(0, 0, 0, 0)' ||
                            parentStyle.color === 'transparent') {
                            return "";
                        }
                        return node.nodeValue;
                    }
                    
                    // BƯỚC 2: XỬ LÝ ELEMENT NODE (Các thẻ div, p, span, img...)
                    if (node.nodeType === 1) { 
                        var style = window.getComputedStyle(node);
                        if (style.display === 'none' || style.visibility === 'hidden' || style.opacity === '0') {
                            return "";
                        }
                        
                        // ----------------------------------------------------
                        // BẢN VÁ: NHẬN DIỆN VÀ ĐÁNH DẤU ẢNH (PLACEHOLDER)
                        // ----------------------------------------------------
                        if (node.tagName === 'IMG') {
                            // node.src trong JS sẽ tự động nối link tương đối thành tuyệt đối
                            // Nếu web dùng lazyload, fallback sang data-src hoặc data-original
                            var src = node.src || node.getAttribute('data-src') || node.getAttribute('data-original');
                            if (src) {
                                return "\\n[IMAGE_MARKER_START]" + src + "[IMAGE_MARKER_END]\\n";
                            }
                            return "";
                        }
                        // ----------------------------------------------------
                        
                        var text = "";
                        
                        // Xử lý thẻ xuống dòng <br> và thẻ khối (p, div) để tách đoạn
                        if (node.tagName === 'BR' || style.display === 'block' || node.tagName === 'P') {
                            text += "\\n";
                        }
                        
                        // LẤY CHỮ BỊ GIẤU TRONG CSS ::before
                        var before = window.getComputedStyle(node, '::before');
                        if (before && before.content && before.content !== 'none' && before.content !== 'normal') {
                            if (parseFloat(before.fontSize) > 0 && before.opacity !== '0') {
                                text += before.content.replace(/^["']|["']$/g, '');
                            }
                        }
                        
                        // Đi sâu vào đọc tiếp các thẻ con bên trong
                        for (var i = 0; i < node.childNodes.length; i++) {
                            text += extractText(node.childNodes[i]);
                        }
                        
                        // LẤY CHỮ BỊ GIẤU TRONG CSS ::after
                        var after = window.getComputedStyle(node, '::after');
                        if (after && after.content && after.content !== 'none' && after.content !== 'normal') {
                            if (parseFloat(after.fontSize) > 0 && after.opacity !== '0') {
                                text += after.content.replace(/^["']|["']$/g, '');
                            }
                        }
                        
                        return text;
                    }
                    return "";
                }
                
                var result = extractText(target);
                
                // BƯỚC 3: LÀM SẠCH VĂN BẢN
                result = result.replace(/\\r/g, '')
                               .replace(/[ \\t]+/g, ' ')
                               .replace(/\\n\\s+/g, '\\n')
                               .replace(/\\n{3,}/g, '\\n\\n');
                               
                return result.trim();
                """
                
                clean_text = self.driver.execute_script(js_script, target_element)
                return clean_text if clean_text else ""

        except StaleElementReferenceException:
            print("Warning: Element has been stale.")
            return ""
        except Exception as e:
            print(f"Unknown error: {e}")
            return ""

    def close_browser(self):
        self.driver.close()

    def quit_driver(self):
        self.driver.quit()

    def extract_images_to_file(self, elements: List[WebElement], file_name: str):
        """
        Cuộn đến từng ảnh, quét OCR và lưu vào file Word (.docx).
        """
        if not elements:
            print("Danh sách thẻ (elements) truyền vào đang trống! Không có gì để quét.")
            return

        print(f"Bắt đầu quét {len(elements)} bức ảnh và lưu vào: {file_name}")
        file_path = os.path.join(self.path, file_name + ".docx")

        # 1. Khởi tạo Document (Tạo file mới hoặc mở file cũ nếu đã tồn tại)
        if os.path.exists(file_path):
            document = docx.Document(file_path)
        else:
            document = docx.Document()
            document.add_heading(f"Dữ liệu quét từ ảnh: {file_name}", level=1)

        # 2. Vòng lặp xử lý từng ảnh
        for index, img in enumerate(elements, start=1):
            try:
                # Cuộn màn hình đến vị trí bức ảnh
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", img)
                time.sleep(1.5) # Đợi Lazy-load
                
                # Chụp ảnh và mở bằng Pillow
                image_bytes = img.screenshot_as_png
                image = Image.open(io.BytesIO(image_bytes))
                
                # Gọi Tesseract
                print(f"Đang dịch ảnh {index}/{len(elements)}...")
                text = pytesseract.image_to_string(image, lang='vie')
                
                # Ghi vào Document trong RAM
                if text.strip():
                    document.add_paragraph(text.strip())
                    
            except Exception as e:
                print(f"Lỗi ở ảnh thứ {index}: {e}")
                document.add_paragraph(f"[Lỗi không đọc được ảnh {index}]")

        # 3. Lưu toàn bộ kết quả từ RAM xuống ổ cứng (Chỉ lưu 1 lần cho nhanh)
        try:
            document.save(file_path)
            print(f"\nHOÀN THÀNH! Toàn bộ nội dung đã được lưu chuẩn vào file {file_name}.docx")
        except Exception as e:
            print(f"Lỗi khi lưu file DOCX: {e}")
