import sys
import os
import threading
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.locators import cung_em_ngam_sao as lo

def crawl_worker(chapter_data, folder_name):
    """
    Worker function to process a chunk of chapters.
    chapter_data: list of tuples (url, chapter_number)
    """
    crawl = base(False)
    try:
        crawl.create_folder(folder_name)
    except:
        pass

    passwords = {
        "32": "topbachuacay",
        "33": "bockhangiayHyundai",
        "34": "lopphogiaitridautay",
        "35": "trangsuavuongtu",
        "36": "DongThuaVonghonbonmuoituoi",
        "37": "ultramanbienhinhPhuongDien",
        "38": "banhtroidao",
        "39": "ngontaycaiGiangTo",
        "40": "daytrangdiem",
        "41": "toabondaihocGiang",
        "42": "KhaLeVitVit",
        "43": "lequockhanhTrinhQuocHoa",
        "44": "cuoithangsau",
        "45": "BacDai",
        "46": "saokim",
        "47": "Bỏ lỡ mất ánh chiều tà rực rỡ, vẫn còn đó một bầu trời đầy sao",
        "48": "307tocngan",
        "49": "haingante",
        "50": "AHoi",
        "51": "haimuoitutuoi",
        "52": "PhoDong",
        "53": "Wei",
        "54": "cotranh",
        "55": "duongchantroi",
        "56": "bocthamtrungthuong",
        "57": "10cm",
        "58": "trasuadaukemcheese",
        "59": "layghechancua",
        "60": "haimuoivante",
        "61": "MinhVan",
        "62": "TayTang",
        "63": "vedunghangsang",
        "64": "muoingante",
        "65": "HenGapLaiNhauNgayHoaNo",
        "66": "aolen",
        "67": "BachNienHaoHop",
        "68": "dienvienmua",
        "69": "becon",
        "70": "phogiaosu",
        "71": "tenhoDuong",
        "72": "honnuanam",
        "73": "muanonbaohiemchobacsiDong",
        "74": "quanbarcualaoTrieu",
        "75": "bonnam",
        "76": "TranTrung",
        "77": "boctomMaoMao",
        "78": "TanTanbaytuoi"
    }

    for chap_url, chap_num in chapter_data:
        
        print(f"Crawling: {chap_url}")
        crawl.go_to_webpage(chap_url)
        crawl.wait_for_page_load(10)

        password = ""
        if crawl.is_element_visible(lo.password_input_field):
            print(f"Password field found for Chap {chap_num}. Trying passwords...")
            for key, value in passwords.items():
                if str(chap_num) == key:
                    password = value
            crawl.input_text(lo.password_input_field, password)
            crawl.click_element(lo.password_submit_btn)
            crawl.sleep(5)
            crawl.wait_for_page_load(10)
            if crawl.is_element_visible(lo.password_input_field) is False:
                    print(f"Password \"{password}\" for Chap \"{chap_num}\".") 
                
        print(f"Crawling: {chap_url}")
        title = crawl.get_element_text(lo.chapter_title)
        content = crawl.get_element_text(lo.chapter_content)

        crawl.add_text_to_doc_file(title, content, "chapter_" + str(chap_num))

    crawl.quit_driver()



def main(folder_name):
    print("=======Create folder=======")
    crawl = base(False)
    try:
        crawl.create_folder(folder_name)
        print("=======Created folder successfully======")
    except Exception as e:
        print(f"Error creating folder: {e}")

    chapters_list = []

    main_url = "https://antinhxoxo.wordpress.com/cung-em-ngam-sao-giao-xuan-binh/"
    
    crawl.go_to_webpage(main_url)
    crawl.wait_for_page_load(10)
    chap_list = crawl.find_elements(lo.chap_list)

    chapters_list = []

    for chap in chap_list:
        anchors = crawl.find_elements(lo.a_tag, chap)
        for anchor in anchors:
            url = crawl.get_attribute_from_element(anchor, "href")
            if url not in chapters_list:
                chapters_list.append(url)  
    crawl.quit_driver()  # Close the initial driver

    # Prepare data: list of (url, chapter_number)
    indexed_chapters = []
    for i, url in enumerate(chapters_list):
        indexed_chapters.append((url, i + 1))

    # Split into chunks for parallel processing
    # Careful when increasing number of threads, some page might be broken
    num_threads = 2  # Adjust number of threads as needed
    chunk_size = math.ceil(len(indexed_chapters) / num_threads)
    chunks = [indexed_chapters[i:i + chunk_size] for i in range(0, len(indexed_chapters), chunk_size)]

    threads = []
    print(f"Starting {len(chunks)} threads...")
    for chunk in chunks:
        t = threading.Thread(target=crawl_worker, args=(chunk, folder_name))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print("=======All threads finished=======")

if __name__ == '__main__':
    main("cung_em_ngam_sao")

'''Note: run this code using cmd: uv run test/cung_em_ngam_sao.py'''