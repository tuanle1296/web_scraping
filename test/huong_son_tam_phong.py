import sys
import os
import threading
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.locators import huong_son_tam_phong as lo


def crawl_worker(chapter_data, folder_name):
    """
    Worker function to process a chunk of chapters.
    chapter_data: list of tuples (url, chapter_number)
    """
    crawl = base()
    try:
        crawl.create_folder(folder_name)
    except:
        pass
    crawl.quit_driver()  # Close browser immediately as we use API for crawling
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    failed_chapters = []
    for chap_url, chap_num in chapter_data:
        try:
            if (chap_num == 60):
                chap_url = "https://tichhashye.wordpress.com/2025/08/22/chuong-60/"
            print(f"Crawling: {chap_url}")
            response = requests.get(chap_url, headers=headers, timeout=20)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
                title_element = soup.select_one(lo.chapter_title[1])
                content_element = soup.select_one(lo.chapter_content[1])
                
                if title_element and content_element:
                    title = title_element.get_text().strip()
                    content = content_element.get_text(separator='\n', strip=True)
                    crawl.add_text_to_doc_file(title, content, "chapter_" + str(chap_num))
                else:
                    print(f"Elements not found for {chap_url}")
                    failed_chapters.append((chap_url, chap_num))
            else:
                print(f"Page {chap_url} returned status {response.status_code}. Skipping.")
                failed_chapters.append((chap_url, chap_num))
        except Exception as e:
            failed_chapters.append((chap_url, chap_num))
            print(f"====== Warning: Error crawling {chap_url}")
    
    print(f"Failed chapters in this worker: {failed_chapters}")

    crawl.quit_driver()


def main(folder_name):
    print("=======Create folder=======")
    crawl = base(False)
    try:
        crawl.create_folder(folder_name)
        print("=======Created folder successfully======")
    except Exception as e:
        print(f"Error creating folder: {e}")

    main_url = "https://tichhashye.wordpress.com/2025/04/20/hien-dai-huong-son-tam-phong-ung-vu-truc/"
    crawl.go_to_webpage(main_url)
    crawl.wait_for_page_load(10)
    chap_list = crawl.find_elements(lo.chap_list)
    # urls_list = crawl.find_elements(lo.a_tag, chap_list)
    chapters_list = []
    for chap in chap_list:
        anchors = crawl.find_elements(lo.a_tag, chap)
        for anchor in anchors:
            chapters_list.append(crawl.get_attribute_from_element(anchor, "href"))            
    crawl.quit_driver()  # Close the initial driver

    # Prepare data: list of (url, chapter_number)
    indexed_chapters = []
    for i, url in enumerate(chapters_list):
        indexed_chapters.append((url, i + 1))

    # Split into chunks for parallel processing
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
    main("huong_son_tam_phong")

'''Note: run this code using cmd: python3 test/huong_son_tam_phong.py'''
