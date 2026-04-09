import sys
import os
import threading
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.locators import cm_anh_duong as lo

def crawl_worker(chap_data, folder_name):
    
    crawl = base()
    try:
        crawl.create_folder(folder_name)
    except:
        pass
    finally:
        crawl.set_path(folder_name)
    
    try:
    
        for chap_url, chap_num in chap_data:
            try:
                print(f"Crawling: {chap_url}")
                
                # Dùng hàm crawl_data (BS4/Requests) của bạn
                soup = crawl.crawl_data(chap_url)
                if soup:
                    title = crawl.crawl_text_from_soup(soup, lo.chapter_title[1])
                    content = crawl.crawl_text_from_soup(soup, lo.chapter_content[1])
                    
                    crawl.add_text_to_doc_file(title, content, "chapter_" + str(chap_num))
                    return f"Complete chapter: {chap_num}"
                else:
                    return f"Failed to crawl chapter: {chap_num}"

            except Exception as e:
                print(f"====== Warning: Error crawling {chap_url}: {e}")
                return f"Error while crawling chapter: {chap_num}"
            
    finally:
        crawl.quit_driver()


def main(folder_name):
    print("======= Khởi tạo và gom link =======")
    crawl = base(False) # Mở trình duyệt có giao diện để gom link nếu cần
    
    try:
        crawl.create_folder(folder_name)
        print("======= Tạo folder thành công ======")
    except Exception as e:
        print(f"An error occurred while creating folder: {e}")

    chapters_list = []
    forbidden_words = ["tuy-tien-phong", "rat-nho-rat-nho", "facebook", "tac-gia", "twitter"]

    try:
        main_url = "https://truyen3d.wordpress.com/2017/01/05/1-cm-anh-duong-mac-bao-phi-bao/"
        crawl.go_to_webpage(main_url)
        crawl.wait_for_page_load(10)
        
        chap_list = crawl.find_elements(lo.chap_list)
        
        for chap in chap_list:
            anchors = crawl.find_elements(lo.a_tag, chap)
            for anchor in anchors:
                url = crawl.get_attribute_from_element(anchor, "href")
                
                # Lọc link chuẩn
                if url and not any(word in url for word in forbidden_words) and (url not in chapters_list):
                    chapters_list.append(url)
                    
    finally:
        crawl.quit_driver()  # Gom link xong thì đóng ngay trình duyệt của hàm main

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
    main("1cm_anh_duong")

'''Note: run this code using cmd: uv run test/1cm_anh_duong.py'''