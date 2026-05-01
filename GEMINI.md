# Web Scraping Project Standards

## 1. Tech Stack & Environment
- **Core:** Python 3.11+ (Docker compatible)
- **Package Manager:** `uv` (luôn dùng `uv add <package>` để cài thêm thư viện).
- **Containerization:** Docker & Docker Compose (Chrome, SeleniumBase, Multithreading).
- **Scraping:** Selenium & SeleniumBase (cho web động), BeautifulSoup4 & Requests (cho web tĩnh).
- **Processing:** python-docx (Export), Zip archiving.
- **Project Structure:** 
  - `src/`: Core logic & Utilities.
  - `newtest/`: Scripts chạy Local (Hardcoded).
  - `docker_test/`: Scripts chạy Docker (CLI Arguments, JSON Passwords).
  - `passwords/`: Folder chứa file cấu hình mật khẩu JSON.

## 2. Docker & Deployment Standards
- **Isolation:** Scripts chạy trong Docker PHẢI sử dụng `argparse` để nhận URL và tên truyện từ dòng lệnh.
- **Environment Variables:** Sử dụng `os.getenv("SCRAPE_USER")` và `os.getenv("SCRAPE_PASS")` cho thông tin đăng nhập. Giá trị thật được lưu trong file `.env`.
- **Resource Management (Docker):** Luôn set `shm_size: '2gb'` trong `docker-compose.yml` để tránh crash Chrome khi chạy đa luồng.
- **Chrome Flags:** Trong Docker, bắt buộc dùng `--no-sandbox`, `--disable-dev-shm-usage`, và `--disable-gpu`.

## 3. Password Management
- **Centralization:** Tất cả mật khẩu truyện phải được gom vào thư mục `passwords/` dưới dạng file `.json`.
- **JSON Structure:** 
  - Khóa `"default"`: Mật khẩu mặc định cho toàn bộ chương.
  - Khóa `"số_chương"`: Mật khẩu riêng cho chương đó (ưu tiên cao hơn default).
- **Security:** Thư mục `passwords/` và file `.env` KHÔNG ĐƯỢC PHÉP commit lên Git.

## 4. Scraping Rules
- **Anti-Detection:** Ưu tiên dùng `SeleniumBase` (UC Mode) cho các trang có Cloudflare (như Mongtruyen).
- **Wait Strategy:** Tuyệt đối không dùng `time.sleep()`. Luôn sử dụng `WebDriverWait` với `expected_conditions` để đợi element.
- **Resource Management:** Luôn đảm bảo đóng Browser (`driver.quit()`) bằng block `try...finally` hoặc context manager.

## 5. Output & Integration
- **Storage:** Kết quả lưu vào `downloaded_files/`.
- **Google Drive:** Sử dụng `DriveManager` kết hợp với `credentials.json` và `get_config_folder_id()`.
- **Zipping:** Sử dụng method `zip_folder()` từ class `Base`.

## 6. Security & Git
- **Ignore List:** Bắt buộc liệt kê các file sau trong `.gitignore`:
  - `.env` (Chứa bí mật đăng nhập).
  - `passwords/` (Chứa mật khẩu truyện).
  - `credentials.json`, `token.json` (Google API).
  - `downloaded_files/`, `*.docx`, `*.zip`.
