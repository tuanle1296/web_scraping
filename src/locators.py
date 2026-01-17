from selenium.webdriver.common.by import By
from dataclasses import dataclass

@dataclass
class xiao_link:
    next_btn : tuple[By, str] = (By.XPATH, "//p[@style='text-align:right;']//a")
    cur_title : str = 'entry-title'
    cur_content : str = 'entry-content'
    is_content_img : tuple[By, str] = (By.XPATH, "//div[@class='entry-content']//img")


@dataclass()
class onlytlinh:
    next_chap : str = "//div[@class='entry-content']//a[contains(text(),'Chương INPUT')]"
    next_chap_ngoai : str = "//div[@class='entry-content']//a[contains(text(),'Ngoại truyện INPUT')]"
    cur_title : str = 'entry-title'
    cur_content : str = 'entry-content'
    pass_input_field : tuple[By, str] = (By.XPATH, "//input[@name='post_password']")
    accept_cookies_btn : tuple[By, str] = (By.XPATH, "//div[@class='hide-on-button ads-active']//input[@type='submit']")
    pass_1 : str= "tanthanh"
    pass_2 : str = "SuanNing"
    pass_3 : str = "onlytlinhLuyiningChengxinglin"

@dataclass()
class kethonsailam:
    next_from_1_to_31 : tuple[By, str] = (By.XPATH, "//div[@id='post-navigation']//div[@class='nav-next']")
    content_from_chap_1_to_31 : str = 'entry-inner'
    title_from_chap_1_to_31 : str = 'post-title'
    next_from_32_to_57 : tuple[By, str] = (By.XPATH, "//div[@class='nav-next']")
    title_from_chap_32_to_57 : str = 'entry-title'
    content_from_chap_32_to_57 : str = 'entry-content'
    close_cookies_banner : tuple[By, str] = (By.XPATH, "//form//input[@value='Đồng ý']")
    password_field : tuple[By, str] = (By.XPATH, "//input[@type='password']")
    submit_password_btn : tuple[By, str] = (By.XPATH, "//input[@value='Nhập']")
    password_nt_1_2 : str = "LamThien"
    password_nt_3 : str = "2708"

@dataclass()
class kcnna:
    password_field : tuple[By, str] = (By.XPATH, "//input[@name='post_password']")
    submit_pass_btn : tuple[By, str] = (By.XPATH, "//input[@value='Nhập']")
    accept_cookies_btn : tuple[By, str] = (By.XPATH, "//input[@value='Đồng ý']")
    chap_title : str = "entry-title"
    chap_content : str = "entry-content"
    password_1 : str = "tuetuetruongtuongkien"
    password_2 : str = "BaibenuongdaU"
    # password_3 : str = "16082008"
    chap_locators : tuple[By, str] = (By.XPATH, "//div[@class='entry-content']//a[contains(text(), 'Chương ')]")

@dataclass()
class nguoi_den_tu_bong_toi_tang_gioi:
    chap_url_list : tuple[By, str] = (By.XPATH, "//div[@class='post-content clear']//p//a[@target='_blank']")
    cur_title : str = "post-title entry-title"
    cur_content : str = "post-content clear"
    accept_cookies_btn : tuple[By, str] = (By.XPATH, "//input[@value='Đồng ý']")
    is_content_img : tuple[By, str] = (By.XPATH, "//div[@class='post-content clear']//img")

@dataclass()
class chi_yeu_minh_anh:
    title : str = "entry-title"
    content : str = "entry-content"
    is_content_img : tuple[By, str] = (By.XPATH, "//div[@class='entry-content']//img")
    chap_gioi_thieu : tuple[By, str] = (By.XPATH, "//div[@class='entry-content']//p[@align='center'][6]//a")
    chap_1_2 : tuple[By, str] = (By.XPATH, "//div[@class='entry-content']//p[@align='center'][7]//a[contains(text(), 'Chương')]")
    chap_3_to_6 : tuple[By, str] = (By.XPATH, "//div[@class='entry-content']//p[@align='center'][8]//a[contains(text(), 'Chương')]")
    chap_7_to_11 : tuple[By, str] = (By.XPATH, "//div[@class='entry-content']//p[@align='center'][9]//a[contains(text(), 'Chương')]")
    chap_12_to_14 : tuple[By, str] = (By.XPATH, "//div[@class='entry-content']//p[@align='center'][10]//a[contains(text(), 'Chương')]")
    chap_15_16 : tuple[By, str] = (By.XPATH, "//div[@class='entry-content']//p[@align='center'][11]//a[contains(text(), 'Chương')]")
    chap_17_18 : tuple[By, str] = (By.XPATH, "//div[@class='entry-content']//p[@align='center'][12]//a[contains(text(), 'Chương')]")
    chap_19_to_63 : str = "//div[@class='entry-content']//p//a[contains(text(), 'Chương INPUT')]"
    chap_ : str = "//div[@class='entry-content']//p//span[contains(text(), 'Chương INPUT')]/../../a"

@dataclass()
class cho_hoang_va_xuong:
    title : str = "chapter-title"
    content : str = "chapter-content"
    close_ads_btn : tuple[By, str] = (By.XPATH, "//span[contains(text(), 'Close')]")
    next_chap : tuple[By, str] = (By.XPATH, "//div[@class='chapter-button'][1]//a[@class='nextChapter']")

@dataclass()
class hoa_hon:
    body_part : tuple[By, str] = (By.CSS_SELECTOR, "#story-reading")
    page : tuple[By, str] = (By.CSS_SELECTOR, ".page")
    pre_tage : tuple[By, str] = (By.TAG_NAME, "pre")
    header : tuple[By, str] = (By.CSS_SELECTOR, "header.panel-reading h1")
    part : tuple[By, str] = (By.CSS_SELECTOR, "#parts-container-new")
    story_parts : tuple[By, str] = (By.CSS_SELECTOR, "div [data-testid='toc'] ul[aria-label='story-parts']")
    all_links : tuple[By, str] = (By.CSS_SELECTOR, "a")

@dataclass()
class khi_gio_noi_len:
    header : str = "entry-title"
    content : str = "entry-content"
    list_chap : tuple[By, str] = (By.CSS_SELECTOR, ".has-text-align-center")
    chap_tag : tuple[By, str] = (By.TAG_NAME, "a")

@dataclass()
class chuyen_cu_kinh_cang:
    title_element : tuple[str, str] = ("h1", "entry-title")
    content_element : tuple[str, str] = ("div", "entry-content clear")
    title : str = "title"
    chapter_link : str = "h2.entry-title a[href]"

@dataclass()
class co_truong_cat_canh_di:
    chapter_blocks : tuple[By, str] = (By.XPATH, "//div[@id='TIEU-DE']//span[text()='Mục lục']/../../../..")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    title : tuple[str, str] = ("h1", "entry-title")
    content : tuple[str, str] = ("div", "entry-content")

@dataclass()
class tulip_trong_gio:
    beginning_chapter_block : tuple[By, str] = (By.XPATH, "//strong[text()='Danh sách chương: ']/..")
    endding_chapter_block : tuple[By, str] = (By.XPATH, "p[text()='Hoàn toàn văn.']")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    title : tuple[By, str] = (By.CSS_SELECTOR, ".entry-title")
    content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")
    pass_word_input_field : tuple[By,str] = (By.CSS_SELECTOR, ".post-password-form__input")
    password_submit_button : tuple[By,str] = (By.CSS_SELECTOR, ".post-password-form__submit")

@dataclass()
class cung_anh_di_den_tan_cung_the_gioi:
    chapter_recognization : tuple[By, str] = (By.CSS_SELECTOR, "div.epub-view")
    next_button : tuple[By, str] = (By.CSS_SELECTOR, "i.fas.fa-long-arrow-alt-right")
    story_content : tuple[By, str] = (By.CSS_SELECTOR, "div.calibre")
    iframe : tuple[By, str] = (By.XPATH, "//iframe[contains(@id, 'epubjs-view')]")

@dataclass()
class sau_khi_hon_nhan_tan_vo:
    chap_title : tuple[By, str] = (By.CSS_SELECTOR, ".truyen-title")
    chap_content : tuple[By, str] = (By.CSS_SELECTOR, ".chapter-c")

@dataclass()
class anh_den_hoa_le:
    chap_title : tuple[By, str] = (By.CSS_SELECTOR, ".truyen-title")
    chap_content : tuple[By, str] = (By.CSS_SELECTOR, ".chapter-c")

@dataclass()
class buc_tuong_doi_mat_dau_goi:
    chap_urls_list : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content .wp-block-table")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    password_field : tuple[By, str] = (By.CSS_SELECTOR, "input[type='password']")
    submit_password_btn : tuple[By, str] = (By.CSS_SELECTOR, "input[name='Submit']")
    invalid_password_message : tuple[By, str] = (By.CSS_SELECTOR, ".post-password-form-invalid-password")
    chap_title : tuple[By, str] = (By.CSS_SELECTOR, "h2.wp-block-post-title")
    chap_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass()
class dung_ai_noi_voi_anh_ay_toi_con_yeu:
    chap_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chap_header : tuple[By, str] = (By.CSS_SELECTOR, "header.entry-header")

@dataclass()
class co_chap:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class suong_mo_tren_dao_hong_kong:
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")

    
@dataclass
class ba_nam_roi_lai_ba_nam:
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")

@dataclass
class hao_mon_kinh_mong_3_dung_de_lo_nhau:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    
@dataclass
class huong_son_tam_phong:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "figure.wp-block-table")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")