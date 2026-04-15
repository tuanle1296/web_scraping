import sys
import os
import math
import re
import time
import concurrent.futures
from curl_cffi import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *

storyName = "anh_o_phia_nam_dam_may"
main_url = "https://www.wattpad.com/1347858407-full-anh-%E1%BB%9F-ph%C3%ADa-nam-%C4%91%C3%A1m-m%C3%A2y-c%E1%BA%A3nh-h%C3%A0nh-l%E1%BB%9Di-%C4%91%E1%BB%81"


def get_story_toc(start_url):
    """
    Extracts the chapter ID from the URL, finds the parent Story ID, 
    and returns a list of all chapters in the book via Wattpad's API.
    """
    # 1. Extract the starting chapter ID from the URL
    match = re.search(r'wattpad\.com/(\d+)', start_url)
    if not match:
        raise ValueError("Could not find a valid Chapter ID in the provided URL.")
    
    chapter_id = match.group(1)
    print(f"Extracted Starting Chapter ID: {chapter_id}")

    # 2. Get the main Story ID to find the Table of Contents
    part_api = f"https://www.wattpad.com/api/v3/story_parts/{chapter_id}"
    response = requests.get(part_api, impersonate="chrome120")
    
    if response.status_code != 200:
        raise ConnectionError("Failed to fetch Story ID. Cloudflare might be blocking.")
        
    story_id = response.json().get("groupId")
    
    # 3. Get the full list of chapters
    print(f"Fetching Table of Contents for Story ID: {story_id}...")
    story_api = f"https://www.wattpad.com/api/v3/stories/{story_id}?fields=id,title,parts(id,title)"
    story_data = requests.get(story_api, impersonate="chrome120").json()
    
    story_title = story_data.get('title')
    all_chapters = story_data.get('parts', [])
    
    print(f"📚 Found Story: '{story_title}' | 📑 Total Chapters: {len(all_chapters)}")
    return all_chapters


def crawl_worker(chapter_data, folder_name):
    crawl = base(is_headless_mode=True) 
    try:
        crawl.set_path(folder_name)
    except Exception as e:
        print(f"Error while setting folder path: {e}")

    failed_chapters = []
    
    for chapter, chap_num in chapter_data:
        chap_id = chapter['id']
        chap_title = chapter['title']
        
        try:
            print(f"Crawling Chapter {chap_num}: {chap_title}")
            api_url = f"https://www.wattpad.com/apiv2/storytext?id={chap_id}"
            
            # 1. Ask for RAW TEXT
            raw_text = crawl.crawl_data(api_url, return_type="text", impersonate="chrome120")
            
            if raw_text:
                
                # Check if Wattpad accidentally returned JSON
                if raw_text.strip().startswith("{"):
                    import json
                    try:
                        data = json.loads(raw_text)
                        raw_html = data.get("text", raw_text) # Extract the text if it's JSON
                    except json.JSONDecodeError:
                        raw_html = raw_text
                else:
                    raw_html = raw_text

                # 2. Parse the HTML directly (No dummy wrappers!)
                soup = BeautifulSoup(raw_html, "html.parser")
                
                # 3. Apply your cleaning logic DIRECTLY to the entire soup 
                # (No need to use select_one() or locators)
                
                # Clean Anti-scraping spans
                for hidden in soup.find_all('span', style=lambda value: value and 'font-size:0' in value.replace(' ', '')):
                    hidden.decompose()

                # Mark Images
                for img in soup.find_all('img'):
                    src = img.get('src') or img.get('data-src') or img.get('data-original')
                    if src:
                        if src.startswith("//"):
                            src = "https:" + src
                        img.replace_with(f"\n[IMAGE_MARKER_START]{src}[IMAGE_MARKER_END]\n")

                # Extract the final text
                content = soup.get_text(separator="\n", strip=True)
                
                if not content or "Cloudflare" in content:
                    print(f"   ❌ WARNING: Content is empty or blocked by Cloudflare!")
                else:
                    # 4. Save the document
                    file_name = f"chapter_{chap_num}"
                    crawl.add_text_to_doc_file(chap_title, content, file_name)
                    print(f"   ✅ Saved Chapter {chap_num} successfully.")
                    
            else:
                raise Exception("crawl_data failed and returned None.")
                
        except Exception as e:
            failed_chapters.append((chap_title, chap_num))
            print(f"====== Warning: Error crawling {chap_title}", e)
            
        # ⚠️ CRITICAL: Sleep to prevent Cloudflare from banning your IP
        time.sleep(3)

    if failed_chapters:
        print(f"Failed chapters in this worker: {failed_chapters}")
        
    try:
        crawl.quit_driver()
    except:
        pass


def main(folder_name):
    print(f"======= Create {folder_name} folder =======")
    
    # Just initialize base to use the folder creation utility
    crawl = base(is_headless_mode=True)
    try:
        crawl.create_folder(folder_name)
        print(f"======= Created folder {folder_name} successfully ======")
    except Exception as e:
        return(f"Error creating folder: {e}")
    finally:
        try: crawl.quit_driver() 
        except: pass

    # 1. Get all chapters via API instead of opening a Selenium browser
    try:
        chapters_list = get_story_toc(main_url)
    except Exception as e:
        print(e)
        return

    # Prepare data: list of (chapter_dict, chapter_number)
    indexed_chapters = []
    for i, chap in enumerate(chapters_list):
        indexed_chapters.append((chap, i + 1))

    # Split into chunks for parallel processing
    num_threads = 3  # Keep this low (1 or 2) to avoid Wattpad rate-limiting you!
    chunk_size = math.ceil(len(indexed_chapters) / num_threads)
    chunks = [indexed_chapters[i:i + chunk_size] for i in range(0, len(indexed_chapters), chunk_size)]

    print(f"Starting {num_threads} threads...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(lambda chunk: crawl_worker(chunk, folder_name), chunks)
        
    print("======= All threads finished =======")


if __name__ == '__main__':
    main(storyName)

'''Note: run this code using cmd: uv run newtest/wattpad_crawler.py'''