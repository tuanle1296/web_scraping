import sys
import os
import threading
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.locators import vo_nho_mang_thai_ho_cua_dai_thuc as lo

# def crawl_worker(chapter_data, folder_name):
#     """
#     Worker function to process a chunk of chapters.
#     chapter_data: list of tuples (url, chapter_number)
#     """
#     crawl = base()
#     try:
#         crawl.create_folder(folder_name)
#     except:
#         pass
#     crawl.quit_driver()
    
#     failed_chapters = []
#     for chap_url, chap_num in chapter_data:
#         try:
#             print(f"Crawling: {chap_url}")
#             soup = crawl.crawl_data(chap_url)
#             if soup:
#                 title = crawl.crawl_text_from_soup(soup, lo.chapter_title[1])
#                 content = crawl.crawl_text_from_soup(soup, lo.chapter_content[1])
#                 crawl.add_text_to_doc_file(title, content, "chapter_" + str(chap_num))
#         except Exception as e:
#             failed_chapters.append((chap_url, chap_num))
#             print(f"====== Warning: Error crawling {chap_url}", e)

#     if failed_chapters:
#         print(f"Failed chapters in this worker: {failed_chapters}")



def main(folder_name):
    print("=======Create folder=======")
    crawl = base(False)
    try:
        crawl.create_folder(folder_name)
        print("=======Created folder successfully======")
    except Exception as e:
        print(f"Error creating folder: {e}")

    # chapters_list = []
    # for i in range (1, 3):
    main_url = "https://truyencom.com/vo-nho-mang-thai-ho-cua-dai-thuc/chuong-35.html"
    
    crawl.go_to_webpage(main_url)
    crawl.wait_for_page_load(10)
    status = True
    index = 35
    while status:
        
        crawl.wait_for_page_load(10)
        crawl.sleep(3)
        title = crawl.get_element_text(lo.chapter_title)
        content = crawl.get_element_text(lo.chapter_content)
        current_url = crawl.get_current_url()
        print(f"Crawling: {current_url}")
        # file_name = current_url.split('/')[-1].split('.')[0]
        crawl.add_text_to_doc_file(title, content, "chapter_" + str(index))

        class_attribute = crawl.get_attribute_from_element(lo.next_chap_btn, "class")
        if "disabled" in class_attribute:
            status = False
        else:
            crawl.click_element(lo.next_chap_btn)
            index += 1
    
    crawl.quit_driver()  # Close the initial driver
    
    #     chap_list = crawl.find_elements(lo.chap_list)
    #     for chap in chap_list:
    #         anchors = crawl.find_elements(lo.a_tag, chap)
    #         for anchor in anchors:
    #             chapters_list.append(crawl.get_attribute_from_element(anchor, "href"))
    # crawl.quit_driver()  # Close the initial driver

    # # Prepare data: list of (url, chapter_number)
    # indexed_chapters = []
    # for i, url in enumerate(chapters_list):
    #     indexed_chapters.append((url, i + 1))

    # # Split into chunks for parallel processing
    # # Careful when increasing number of threads, some page might be broken
    # num_threads = 3  # Adjust number of threads as needed
    # chunk_size = math.ceil(len(indexed_chapters) / num_threads)
    # chunks = [indexed_chapters[i:i + chunk_size] for i in range(0, len(indexed_chapters), chunk_size)]

    # threads = []
    # print(f"Starting {len(chunks)} threads...")
    # for chunk in chunks:
    #     t = threading.Thread(target=crawl_worker, args=(chunk, folder_name))
    #     threads.append(t)
    #     t.start()

    # for t in threads:
    #     t.join()
    print("=======All threads finished=======")

if __name__ == '__main__':
    main("vo_nho_mang_thai_ho_cua_dai_thuc_2")

'''Note: run this code using cmd: uv run test/vo_nho_mang_thai_ho_cua_dai_thuc.py'''