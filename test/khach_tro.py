import sys
import os
import threading
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.base_functions import *
from src.locators import khach_tro as lo


def crawl_worker(chapter_data, folder_name):
    """
    Worker function to process a chunk of chapters.
    chapter_data: list of tuples (url, chapter_number)
    """
    with Base(False) as crawl:
        try:
            crawl.create_folder(folder_name)
        except:
            pass
    


    failed_chapters = []
    password = ""
    crawl.maximize_browser()
    for chap_url, chap_num in chapter_data:
        try:
            if (chap_num <= 100):
                password = "1"
            else:
                password = "2"

            print(f"Crawling: {chap_url}")
            
            crawl.go_to_webpage(chap_url)
            crawl.wait_for_page_load(10)
            crawl.sleep(3)

            if crawl.is_element_visible(lo.password_input_field):
                crawl.input_text(lo.password_input_field, password)
                crawl.sleep(2)
                crawl.click_element(lo.password_submit_btn, force_js=True)
                crawl.wait_for_page_load(10)
                # crawl.sleep(2)

                crawl.sleep(3)


            crawl.wait_for_element_visible(lo.chapter_content, timeout=10)
            # crawl.sleep(3)

            print("Extracting text...")
            title = crawl.get_element_text(lo.chapter_title, extract_hidden=False)
            content = crawl.get_element_text(lo.chapter_content, extract_hidden=False)
            crawl.add_text_to_doc_file(title, content, "chapter_" + str(chap_num))

            crawl.sleep(3)

        except Exception as e:
            failed_chapters.append((chap_url, chap_num))
            print(f"====== Warning: Error crawling {chap_url}", e)

    if failed_chapters:
        print(f"Failed chapters in this worker: {failed_chapters}")
    
    crawl.quit_driver()




def main(folder_name):
    print("=======Create folder=======")
    with Base(False) as crawl:
        try:
            crawl.create_folder(folder_name)
            print("=======Created folder successfully======")
        except Exception as e:
            print(f"Error creating folder: {e}")

        chapters_list = []
        for i in range (1, 5):
            main_url = f"https://trichtinhlau.com/xem-truyen/khach-tro?page={i}"
    
            crawl.go_to_webpage(main_url)
            crawl.wait_for_page_load(10)
            crawl.sleep(3)
            chap_list = crawl.find_elements(lo.chap_list)
            for chap in chap_list:
                anchors = crawl.find_elements(lo.a_tag, chap)
                for anchor in anchors:
                    chapters_list.append(crawl.get_attribute_from_element(anchor, "href"))

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
    main("khach_tro")

'''Note: run this code using cmd: uv run test/khach_tro.py'''

# def crawl_khach_tro():
#     # 1. Khởi tạo con Bot từ class của bạn (Bật cửa sổ để vượt Cloudflare)
#     print("Đang khởi động trình duyệt...")
#     bot = Base(is_headless_mode=False, timeout=15)

#     try:
#         # 2. Tạo thư mục để lưu file DOCX
#         truyen_ten = "Khach_Tro"
#         bot.create_folder(truyen_ten)
#         print(f"Đã tạo thư mục: {bot.path}")

#         # URL của chương cần cào
#         url = "https://trichtinhlau.com/doc-truyen/khach-tro/chuong-1"
#         print(f"Đang truy cập: {url}")
        
#         # 3. Mở trang web (Dùng hàm của seleniumbase để tự động vượt Cloudflare)
#         bot.driver.uc_open_with_reconnect(url, reconnect_time=4)
        
#         # 4. Chờ phần tử chứa nội dung xuất hiện 
#         # (ID "chapter-c" là chuẩn chung của web truyện mà bạn đã chụp trong ảnh)
#         chuong_locator = (By.CSS_SELECTOR, "div.entry-content")
#         bot.wait_for_element_visible(chuong_locator, timeout=10)
        
#         # 5. Cào Text (Hàm này của bạn đã tự động gọi BeautifulSoup cắt bỏ font-size:0)
#         print("Đang cào nội dung và dọn rác tàng hình...")
#         noi_dung = bot.get_element_text(chuong_locator, extract_hidden=False)
        
#         # --- BỘ LỌC CHỮ QUẢNG CÁO MẠNG XÃ HỘI ---
#         # Loại bỏ các dòng chứa plugin Facebook/X (Twitter) thường nằm cuối truyện
#         garbage_lines = [
#             "Quảng cáo", "Chia sẻ:", "Chia sẻ trên X (Mở trong cửa sổ mới)", 
#             "X", "Chia sẻ lên Facebook (Mở trong cửa sổ mới)", "Facebook", 
#             "Thích", "Đang tải..."
#         ]
#         lines = noi_dung.split('\n')
#         clean_lines = [line for line in lines if line.strip() not in garbage_lines]
#         noi_dung_sach = '\n'.join(clean_lines).strip()

#         # 6. Lưu thành file DOCX bằng hàm bạn đã viết sẵn
#         if noi_dung_sach:
#             ten_file = "Chuong_1"
#             tieude_trong_file = "Chương 1: Vị khách mới"
            
#             bot.add_text_to_doc_file(
#                 title=tieude_trong_file, 
#                 text=noi_dung_sach, 
#                 file_name=ten_file
#             )
#             print(f"Hoàn thành! Đã lưu: {ten_file}.docx")
#         else:
#             print("Cảnh báo: Nội dung cào được đang trống!")

#     except Exception as e:
#         print(f"Lỗi trong quá trình chạy: {e}")
#     finally:
#         # 7. Luôn đóng trình duyệt an toàn
#         bot.quit_driver()
#         print("Đã đóng trình duyệt.")

# if __name__ == "__main__":
#     crawl_khach_tro()