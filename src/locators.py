from selenium.webdriver.common.by import By


class xiao_link:
    next_btn = (By.XPATH, "//a[@rel='next']")
    cur_title = 'entry-title'
    cur_content = 'entry-content'
    is_content_img = (By.XPATH, "//div[@class='entry-content']//img")
