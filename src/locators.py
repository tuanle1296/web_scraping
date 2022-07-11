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
