import sys
import os
import math
import re
import time
import json
import argparse
import concurrent.futures
from curl_cffi import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.base_functions import *
from src.file_manager import get_config_folder_id
from src.drive_manager import DriveManager

def get_story_toc(start_url):
    """
    Extracts chapter list from Wattpad API.
    """
    match = re.search(r'wattpad\.com/(\d+)', start_url)
    if not match:
        raise ValueError("Could not find a valid Chapter ID in the provided URL.")
    
    chapter_id = match.group(1)
    print(f"Extracted Starting Chapter ID: {chapter_id}")

    part_api = f"https://www.wattpad.com/api/v3/story_parts/{chapter_id}"
    response = requests.get(part_api, impersonate="chrome120")
    if response.status_code != 200:
        raise ConnectionError("Failed to fetch Story ID. Cloudflare might be blocking.")
        
    story_id = response.json().get("groupId")
    
    print(f"Fetching Table of Contents for Story ID: {story_id}...")
    story_api = f"https://www.wattpad.com/api/v3/stories/{story_id}?fields=id,title,parts(id,title)"
    story_data = requests.get(story_api, impersonate="chrome120").json()
    
    story_title = story_data.get('title')
    all_chapters = story_data.get('parts', [])
    
    print(f"📚 Found Story: '{story_title}' | 📑 Total Chapters: {len(all_chapters)}")
    return all_chapters


def crawl_worker(chapter_data, folder_name):
    """
    Worker function to process a chunk of chapters.
    """
    with Base(True) as crawl:
        try:
            crawl.set_path(folder_name)
        except Exception as e:
            print(f"Error while setting folder path: {e}")

        # Close browser immediately
        crawl.quit_driver()
        
        for chapter, chap_num in chapter_data:
            chap_id = chapter['id']
            chap_title = chapter['title']
            
            try:
                print(f"--- Crawling Chapter {chap_num}: {chap_title} ---")
                api_url = f"https://www.wattpad.com/apiv2/storytext?id={chap_id}"
                
                raw_text = crawl.crawl_data(api_url, return_type="text", impersonate="chrome120")
                if raw_text:
                    if raw_text.strip().startswith("{"):
                        try:
                            data = json.loads(raw_text)
                            raw_html = data.get("text", raw_text)
                        except json.JSONDecodeError:
                            raw_html = raw_text
                    else:
                        raw_html = raw_text

                    soup = BeautifulSoup(raw_html, "html.parser")
                    
                    # Clean Anti-scraping spans
                    for hidden in soup.find_all('span', style=lambda v: v and 'font-size:0' in v.replace(' ', '')):
                        hidden.decompose()

                    # Mark Images
                    for img in soup.find_all('img'):
                        src = img.get('src') or img.get('data-src') or img.get('data-original')
                        if src:
                            if src.startswith("//"): src = "https:" + src
                            img.replace_with(f"\n[IMAGE_MARKER_START]{src}[IMAGE_MARKER_END]\n")

                    content = soup.get_text(separator="\n", strip=True)
                    if content and "Cloudflare" not in content:
                        crawl.add_text_to_doc_file(chap_title, content, f"chapter_{chap_num}")
                        print(f"✅ Saved Chapter {chap_num} successfully.")
                    else:
                        print(f"❌ WARNING: Chapter {chap_num} content is empty or blocked.")
                else:
                    print(f"❌ ERROR: Failed to crawl Chapter {chap_num}")
                    
            except Exception as e:
                print(f"Exception during Chapter {chap_num} crawl: {e}")
                
            time.sleep(3) # Throttle to avoid rate limits


def main():
    parser = argparse.ArgumentParser(description='Wattpad Crawler (Docker Optimized)')
    parser.add_argument('--url', type=str, required=True, help='Any chapter URL from the story')
    parser.add_argument('--name', type=str, required=True, help='Output folder name')
    args = parser.parse_args()

    main_url = args.url
    storyName = args.name

    print(f"======= Starting Wattpad crawl for: {storyName} =======")
    
    # Initialize storage folder
    with Base(True) as temp_crawl:
        try:
            temp_crawl.create_folder(storyName)
        except Exception as e:
            print(f"Error creating folder: {e}")
            return

    try:
        chapters_list = get_story_toc(main_url)
    except Exception as e:
        print(f"Error fetching TOC: {e}")
        return

    indexed_chapters = [(chap, i + 1) for i, chap in enumerate(chapters_list)]
    num_threads = 2 # Keep low for Wattpad
    chunk_size = math.ceil(len(indexed_chapters) / num_threads)
    chunks = [indexed_chapters[i:i + chunk_size] for i in range(0, len(indexed_chapters), chunk_size)]

    print(f"Launching {num_threads} threads for {len(chapters_list)} chapters...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(lambda chunk: crawl_worker(chunk, storyName), chunks)
        
    print("======= Finished crawling all chapters =======")
    
    # Zip and Upload to Drive
    try:
        with Base(True) as zip_crawl:
            zip_path = zip_crawl.zip_folder(storyName)
            if zip_path:
                print(f"Folder zipped successfully: {zip_path}")
                drive = DriveManager()
                drive.upload_zip(zip_path, folder_id=get_config_folder_id())
                print("======= Successfully uploaded to Google Drive =======")
    except Exception as e:
        print(f"Error during zipping or uploading: {e}")

if __name__ == '__main__':
    main()
