# Web Scraping Project Standards

## 1. Tech Stack & Environment
- **Core:** Python 3.13+
- **Package Manager:** `uv` (luôn dùng `uv add <package>` để cài thêm thư viện).
- **Scraping:** Selenium & SeleniumBase (cho web động), BeautifulSoup4 & Requests (cho web tĩnh).
- **Processing:** Pytesseract (OCR), Pillow (Image), python-docx (Export).
- **Project Structure:** Code chính nằm trong `src/`, test nằm trong `test/`.

## 2. Coding Conventions
- **Style:** Tuân thủ PEP 8.
- **Naming:** 
  - Biến/Hàm: `snake_case`.
  - Class: `PascalCase`.
  - Hằng số: `UPPER_SNAKE_CASE`.
- **Type Hinting:** Bắt buộc sử dụng Type Hints cho tất cả tham số hàm và giá trị trả về (ex: `def fetch_data(url: str) -> dict:`).
- **Documentation:** Mỗi function/class phải có Docstring mô tả mục đích và các tham số.

## 3. Scraping Rules
- **Anti-Detection:** Ưu tiên dùng `SeleniumBase` với các chế độ bypass bot nếu gặp khó khăn.
- **Wait Strategy:** Tuyệt đối không dùng `time.sleep()`. Luôn sử dụng `WebDriverWait` với `expected_conditions` để đợi element.
- **Data Safety:** Kiểm tra sự tồn tại của element (`try-except` hoặc check length) trước khi extract để tránh crash giữa chừng.
- **Resource Management:** Luôn đảm bảo đóng Browser (`driver.quit()`) bằng block `try...finally` hoặc context manager.

## 4. Output, Archiving & Integration
- **Logging:** Dùng `print()` thay vì `logging()`.
- **Storage:** File tải về hoặc export phải được lưu vào thư mục `downloaded_files/`.
- **Archiving:** Khi cần nén dữ liệu, sử dụng method `zip_folder()` (kế thừa từ `FileManager` trong `Base` class).
- **Email:** Sử dụng `MailManager` trong `src/mail_manager.py` để gửi file zip qua Gmail. Yêu cầu dùng App Password.
- **Google Drive:** Sử dụng `DriveManager` trong `src/drive_manager.py` để upload file lên Drive. Sử dụng hàm tiện ích `get_config_folder_id()` từ `src/file_manager.py` để lấy ID folder từ `config.json`.

## 5. Security
- Không bao giờ commit `credentials.json`, `token.json`, `config.json`, hoặc App Passwords lên Git.
- Luôn đảm bảo các file này được liệt kê trong `.gitignore`.

## 5. Workflow
- Trước khi viết script mới, hãy kiểm tra các utility đã có trong `src/` để tái sử dụng.
- Khi tạo file mới, hãy cập nhật `.gitignore` nếu file đó tạo ra dữ liệu rác hoặc log.
