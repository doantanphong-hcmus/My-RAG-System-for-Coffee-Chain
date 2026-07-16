import os
from dotenv import load_dotenv

# Tải các biến môi trường từ file .env
load_dotenv()

# Cấu hình API cho LLM (Claude)
ANTHROPIC_AUTH_TOKEN = os.getenv("ANTHROPIC_AUTH_TOKEN")
ANTHROPIC_BASE_URL = os.getenv("ANTHROPIC_BASE_URL")

# Cấu hình Database (Supabase)
DATABASE_URL = os.getenv("DATABASE_URL")

print(ANTHROPIC_BASE_URL) 

# Kiểm tra nhanh để đảm bảo các biến đã được load
if not ANTHROPIC_AUTH_TOKEN:
    print("⚠️ CẢNH BÁO: Không tìm thấy ANTHROPIC_AUTH_TOKEN trong .env")
if not ANTHROPIC_BASE_URL:
    print("⚠️ CẢNH BÁO: Không tìm thấy ANTHROPIC_BASE_URL trong .env")
if not DATABASE_URL:
    print("⚠️ CẢNH BÁO: Không tìm thấy DATABASE_URL trong .env")
