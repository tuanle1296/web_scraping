import sys
import os
import threading
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.locators import mot_dong_xu as lo

def crawl_worker(chap_data, folder_name):
    """
    Worker xử lý TỪNG CHƯƠNG MỘT thay vì cả cục.
    chap_data: tuple (url, chapter_number)
    """
    
    # Khởi tạo trình duyệt riêng cho từng luồng
    crawl = base()
    passwords = "motdongxu"
    
    crawl.set_path(folder_name)
    for chap_url, chap_num in chap_data:
        try:
            print(f"Crawling: {chap_url}")
            crawl.go_to_webpage(chap_url)
            crawl.wait_for_page_load(10)
            
            if crawl.is_element_visible(lo.password_input_field):
                    print(f"Password field found for Chap {chap_num}. Trying passwords...")
                    crawl.input_text(lo.password_input_field, passwords)
                    crawl.click_element(lo.password_submit_btn)
                    crawl.sleep(5)
                    crawl.wait_for_page_load(10)
                    if crawl.is_element_visible(lo.password_input_field) is False:
                            print(f"Password {passwords} is correct for Chap {chap_num}.") 

            title = crawl.get_element_text(lo.chapter_title)
            content = crawl.get_element_text(lo.chapter_content)
            crawl.add_text_to_doc_file(title, content, "chapter_" + str(chap_num))
            
            return f"Completed chapter: {chap_num}"
            
        except Exception as e:
            print(f"====== Warning: Error crawling {chap_url}: {e}")
            return f"Failed to crawl chapter:{chap_num}"
            
        finally:
            # CHẮC CHẮN 100% TRÌNH DUYỆT SẼ ĐƯỢC ĐÓNG DÙ CÓ LỖI HAY KHÔNG
            crawl.quit_driver()


def main(folder_name):
    print("======= Starting =======")
    crawl = base(False)
    
    try:
        crawl.create_folder(folder_name)
        print("======= Created folder successfully ======")
    except Exception as e:
        print(f"Error while creating folder: {e}")

    chapters_list = []
    
    try:
        main_url = f"https://lamdaunhagau.wordpress.com/hd-dang-edit-mot-dong-xu-quyet-biet/"
        crawl.go_to_webpage(main_url)
        crawl.wait_for_page_load(10)
            
        chap_list = crawl.find_elements(lo.chap_list)
        for chap in chap_list:
            anchors = crawl.find_elements(lo.a_tag, chap)
            for anchor in anchors:
                url = crawl.get_attribute_from_element(anchor, "href")
                
                # Lọc link chuẩn
                if url and (url not in chapters_list):
                    chapters_list.append(url)
    finally:
        crawl.quit_driver()  # Đóng trình duyệt gom link

    # Prepare data: list of (url, chapter_number)
    indexed_chapters = []
    for i, url in enumerate(chapters_list):
        indexed_chapters.append((url, i + 1))

    # Split into chunks for parallel processing
    # Careful when increasing number of threads, some page might be broken
    num_threads = 3  # Adjust number of threads as needed
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
    main("mot_dong_xu")

'''Note: run this code using cmd: uv run test/mot_dong_xu.py'''
