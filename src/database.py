from langchain_community.vectorstores import PGVector
from src.config import DATABASE_URL 
from src.document_processor import get_embeddings 

# Tên Collection trong Database
COLLECTION_NAME = "sunny_coffee_rules"

def get_vector_db():
    """
    Kết nối database để lấy dữ liệu 
    """
    embeddings = get_embeddings()
    vector_db = PGVector(
    connection_string=DATABASE_URL, 

    embedding_function=embeddings, 

    collection_name=COLLECTION_NAME, 
        use_jsonb=True 
    ) 
    return vector_db 

def save_chunks_to_db(chunks):
    """
    Đẩy các chunk lên Supabase (tự động tạo bảng nếu chưa có)
    """
    print("Đang lưu các chunks vào DB...")
    embeddings = get_embeddings() 

    PGVector.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        
    collection_name=COLLECTION_NAME, 
        
    collection_string=DATABASE_URL, 
        use_jsonb=True, 
        pre_delete_collection=True 
        # Xóa data cũ của collection này nếu lỡ chạy file ingest nhiều lần
    )
    print("Lưu dữ liệu vào Database thành công!")
    
