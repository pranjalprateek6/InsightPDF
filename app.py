import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import HuggingFacePipeline
from transformers import pipeline


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)
    return text_splitter.split_text(text)


def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.from_texts(texts=text_chunks, embedding=embeddings)


def get_qa_chain():
    hf_pipeline = pipeline("text2text-generation", model="google/flan-t5-large", model_kwargs={"max_length": 1024, "temperature": 0.5})
    llm = HuggingFacePipeline(pipeline=hf_pipeline)
    qa_chain = load_qa_chain(llm, chain_type="stuff")
    return qa_chain


def main():
    st.set_page_config(page_title="InsightPDF", page_icon="💭")
    st.title("InsightPDF - Ask your PDF 💭")
    st.sidebar.subheader("Upload Documents")
    pdf_docs = st.sidebar.file_uploader("PDFs only", accept_multiple_files=True)

    if pdf_docs:
        with st.spinner("Processing PDFs..."):
            raw_text = get_pdf_text(pdf_docs)
            text_chunks = get_text_chunks(raw_text)
            vectorstore = get_vectorstore(text_chunks)
            qa_chain = get_qa_chain()

        st.success("PDFs processed successfully.")

        user_question = st.text_input("Ask a question about the documents.")
        if user_question:
            with st.spinner("Generating response..."):
                docs = vectorstore.similarity_search(user_question)
                response = qa_chain.run(input_documents=docs, question=user_question)
                st.write(response)

if __name__ == "__main__":
    main()