from selenium.webdriver.common.by import By


class xiao_link:
    next_btn = (By.XPATH, "//p[@style='text-align:right;']//a")
    cur_title = 'entry-title'
    cur_content = 'entry-content'
    is_content_img = (By.XPATH, "//div[@class='entry-content']//img")


class onlytlinh:
    next_chap = "//div[@class='entry-content']//a[contains(text(),'Chương INPUT')]"
    next_chap_ngoai = "//div[@class='entry-content']//a[contains(text(),'Ngoại truyện INPUT')]"
    cur_title = 'entry-title'
    cur_content = 'entry-content'
    pass_input_field = (By.XPATH, "//input[@name='post_password']")
    accept_cookies_btn = (By.XPATH, "//div[@class='hide-on-button ads-active']//input[@type='submit']")
    pass_1 = "tanthanh"
    pass_2 = "SuanNing"
    pass_3 = "onlytlinhLuyiningChengxinglin"

class kethonsailam:
    next_from_1_to_31 = (By.XPATH, "//div[@id='post-navigation']//div[@class='nav-next']")
    content_from_chap_1_to_31 = 'entry-inner'
    title_from_chap_1_to_31 = 'post-title'
    next_from_32_to_57 = (By.XPATH, "//div[@class='nav-next']")
    title_from_chap_32_to_57 = 'entry-title'
    content_from_chap_32_to_57 = 'entry-content'
    close_cookies_banner = (By.XPATH, "//form//input[@value='Đồng ý']")
    password_field = (By.XPATH, "//input[@type='password']")
    submit_password_btn = (By.XPATH, "//input[@value='Nhập']")
    password_nt_1_2 = "LamThien"
    password_nt_3 = "2708"

class kcnna:
    password_field = (By.XPATH, "//input[@name='post_password']")
    submit_pass_btn = (By.XPATH, "//input[@value='Nhập']")
    accept_cookies_btn = (By.XPATH, "//input[@value='Đồng ý']")
    chap_title = "entry-title"
    chap_content = "entry-content"
    password_1 = "tuetuetruongtuongkien"
    password_2 = "BaibenuongdaU"
    # password_3 = "16082008"
    chap_locators = (By.XPATH, "//div[@class='entry-content']//a[contains(text(), 'Chương ')]")

class nguoi_den_tu_bong_toi_tang_gioi:
    chap_url_list = (By.XPATH, "//div[@class='post-content clear']//p//a[@target='_blank']")
    cur_title = "post-title entry-title"
    cur_content = "post-content clear"
    accept_cookies_btn = (By.XPATH, "//input[@value='Đồng ý']")
    is_content_img = (By.XPATH, "//div[@class='post-content clear']//img")

class chi_yeu_minh_anh:
    title = "entry-title"
    content = "entry-content"
    is_content_img = (By.XPATH, "//div[@class='entry-content']//img")
    chap_gioi_thieu = (By.XPATH, "//div[@class='entry-content']//p[@align='center'][6]//a")
    chap_1_2 = (By.XPATH, "//div[@class='entry-content']//p[@align='center'][7]//a[contains(text(), 'Chương')]")
    chap_3_to_6 = (By.XPATH, "//div[@class='entry-content']//p[@align='center'][8]//a[contains(text(), 'Chương')]")
    chap_7_to_11 = (By.XPATH, "//div[@class='entry-content']//p[@align='center'][9]//a[contains(text(), 'Chương')]")
    chap_12_to_14 = (By.XPATH, "//div[@class='entry-content']//p[@align='center'][10]//a[contains(text(), 'Chương')]")
    chap_15_16 = (By.XPATH, "//div[@class='entry-content']//p[@align='center'][11]//a[contains(text(), 'Chương')]")
    chap_17_18 = (By.XPATH, "//div[@class='entry-content']//p[@align='center'][12]//a[contains(text(), 'Chương')]")
    chap_19_to_63 = "//div[@class='entry-content']//p//a[contains(text(), 'Chương INPUT')]"
    chap_ = "//div[@class='entry-content']//p//span[contains(text(), 'Chương INPUT')]/../../a"

class cho_hoang_va_xuong:
    title = "chapter-title"
    content = "chapter-content"
    close_ads_btn = (By.XPATH, "//span[contains(text(), 'Close')]")
    next_chap = (By.XPATH, "//div[@class='chapter-button'][1]//a[@class='nextChapter']")

class hoa_hon:
    body_part = (By.CSS_SELECTOR, "#story-reading")
    parts = (By.CSS_SELECTOR, ".panel-reading pre")

