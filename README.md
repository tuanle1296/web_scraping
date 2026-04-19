# Web Scraping Project (Web Novel Specialist)

A high-level, flexible web automation and scraping framework built in Python 3.13+, specifically optimized for extracting web novels, bypassing anti-bot protections, and generating structured documents.

## 🚀 Overview
This project provides a robust framework for web scraping using **Selenium**, **SeleniumBase**, and **curl-cffi**. It is designed to handle dynamic content, iframes, and advanced anti-bot measures (like Cloudflare) while providing specialized tools for novel content extraction and `.docx` generation.

## ✨ Key Features
- **Anti-Bot Bypass**: 
  - `SeleniumBase` (UC Mode) for navigating Cloudflare-protected sites.
  - `curl-cffi` (impersonate) for standard HTTP scraping that mimics real browsers.
- **Dynamic Content Handling**: Advanced methods for scrolling, waiting for JS/jQuery conditions, and handling lazy-loaded images.
- **Novel-Specific Extraction**:
  - `get_element_text`: Custom JS-based text extraction that preserves image placeholders (`[IMAGE_MARKER_START]...`) and filters out anti-copy elements (zero-font spans).
  - `crawl_text_from_soup`: BeautifulSoup-based extraction with image marker support.
- **Content Export**: Automated export to `.docx` files with image downloading and embedding.
- **File Management & Archiving**:
  - `zip_folder`, `create_folder`, `save_doc`, etc.: Built-in file and directory operations (inherited from `FileManager`).
- **Cloud Integrations**:
  - **Gmail**: Automated sending of zip attachments via `MailManager`.
  - **Google Drive**: Automated file uploads to specific folders via `DriveManager`, utilizing `get_config_folder_id` for configuration.

## 📁 Project Structure
- `src/base_functions.py`: The core `Base` class (Automation, Scraping).
- `src/file_manager.py`: `FileManager` class (File/Folder operations, Zipping, config utility).
- `src/mail_manager.py`: Gmail integration for sending zip files.
- `src/drive_manager.py`: Google Drive API integration for cloud storage.
- `src/newlocators.py`: Site-specific configurations, selectors, and credentials using `dataclasses`.
- `credentials.json`: (User-provided) Google API credentials.
- `token.json`: (Auto-generated) Google OAuth session token.
- `config.json`: (User-provided) External IDs (e.g., Google Drive Folder ID).

## 🛠️ Usage Example
### Zipping and Uploading to Drive
```python
from src.base_functions import Base
from src.file_manager import get_config_folder_id
from src.drive_manager import DriveManager

# 1. Scrape and Zip
with Base() as crawl:
    # ... scraping logic ...
    # zip_folder is inherited from FileManager
    zip_path = crawl.zip_folder("my_scraped_data")

# 2. Upload to Drive using utility from file_manager.py
drive = DriveManager(credentials_path="credentials.json")
drive.upload_zip(zip_path, folder_id=get_config_folder_id())
```

### Sending via Gmail
```python
from src.mail_manager import MailManager

mailer = MailManager("your_email@gmail.com", "your_app_password")
mailer.send_email_with_zip(
    receiver_email="target@gmail.com",
    subject="Scraped Data",
    body="Attached is the zipped content.",
    zip_file_path="my_scraped_data.zip"
)
```

## 🤖 AI Context & Coding Standards (Mandatory)
- **Package Manager**: Use `uv` (e.g., `uv add <package>`).
- **Coding Style**: PEP 8, `snake_case` for functions/variables, `PascalCase` for classes.
- **Type Hinting**: Required for all function parameters and return values.
- **Documentation**: Every class/method MUST have a Docstring.
- **Wait Strategy**: Avoid `time.sleep()`; use `WebDriverWait` with `expected_conditions`.
- **Resource Management**: Use context managers or `try...finally` to ensure `driver.quit()`.
- **Bypass Rule**: If a site has Cloudflare, use `Base(use_seleniumbase=True)` and `go_to_webpage(url, bypass_cloudflare=True)`.
