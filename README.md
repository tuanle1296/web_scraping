# 🚀 Web Scraping Project (Web Novel Specialist)

---

## 🇺🇸 English Version

A high-level, flexible web automation and scraping framework built in Python 3.11+, specifically optimized for extracting web novels, bypassing anti-bot protections, and generating structured documents using Docker.

### ✨ Key Features
- **Docker-First Architecture**: Run the crawler anywhere without local Python or Chrome installation.
- **Multithreading**: High-speed scraping using `ThreadPoolExecutor`.
- **Anti-Bot Bypass**: `SeleniumBase` (UC Mode) and `curl-cffi` to navigate Cloudflare.
- **Flexible Password Support**: Manage story passwords via central JSON files in the `passwords/` folder.
- **Cloud Export**: Automatic zipping and uploading to **Google Drive**.

### 📁 Project Structure
- `src/`: Core logic and automation utilities.
- `docker_test/`: Scripts optimized for Docker with CLI argument support.
- `newtest/`: Original scripts for local execution.
- `passwords/`: Centralized JSON password management.

### 🛠️ How to Run (Docker)
1. Prepare your `.env` file for credentials (use `SCRAPE_USER` and `SCRAPE_PASS`).
2. Run via Docker Compose:
```bash
docker compose -f docker_test_compose.yml up --build
```
3. To change the story, edit the `command` section in `docker_test_compose.yml` to specify the `--url`, `--name`, and `--pass-file`.

---

## 🇻🇳 Tiếng Việt

Một framework cào dữ liệu web mạnh mẽ được xây dựng bằng Python 3.11+, tối ưu hóa cho việc trích xuất nội dung truyện chữ, vượt qua các hệ thống chống bot và tự động đóng gói tài liệu bằng Docker.

### ✨ Các Tính năng Chính
- **Kiến trúc Docker-First**: Chạy crawler ở bất kỳ đâu mà không cần cài đặt Python hay Chrome trên máy thật.
- **Đa luồng (Multithreading)**: Tăng tốc độ cào dữ liệu bằng `ThreadPoolExecutor`.
- **Vượt rào cản Bot**: Sử dụng `SeleniumBase` (UC Mode) và `curl-cffi` để vượt qua Cloudflare.
- **Quản lý Mật khẩu Linh hoạt**: Quản lý mật khẩu truyện tập trung qua các file JSON trong thư mục `passwords/`.
- **Xuất dữ liệu lên Cloud**: Tự động nén zip và upload kết quả lên **Google Drive**.

### 📁 Cấu trúc Project
- `src/`: Chứa logic cốt lõi và các công cụ tự động hóa.
- `docker_test/`: Các script được tối ưu cho Docker, hỗ trợ truyền tham số dòng lệnh.
- `newtest/`: Các script gốc dùng để chạy trên máy cá nhân (Local).
- `passwords/`: Nơi quản lý mật khẩu tập trung dưới dạng JSON.

### 🛠️ Hướng dẫn Chạy (Docker)
1. Chuẩn bị file `.env` chứa tài khoản đăng nhập (biến `SCRAPE_USER` và `SCRAPE_PASS`).
2. Chạy qua Docker Compose:
```bash
docker compose -f docker_test_compose.yml up --build
```
3. Để đổi truyện cần crawl, hãy sửa phần `command` trong file `docker_test_compose.yml` với các tham số `--url`, `--name`, và `--pass-file`.
