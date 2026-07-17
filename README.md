# Hệ Thống Truy Xuất Và Sinh Văn Bản (RAG) Dựa Trên Tài Liệu

## 1. Giới Thiệu
Đây là một bài thực hành cá nhân (Lab) nhằm mục đích tự nghiên cứu và tìm hiểu sâu về kiến trúc RAG (Retrieval-Augmented Generation). Dự án ứng dụng kiến trúc này để xây dựng một hệ thống hỏi đáp tự động, cho phép người dùng đặt câu hỏi và nhận câu trả lời chính xác dựa trên nội dung của một tài liệu văn bản cụ thể (trong bài thực hành này là bản nội quy của một cơ sở kinh doanh). 

Mục tiêu cốt lõi của dự án là nắm vững quy trình trích xuất văn bản, chuyển đổi dữ liệu thành véc-tơ, quản lý cơ sở dữ liệu véc-tơ và tích hợp chuỗi xử lý với mô hình ngôn ngữ lớn.

## 2. Kiến Trúc Và Công Nghệ
Hệ thống được thiết kế theo dạng mô-đun với các thành phần kỹ thuật sau:
- Xử lý tài liệu: Sử dụng công cụ của thư viện LangChain để đọc tập tin định dạng PDF và chia nhỏ văn bản thành các đoạn ngắn.
- Mô hình biểu diễn (Embedding): Sử dụng mô hình hỗ trợ xử lý tiếng Việt (vietnamese-sbert) thông qua thư viện HuggingFace để chuyển đổi các đoạn văn bản thành định dạng véc-tơ.
- Lưu trữ và truy xuất: Sử dụng cơ sở dữ liệu PostgreSQL kết hợp với phần mở rộng PGVector (vận hành trên nền tảng Supabase) để lưu trữ và tìm kiếm các véc-tơ có độ tương đồng cao nhất.
- Khung ứng dụng: Ứng dụng kiến trúc LangChain để liên kết các thành phần thành một chuỗi xử lý thống nhất.
- Mô hình ngôn ngữ lớn (LLM): Tích hợp dòng mô hình Claude thông qua giao diện lập trình ứng dụng (API) để phân tích ngữ cảnh và tổng hợp câu trả lời ngôn ngữ tự nhiên.

## 3. Cấu Trúc Mã Nguồn
```text
My-RAG-System-for-Coffee-Chain/
├── src/
│   ├── __init__.py             
│   ├── config.py               # Thiết lập cấu hình và nạp các biến môi trường
│   ├── document_processor.py   # Xử lý tập tin tài liệu và khởi tạo mô hình biểu diễn véc-tơ
│   ├── database.py             # Quản lý kết nối và tương tác với cơ sở dữ liệu PostgreSQL
│   └── rag_engine.py           # Thiết lập luồng truy xuất và kết nối với mô hình ngôn ngữ lớn
├── .env.example                # Tập tin mẫu định nghĩa các biến kết nối
├── requirements.txt            # Danh sách các thư viện mã nguồn mở cần thiết
├── Nội_Quy_Sunny_Coffee.pdf    # Tập tin tài liệu mẫu cung cấp dữ liệu đầu vào
├── ingest.py                   # Tập lệnh trích xuất văn bản và nạp dữ liệu vào cơ sở dữ liệu
└── app.py                      # Tập lệnh chính để khởi chạy giao diện tương tác dòng lệnh
```

## 4. Hướng Dẫn Cài Đặt
Bước 1: Khởi tạo môi trường ảo và cài đặt các thư viện phụ thuộc.
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

Bước 2: Thiết lập kết nối.
- Tạo một tập tin mang tên `.env` tại thư mục gốc của dự án.
- Cung cấp chuỗi kết nối cơ sở dữ liệu và khóa xác thực vào tập tin `.env` dựa theo định dạng của `.env.example`.

## 5. Hướng Dẫn Khởi Chạy
Bước 1: Nạp dữ liệu vào cơ sở dữ liệu. 
Tập lệnh này chỉ yêu cầu thực thi một lần duy nhất trong lần triển khai đầu tiên hoặc khi có sự thay đổi về tài liệu gốc.
```bash
python ingest.py
```

Bước 2: Khởi chạy giao diện tương tác.
Sau khi quy trình nạp dữ liệu hoàn tất, thực thi tập lệnh dưới đây để bắt đầu đặt câu hỏi với hệ thống.
```bash
python app.py
```
