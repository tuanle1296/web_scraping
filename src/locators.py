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
    header : tuple[By, str] = (By.CSS_SELECTOR, ".entry-title")
    content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")
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
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")

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

@dataclass()
class doi_em_tro_ve_se_noi_yeu_em:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass()
class bon_thang_yeu_chua_du:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, ".book-nav ul.menu")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.page-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.content.gs-book")

@dataclass()
class thich:
    chap_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h2.post-title")

@dataclass()
class bay_nam_van_ngoanh_ve_phuong_bac:
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".post-content.clear")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")

@dataclass
class hao_mon_kinh_mong_99_ngay_lam_co_dau:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div#list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")

@dataclass
class thuyen_cua_tay_giang_cuu_nguyet_hi:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class canh_dong_hoang_vu:
    chap_list : tuple[By, str] = (By.XPATH, "//a[contains(text(), 'Chương')]")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")
    password_input_field : tuple[By, str] = (By.CSS_SELECTOR, "input[name='post_password']")
    password_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "input[name='Submit']")

@dataclass
class banh_rang:
    chap_list : tuple[By, str] = (By.XPATH, "//a[contains(text(), 'Chương')]")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")

@dataclass
class ngo_cu_tinh_sau:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, ".mvd-san-pham-show-danh-sach-chuong")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".mdv-san-pham-detail-chuong-title-text")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".msv-khung-truyen-noi-dung.doc-quyen")
    password_input_field : tuple[By, str] = (By.CSS_SELECTOR, ".password-input")
    password_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "button.password-submit-btn")

@dataclass
class trang_sang_ngan_van_dam:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "figure.wp-block-table.is-style-stripes")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h2.wp-block-post-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass
class sa_doa:
    chapter_list_button : tuple[By, str] = (By.XPATH, "//button[@role='tab' and contains(text(), 'Danh sách chương')]")
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "a.p-2")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.text-2xl")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.bg-white.p-6")

@dataclass()
class doa_hoa_toi_loi:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class lo_hen_cung_xuan:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "figure.wp-block-table.is-style-stripes")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")
    password_input_field : tuple[By, str] = (By.CSS_SELECTOR, "input[name='post_password']")
    password_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "input[name='Submit']")

@dataclass
class bo_tat_dien:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "figure.wp-block-table.is-style-stripes")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass
class jolina_land:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.container")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass()
class dam_lay_mua_xuan:
    header : tuple[By, str] = (By.CSS_SELECTOR, "h2.wp-block-post-title")
    content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")
    list_chap : tuple[By, str] = (By.CSS_SELECTOR, "p.has-text-align-center")
    chap_tag : tuple[By, str] = (By.TAG_NAME, "a")

@dataclass
class co_huong_thao:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")

@dataclass
class mot_ngay_mua:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")

@dataclass
class dau_tay:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "p[style='text-align:center']")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")
    password_input_field : tuple[By, str] = (By.CSS_SELECTOR, "input[name='post_password']")
    password_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "input[name='Submit']")

@dataclass()
class than_mat_khang_khit:
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "p.has-text-align-center")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    password_input_field : tuple[By, str] = (By.CSS_SELECTOR, "input[name='post_password']")
    password_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "input[name='Submit']")

@dataclass
class sac_mau_hon_nhan:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div#chapter-list")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.truyen")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-title")

@dataclass
class sac_mau_am:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div#chapter-list")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.truyen")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-title")

@dataclass
class khach_tro:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "li.name-breadcum")
    password_input_field : tuple[By, str] = (By.CSS_SELECTOR, "input#passwordInput")
    password_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "button[type='submit']")

@dataclass
class say_dam:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")
    password_input_field : tuple[By, str] = (By.CSS_SELECTOR, "input[name='post_password']")
    password_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "input[name='Submit']")

@dataclass()
class nguoi_dep_mau_lua:
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "p.has-text-align-center")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")

@dataclass
class bien_thoi_gian:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "figure.wp-block-table")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass
class tinh_cam_sau_nang:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.row.book-list.list-chap")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "div.rv-chapt-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class mua_he_hoang_da:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div#result-danh-sach-chuong")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".mdv-san-pham-detail-chuong-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div#noi_dung_truyen")

@dataclass()
class binh_minh_mau_do:
    header : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")
    list_chap : tuple[By, str] = (By.CSS_SELECTOR, "p.has-text-align-center")
    chap_tag : tuple[By, str] = (By.TAG_NAME, "a")

@dataclass()
class hoang_hon_mong_manh:
    header : tuple[By, str] = (By.CSS_SELECTOR, ".page-title")
    content : tuple[By, str] = (By.CSS_SELECTOR, "div.content.gs-book")
    list_chap : tuple[By, str] = (By.CSS_SELECTOR, ".book-nav ul.menu")
    chap_tag : tuple[By, str] = (By.TAG_NAME, "a")

@dataclass()
class tinh_yeu_chet_tiet_nay:
    header : tuple[By, str] = (By.CSS_SELECTOR, ".wp-block-post-title")
    content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")
    list_chap : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    chap_tag : tuple[By, str] = (By.TAG_NAME, "a")

@dataclass
class cuc_han_tren_bien:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "figure.wp-block-table.is-style-stripes")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass()
class cuc_non_trong_tam_mat:
    header : tuple[By, str] = (By.CSS_SELECTOR, ".wp-block-post-title")
    content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")
    list_chap : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    chap_tag : tuple[By, str] = (By.TAG_NAME, "a")

@dataclass
class xuan_muon:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "figure.wp-block-table")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.wp-block-post-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass
class dong_tam_vi_em:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div#result-danh-sach-chuong")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".mdv-san-pham-detail-chuong-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div#noi_dung_truyen")

@dataclass
class tinh_yeu_cua_chung_ta:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")
    password_input_field : tuple[By, str] = (By.CSS_SELECTOR, "input[name='post_password']")
    password_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "input[name='Submit']")

@dataclass
class ngay_doc_lap_cua_toi:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "figure.wp-block-table")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.wp-block-post-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass
class that_hon:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass
class hoa_hong_ky_uc:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div#tab_mucluc2 div.widget.category")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div#chuong_content")

@dataclass
class hanh_phuc_la_khi_yeu_anh:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass
class the_gioi_tang_em_cho_anh:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "figure.wp-block-table")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass
class phuong_nam_co_cay_cao:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")

@dataclass
class anh_biet_gio_den_tu_dau:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass
class nam_thu_hai_sau_khi_ket_hon:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.mvd-san-pham-show-dsc-content")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".mdv-san-pham-detail-chuong-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div#noi_dung_truyen")

@dataclass
class den_sang_khi_nguoi_den:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass
class toa_thanh_tren_khong:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, ".mvd-san-pham-show-dsc-content-box")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".mdv-san-pham-detail-chuong-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div#noi_dung_truyen")

@dataclass
class hoa_baby:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass
class nui_non_hai_duong:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, ".mvd-san-pham-show-dsc-content-box")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".mdv-san-pham-detail-chuong-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div#noi_dung_truyen")

@dataclass
class chi_yeu_minh_em:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass
class thien_huong_nguoi_mu:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.wp-block-group.has-text-color")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass
class chi_la_da_nghiem_tuc_voi_em:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "figure.wp-block-table.is-style-stripes")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass
class sao_tren_troi_rat_xa_sao_cua_anh_that_gan:
    next_chap_btn : tuple[By, str] = (By.CSS_SELECTOR, "div#chapter-nav-top a#next_chap")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.truyen-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class em_thay_nui_xanh:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass
class than_linh:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div#chapter-list")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.truyen")

@dataclass
class anh_sang_nhat:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass
class em_la_tat_ca_nhung_gi_anh_khao_khat:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.post-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.post-content")

@dataclass
class cm_anh_duong:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content div")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-body")

@dataclass
class minh_nguyet_lac_nga_hoai:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass
class phung_thanh:
    next_chap_btn : tuple[By, str] = (By.CSS_SELECTOR, "div#chapter-nav-top a#next_chap")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass()
class troi_dat_tac_thanh:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, ".book-nav ul.menu")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.page-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.content.gs-book")

@dataclass
class dau_the_nao_cung_muon_o_ben_nhau:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass
class mr_da_dieu_cua_toi:
    next_chap_btn : tuple[By, str] = (By.CSS_SELECTOR, "div#story-part-navigation")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.h2")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.panel.panel-reading")
    footer : tuple[By, str] = (By.CSS_SELECTOR, "div#footer")

@dataclass
class coc_tra_hoa_mua_ha:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "figure.wp-block-table.is-style-stripes")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass
class doan_tau_trong_suong_mu:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "figure.wp-block-table.is-style-stripes")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h2.wp-block-post-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.wp-block-group.has-text-align-justify")
    password_input_field : tuple[By, str] = (By.CSS_SELECTOR, "input[name='post_password']")
    password_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "input[name='Submit']")

@dataclass()
class cam_do_chi_mang:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, ".book-nav ul.menu")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.page-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.content.gs-book")

@dataclass()
class cuoc_chien_chinh_doat:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, ".book-nav ul.menu")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.page-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.content.gs-book")

@dataclass
class hon_ca_hon_nhan:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, ".mvd-san-pham-show-dsc-content-box")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".mdv-san-pham-detail-chuong-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div#noi_dung_truyen")
    signin_signup_link : tuple[By, str] = (By.CSS_SELECTOR, ".hydrosite-mong-truyen-user-text")
    username_signin_field : tuple[By, str] = (By.CSS_SELECTOR, "input[name='username']")
    password_signin_field : tuple[By, str] = (By.CSS_SELECTOR, "input[name='password']")
    signin_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "input[name='dangnhap']")   
    password_input_field : tuple[By, str] = (By.CSS_SELECTOR, "input.password-input")
    password_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "button#btnSubmitPassword")

@dataclass
class anh_trang_roi_vao_be_tinh:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.wp-block-columns p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")
    password_input_field : tuple[By, str] = (By.CSS_SELECTOR, "input[name='post_password']")
    password_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "input[name='Submit']")

@dataclass
class nguoi_tinh_tri_mang:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.post-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.post-content")

@dataclass
class hao_mon_kinh_mong_2:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h2.font-weight-normal")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class cai_thuoc:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class tro_ve_phuong_bac:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, ".wp-block-query")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")

@dataclass
class troi_sang_roi_noi_tam_biet:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class nguoi_den_tu_bong_toi:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.post-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.post-content")

@dataclass
class dong_long:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")

@dataclass
class chiec_coi_trang:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.post-content h4")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.post-content")

@dataclass
class tro_choi_tim_kiem_tinh_yeu:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class trong_mat_anh_co_ngoi_sao:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class gio_xuan_ruc_lua:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class du_am_van_con_thoang_ben_tai:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")

@dataclass
class hon_dao_ke_tiep:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class non_xanh_van_o_day:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class doi_mua_tanh:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")

@dataclass
class hanh_phuc_khong_ban_khong_trung_bia:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class choi_mat:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class nu_hon_cuu_roi:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.row.book-list.list-chap")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "div.rv-chapt-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class dem_dai_o_bac_dao:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class chan_troi_goc_be:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class da_do:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "figure.wp-block-table")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass
class tieu_khanh:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class nguyen_anh_cuoi_khi_dang_do_tai_hoa:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class canh_bac_tinh_yeu:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class do_quyen_khong_tan:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")

@dataclass
class sinh_do:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class son_nam_hai_bac:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class anh_den_trong_con_mua_hoa_mua_ha:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class neu_chi_la_thoang_qua:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class nghiem_tuc_ho_nhao:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class tam_giac_mua_he:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")
    img_tag : tuple[By, str] = (By.TAG_NAME, "img")

@dataclass
class tron_kiep_yeu:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class thu_kinh:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class cay_o_liu_mau_trang:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class tinh_bien:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div#chapter-list")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.truyen")

@dataclass
class ao_mu_chinh_te:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div#result-danh-sach-chuong")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".mdv-san-pham-detail-chuong-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div#noi_dung_truyen")

@dataclass
class pham_ca:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class gon_gio_dem:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.row.book-list.list-chap")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "div.rv-chapt-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class yen_lang_cho_ba_bua_com:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div#chapter-list")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.truyen")

@dataclass
class hai_sao_1:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class hai_sao_2:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class hai_sao_3:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class em_o_ben_ai_cung_la_khoang_trong_trong_anh:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class mua_xuan_o_can_nha_cu:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class em_la_anh_sang_cua_doi_anh:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class cam_on_em_da_dung_cam_yeu_anh:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class thuat_doc_tam:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class pho_dai:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class nguyen_tran_an_tinh:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class muc_tieu_cua_toi_dinh_menh_cua_toi:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class mat_ba_dao:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class coi_xay_gio_mau_xanh:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class ngay_mai_van_con_yeu_em:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div#result-danh-sach-chuong")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".mdv-san-pham-detail-chuong-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div#noi_dung_truyen")

@dataclass
class dau_xuan_tuoi_sang:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class chay_bong:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class tron_thoat_duoi_day_bien:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")

@dataclass
class dau_lau_hoa_hong:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")

@dataclass
class bien_ca_duoi_troi_sao:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "figure.wp-block-table.is-style-stripes")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-body")

@dataclass
class uoc_hen_thanh_son:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class gon_song_khong_ten:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.mvd-san-pham-show-dsc-content")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".mdv-san-pham-detail-chuong-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div#noi_dung_truyen")

@dataclass
class em_la_doi_canh_cua_anh:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class neu_nhu_anh_trang_khong_om_lay_em:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class gia_bo:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class me_tinh_berlin:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")

@dataclass
class duong_ve:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class khong_biet_sao_yeu_em:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")

@dataclass
class vung_trom_khong_the_giau:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div#result-danh-sach-chuong")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".mdv-san-pham-detail-chuong-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div#noi_dung_truyen")

@dataclass
class huou_lac_loi:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div#result-danh-sach-chuong")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".mdv-san-pham-detail-chuong-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div#noi_dung_truyen")

@dataclass
class khong852:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div#result-danh-sach-chuong")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".mdv-san-pham-detail-chuong-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div#noi_dung_truyen")

@dataclass
class nam_ay_gap_duoc_anh:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class quy_loc:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")
    password_input_field : tuple[By, str] = (By.CSS_SELECTOR, "input[name='post_password']")
    password_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "input[name='Submit']")

@dataclass
class mua_xuan_den_muon:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div#result-danh-sach-chuong")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".mdv-san-pham-detail-chuong-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div#noi_dung_truyen")

@dataclass
class nhiet_do_co_the_cua_ac_ma:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class phon_gian:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class gio_nam_va_hoa_hong:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class thoi_gian_nhu_hen:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")

@dataclass
class mot_ngan_tam_tram_ngay:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class cau_chuyen_ve_em:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class loi_hua_cua_anh_la_bien_xanh_cua_em:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div#result-danh-sach-chuong")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".mdv-san-pham-detail-chuong-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div#noi_dung_truyen")

@dataclass
class cau_chuyen_ngay_xuan:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class gia_vo_khong_quan_tam:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class duc_phat_va_nang:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class co_chay_dang_troi:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class dung_khi_de_yeu:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class chi_muon_thuong_anh_chieu_anh_nuoi_anh:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class nghe_noi_em_thich_toi:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class mot_toa_thanh_dang_cho_anh:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.row.book-list.list-chap")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "div.rv-chapt-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class loi_keo:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class nghe_loi_anh_nhat:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class mac_phu_han_ha:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class o_lai_trong_long_anh:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.container")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass
class chi_ngoan_voi_em:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")
    password_input_field : tuple[By, str] = (By.CSS_SELECTOR, "input[name='post_password']")
    password_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "input[name='Submit']")

@dataclass()
class tram_quang_theo_huong_nam:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, ".book-nav ul.menu")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.page-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.content.gs-book")

@dataclass
class quan_hon_cung_co_ai:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.row.book-list.list-chap")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "div.rv-chapt-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class hoa_hong_tien_sinh:
    next_chap_btn : tuple[By, str] = (By.CSS_SELECTOR, "div#gotochap a.next")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.truyen")

@dataclass
class qua_ngot_nam_thang:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div#result-danh-sach-chuong")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".mdv-san-pham-detail-chuong-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div#noi_dung_truyen")

@dataclass
class tham_luyen:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")

@dataclass
class em_chi_thich_mat_cua_anh:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")

@dataclass
class tam_hoa:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class luoi_dao_diu_dang:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div#result-danh-sach-chuong")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".mdv-san-pham-detail-chuong-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div#noi_dung_truyen")

@dataclass
class thoi_nien_thieu:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class ca_voi_co_don:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class nghe_noi_chu_yeu_loli:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class xuan_ha_thu_dong_roi_lai_xuan:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class may_bay_qua_troi_em_qua_tim_toi:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content h4")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")

@dataclass
class cap_doi_nong_chay:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")

@dataclass
class phu_hieu_em_la_cua_anh:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div#result-danh-sach-chuong")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".mdv-san-pham-detail-chuong-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div#noi_dung_truyen")

@dataclass
class anh_tren_trang_giay:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.row.book-list.list-chap")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "div.rv-chapt-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class cung_chieu_doc_nhat:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")

@dataclass
class hon_nhan_da_qua:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass()
class cho_hoang_va_xuong:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass()
class le_ngot:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class to_tinh:
    chap_list : tuple[By, str] = (By.XPATH, "//div[@class='book-list story-details list-chap']")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "div.rv-chapt-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class tan_hon:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p[class='has-text-align-center wp-block-paragraph']")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")

@dataclass
class o_chan_co_ay_rat_mem_mai:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p[class='has-text-align-center wp-block-paragraph']")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")
    
@dataclass()
class nhuoc_xuan_va_canh_minh:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass()
class om_em_di_diep_tu_vien:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass()
class guc_truoc_diu_dang:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass()
class trai_tim_thieu_nu:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class bat_em_vao_trong:
    accept_warning_btn : tuple[By, str] = (By.CSS_SELECTOR, "div.gioi-han-do-tuoi-warning-box a.gioi-han-do-tuoi-btn-continue")
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, ".mvd-san-pham-show-dsc-content-box")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, ".mdv-san-pham-detail-chuong-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div#noi_dung_truyen")
    signin_signup_link : tuple[By, str] = (By.CSS_SELECTOR, ".hydrosite-mong-truyen-user-text")
    username_signin_field : tuple[By, str] = (By.CSS_SELECTOR, "input[name='username']")
    password_signin_field : tuple[By, str] = (By.CSS_SELECTOR, "input[name='password']")
    signin_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "input[name='dangnhap']")   
    password_input_field : tuple[By, str] = (By.CSS_SELECTOR, "input.password-input")
    password_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "button#btnSubmitPassword")

@dataclass()
class vo_nho_mang_thai_ho_cua_dai_thuc:
    next_chap_btn : tuple[By, str] = (By.CSS_SELECTOR, "div#chapter-nav-top a#next_chap")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass()
class bup_be_sua_cua_diep_thieu_gia:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "div.text-center h2")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.c-content")

@dataclass()
class chong_gia_vo_tre:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass()
class hoa_hong_som_mai:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class em_chi_minh_anh_nuong_chieu_thoi:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.row.book-list.list-chap")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "div.rv-chapt-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")
    
@dataclass
class hom_qua_vui_ve:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content")
    password_input_field : tuple[By, str] = (By.CSS_SELECTOR, "input[name='post_password']")
    password_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "input[name='Submit']")

@dataclass()
class roi_vao_ngan_ha:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass()
class ngoc_lua_vang:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass()
class vi_gio_o_noi_ay:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass()
class gio_dang_noi_dau:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "ul.list-chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "a.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-c")

@dataclass
class buoc_vao_giac_mong_ca_vang:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "figure.wp-block-table")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")

@dataclass
class xin_em_o_lai_ben_anh:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "div.chapter-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, "div.truyen")

@dataclass
class cung_em_ngam_sao:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p[class='has-text-align-center wp-block-paragraph']")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")
    password_input_field : tuple[By, str] = (By.CSS_SELECTOR, "input[name='post_password']")
    password_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "input[name='Submit']")

@dataclass
class mot_dong_xu:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "div.entry-content p")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")
    password_input_field : tuple[By, str] = (By.CSS_SELECTOR, "input[name='post_password']")
    password_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "input[name='Submit']")

@dataclass
class chech_huong:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "figure.wp-block-table")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")
    age_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "button.age-gate__submit--yes")

@dataclass
class danh_gia_kem:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "figure.wp-block-table")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")
    age_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "button.age-gate__submit--yes")

@dataclass
class ban_cong:
    chap_list : tuple[By, str] = (By.CSS_SELECTOR, "figure.wp-block-table")
    a_tag : tuple[By, str] = (By.TAG_NAME, "a")
    chapter_title : tuple[By, str] = (By.CSS_SELECTOR, "h1.entry-title")
    chapter_content : tuple[By, str] = (By.CSS_SELECTOR, ".entry-content")
    age_submit_btn : tuple[By, str] = (By.CSS_SELECTOR, "button.age-gate__submit--yes")