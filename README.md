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

## 📁 Project Structure
- `src/base_functions.py`: The core `Base` class containing all automation and extraction logic.
- `src/locators.py`: Site-specific configurations, selectors, and credentials using `dataclasses`.
- `pyproject.toml`: Managed by **`uv`**, containing dependencies (`selenium`, `seleniumbase`, `curl-cffi`, `python-docx`).
- `downloaded_files/`: Default output directory for scraped content.
- `GEMINI.md`: Detailed project standards and coding conventions.

## 🛠️ Usage Example
The `Base` class supports context manager usage for automatic browser cleanup:

```python
from src.base_functions import Base
from selenium.webdriver.common.by import By

# Initialize with SeleniumBase UC Mode
with Base(use_seleniumbase=True, is_headless_mode=False) as crawl:
    crawl.go_to_webpage("https://example-novel-site.com", bypass_cloudflare=True)
    crawl.create_folder("Novel_Title")
    
    # Extract text while preserving image markers
    content = crawl.get_element_text((By.CLASS_NAME, "chapter-content"))
    
    # Save to Word document
    crawl.add_text_to_doc_file("Chapter 1", content)
```

## 🤖 AI Context & Coding Standards (Mandatory)
- **Package Manager**: Use `uv` (e.g., `uv add <package>`).
- **Coding Style**: PEP 8, `snake_case` for functions/variables, `PascalCase` for classes.
- **Type Hinting**: Required for all function parameters and return values.
- **Documentation**: Every class/method MUST have a Docstring.
- **Wait Strategy**: Avoid `time.sleep()`; use `WebDriverWait` with `expected_conditions`.
- **Resource Management**: Use context managers or `try...finally` to ensure `driver.quit()`.
- **Bypass Rule**: If a site has Cloudflare, use `Base(use_seleniumbase=True)` and `go_to_webpage(url, bypass_cloudflare=True)`.
