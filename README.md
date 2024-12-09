# InsightPDF

**InsightPDF** is a Streamlit-based application that enables users to upload PDF documents and ask questions about their content. By leveraging Hugging Face models, LangChain, and FAISS, it provides efficient document analysis and question-answering capabilities.

---
![image](https://github.com/user-attachments/assets/0dab9646-02bc-4bf2-bfd7-e8f44ddb7e00)

## Features
- Upload and process one or more PDF documents.
- Extract text from PDFs using `PyPDF2`.
- Split text into manageable chunks with LangChain's `CharacterTextSplitter`.
- Generate embeddings using `sentence-transformers/all-MiniLM-L6-v2`.
- Perform semantic similarity searches with FAISS.
- Answer questions using `google/flan-t5-large`.

---

## Requirements
- **Python Version**: 3.7 or above.
- **Libraries**:
  - `streamlit`
  - `PyPDF2`
  - `langchain`
  - `sentence-transformers`
  - `transformers`
  - `faiss-cpu`

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/InsightPDF.git
   cd InsightPDF
