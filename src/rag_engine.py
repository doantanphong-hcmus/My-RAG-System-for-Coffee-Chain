from langchain_anthropic import ChatAnthropic 
from langchain_core.prompts import PromptTemplate 
from langchain_core.runnables import RunnablePassthrough 
from langchain_core.output_parsers import StrOutputParser 

from src.config import ANTHROPIC_AUTH_TOKEN, ANTHROPIC_BASE_URL 
from src.database import get_vector_db 

def get_retriever(): 
    """
    Tạo công cụ tìm kiếm vào Supabase
    """
    db = get_vector_db() # Cấu hình tìm kiếm: Lấy ra 3 đoạn chunks giống với câu hỏi nhất
    return db.as_retriever(search_kwargs={"k":3})

def get_rag_chain():
    """
    Tạo Chain kết nối Retriever -> Prompt -> LLM
    """
    # Khởi tạo Claude 
    llm = ChatAnthropic(
        model_name="claude-opus-4-8",   
        api_key=ANTHROPIC_AUTH_TOKEN,

        base_url=ANTHROPIC_BASE_URL, 
        temperature=0.2
    )


    # Tạo Prompt Template
    prompt_template = """
    Bạn là một trợ lý nhân sự tận tâm của quán Sunny Coffee. 
    Hãy sử dụng BẢN NỘI QUY dưới đây để trả lời câu hỏi của nhân viên. 
    Nếu câu hỏi không có thông tin trong nội quy, hãy nói rõ là "Xin lỗi, tôi không tìm thấy quy định về vấn đề này trong nội quy hiện tại" chứ tuyệt đối KHÔNG ĐƯỢC TỰ BỊA RA. 

    BẢN NỘI QUY: {context}

    CÂU HỎI CỦA NHÂN VIÊN: {question} 

    TRẢ LỜI: 
"""

    prompt = PromptTemplate.from_template(prompt_template) 

    # Hàm phụ trợ để nối 3 đoạn văn bản tìm được thành một chuỗi dài
    def format_docs(docs): 
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain = (
        {"context": get_retriever() | format_docs, "question":
        RunnablePassthrough()}
        | prompt
        | llm 
        | StrOutputParser()
    )

    return rag_chain 
