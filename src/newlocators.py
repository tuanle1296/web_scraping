from selenium.webdriver.common.by import By
from dataclasses import dataclass

@dataclass
class truyenfullvision:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")
    pagination : tuple[By, str] = (By.CSS_SELECTOR, "ul.pagination")
    page_link : tuple[By, str] = (By.CSS_SELECTOR, "li")


@dataclass
class mongtruyen:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div#result-danh-sach-chuong")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".mdv-san-pham-detail-chuong-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div#noi_dung_truyen")
    pagination : tuple[By, str] = (By.CSS_SELECTOR, "div.mvd-san-pham-show-danh-sach-chuong-pagination")
    page_link : tuple[By, str] = (By.CSS_SELECTOR, "a.page-link")
    signin_signup_link : tuple[By, str] = (By.CSS_SELECTOR, ".hydrosite-mong-truyen-user-text")
    username_signin_field : tuple[By, str] = (By.CSS_SELECTOR, "input[name='username']")
    password_signin_field : tuple[By, str] = (By.CSS_SELECTOR, "input[name='password']")
    signin_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "input[name='dangnhap']")   
    password_input_field : tuple[By, str] = (By.CSS_SELECTOR, "input.password-input")
    password_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "button#btnSubmitPassword")
    accept_warning_btn : tuple[By, str] = (By.CSS_SELECTOR, "div.gioi-han-do-tuoi-warning-box a.gioi-han-do-tuoi-btn-continue")

@dataclass
class wordpress:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")
    password_input_field : tuple[By, str] = (By.CSS_SELECTOR, "input[name='post_password']")
    password_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "input[name='Submit']")