from src.document_processor import process_pdf
from src.database import save_chunks_to_db 

def main(): 
    print("--- BẮT ĐẦU NẠP DỮ LIỆU ---") 
    # Đọc và chia nhỏ file PDF 
    chunks = process_pdf("Nội_Quy_Sunny_Coffee.pdf")

    # Đẩy lên DB 
    save_chunks_to_db(chunks)

    print("--- HOÀN TẤT ---") 

if __name__ == "__main__": 
    main() 