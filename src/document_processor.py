from langchain_community.document_loaders import PyPDFLoader 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings 

def get_embeddings(): 
    """
    Khởi tạo mô hình Embedding. 
    """
    # Sử dụng mô hình: vietnamese-sbert
    print("Đang khởi tạo Embedding Model ...")
    embeddings = HuggingFaceEmbeddings(model_name="keepitreal/vietnamese-sbert") 
    return embeddings 

def process_pdf(file_path: str): 
    """
    Đọc file PDF và chia nhỏ thành các chunks. 
    """
    print(f"Đang đọc file PDF: {file_path}")
    loader = PyPDFLoader(file_path)
    documents = loader.load() # Mảng chứa các đối tượng Documents

    # Chia nhỏ văn bản để AI dễ tìm kiếm ngữ cảnh
    print("Đang thực hiện quá trình Chunking...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=700, # Mỗi chunk có khoảng 700 ký tự
        chunk_overlap=100, # Phần nối tiếp giữa 2 chunk để không mất ngữ cảnh
        separators=["\n\n", "\n", ".", " ", ""]
    )
    chunks = text_splitter.split_documents(documents) 

    print(f"Hoàn tất quá trình Chunking PDF")
    return chunks 


