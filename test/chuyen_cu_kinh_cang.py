import requests
from bs4 import BeautifulSoup
import base64
import io
from src.base_functions import *
from PIL import Image
import pytesseract


def scrape_chapter_content(url, crawl_instance):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    print(f"1. Downloading {url}...")
    try:
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8' # Force Vietnamese encoding

        soup = BeautifulSoup(response.text, 'html.parser')

        title_element = crawl_instance.get_element_by_tag(soup, 'h1', 'entry-title')
        content_element = crawl_instance.get_element_by_tag(soup, 'div', 'entry-content clear')

        print("2. Processing images (Base64 & Links)...")
        
        # Loop through all images in the story
        images = content_element.find_all('img')
        
        for img in images:
            img_src = img.get('src', '')

            # --- CASE A: Base64 Encoded Image (The one in your screenshot) ---
            if img_src.startswith('data:image'):
                try:
                    # 1. Clean the string (remove "data:image/png;base64,")
                    base64_data = img_src.split(',')[1]
                    
                    # 2. Decode bytes
                    image_bytes = base64.b64decode(base64_data)
                    
                    # 3. Open image in memory (no need to save to file)
                    image = Image.open(io.BytesIO(image_bytes))
                    
                    # 4. Run OCR (Specify Vietnamese!)
                    # --psm 6 assumes a block of text
                    extracted_text = pytesseract.image_to_string(image, lang='vie', config='--psm 6')
                    
                    print(f"   -> Extracted hidden text: {extracted_text[:30]}...")
                    
                    # 5. Replace the image tag with the text
                    img.replace_with(f"\n{extracted_text}\n")
                    
                except Exception as e:
                    print(f"   -> Failed to process base64 image: {e}")

            # --- CASE B: Normal Image Link ---
            elif img_src.startswith('http'):
                # Just leave a marker for normal images
                img.replace_with(f"\n[IMAGE LINK: {img_src}]\n")

        # --- FINAL OUTPUT ---
        title = title_element.get_text().strip()
        # Save to .docx file using the method from the base class, which handles saving to the correct folder.
        crawl_instance.save_doc(title_element, content_element)
        
        print(f"   -> Successfully saved: {title}.docx")
            
    except Exception as e:
        print(f"Error: {e}")

def scrape_story(base_url):
    """Finds all chapter links from a story page and scrapes each one."""
    crawl = base()
    
    print(f"--- Starting to scrape story from: {base_url} ---")
    main_page_soup = crawl.crawl_data(base_url)
    
    story_title_element = main_page_soup.find('title')
    story_title = story_title_element.get_text().strip() if story_title_element else "story"
    
    # Create a folder named after the story
    crawl.create_folder(story_title)
    print(f"Created folder: '{story_title}'")

    chapter_links = [a['href'] for a in main_page_soup.select("h2.entry-title a[href]")]
    
    print(f"Found {len(chapter_links)} chapters. Starting download...\n")
    for link in chapter_links:
        scrape_chapter_content(link, crawl)

# --- Main Execution ---
scrape_story("https://rungtruyen.com/category/ngon-tinh/chuyen-cu-kinh-cang/")