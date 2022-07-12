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
