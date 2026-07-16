from src.rag_engine import get_rag_chain 

def main():
    print("Đang khởi tạo trợ lý Nhân sự Sunny Coffee...")
    rag_chain = get_rag_chain() 
    print("Hệ thống đã sẵn sàng! (Gõ thoát để kết thúc)\n")
    print("=" * 60)

    while True: 
        # Nhận câu hỏi từ người dùng
        question = input("Nhân viên: ")

        if question.lower() in ['thoát', 'exit', 'quit']: 
            print("AI: Chào tạm biệt! Chúc bạn một ngày vui.")
            break  

        if not question.strip(): 
            continue
        print("AI: Đang tra cứu nội quy và suy nghĩ...", end = "\n")

        # Gọi RAG chain để sinh câu trả lời 
        answer = rag_chain.invoke(question) 

        # In câu trả lời ra màn hình (ghi đè dòng tra cứu) 
        print("AI:", answer) 
        print("-" * 60)

        
if __name__ == "__main__": 
    main() 