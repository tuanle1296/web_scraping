import sys
import os
import threading
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.seleniumbase_functions import *
from src.locators import gon_song_khong_ten as lo


# def crawl_worker(chapter_data, folder_name):
#     """
#     Worker function to process a chunk of chapters.
#     chapter_data: list of tuples (url, chapter_number)
#     """
#     crawl = base(False)
#     try:
#         crawl.create_folder(folder_name)
#     except:
#         pass
    
#     for chap_url, chap_num in chapter_data:
#         print(f"Crawling: {chap_url}")
#         crawl.go_to_webpage(chap_url)
#         crawl.sleep(5)
#         crawl.wait_for_page_load(10)
#         title = crawl.get_element_text(lo.chapter_title)
#         content = crawl.get_element_text(lo.chapter_content)
#         crawl.add_text_to_doc_file(title, content, "chapter_" + str(chap_num))


def main(folder_name):
    print("=======Create folder=======")
    crawl = base(False)
    try:
        crawl.create_folder(folder_name)
        print("=======Created folder successfully======")
    except Exception as e:
        print(f"Error creating folder: {e}")

    # chapters_list = []

    for i in range (1, 92):
        main_url = f"https://lantruyen.vn/gon-song-khong-ten-9833.html?chuong={i}"
        crawl.go_to_webpage("https://www.google.com")
        crawl.wait_for_page_load()
        crawl.go_to_webpage(main_url)
        # crawl.wait_for_page_load(5)
        source = crawl.get_page_source()
        soup = BeautifulSoup(source, 'html.parser')

        # source = crawl.get_page_source()
        # soup = BeautifulSoup(source, 'html.parser')

        # # 3. Find your element (using the CSS selector we discussed earlier)
        title = soup.select_one(lo.chapter_title[1])
        title_text = title.get_text(separator='\n', strip=True)
        content = soup.select_one(lo.chapter_content[1])
        content_text = content.get_text(separator='\n', strip=True)
        
        # title = crawl.get_element_text(lo.chapter_title)
        # content = crawl.get_element_text(lo.chapter_content)
        crawl.add_text_to_doc_file(title_text, content_text, "chapter_" + str(i))
    
    crawl.quit_driver()

    # crawl.go_to_webpage(main_url)
    # chap_list = crawl.find_elements(lo.chap_list)
    # for chap in chap_list:
    #     anchors = crawl.find_elements(lo.a_tag, chap)
    #     for anchor in anchors:
    #         chapters_list.append(crawl.get_attribute_from_element(anchor, "href"))
    # crawl.quit_driver()  # Close the initial driver

    # # Prepare data: list of (url, chapter_number)
    # indexed_chapters = []
    # for i, url in enumerate(chapters_list):
    #     indexed_chapters.append((url, i + 1))

    # Split into chunks for parallel processing
    # Careful when increasing number of threads, some page might be broken
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
    # print("=======All threads finished=======")

if __name__ == '__main__':
    main("gon_song_khong_ten")

'''Note: run this code using cmd: uv run test/gon_song_khong_ten.py'''
