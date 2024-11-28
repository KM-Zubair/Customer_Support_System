# sfbu_support.py
from langchain.document_loaders import PDFLoader, YouTubeLoader, URLLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain import OpenAI
import os

def load_documents():
    """
    Loads documents from multiple sources (PDF, YouTube, and URL).
    """
    pdf_loader = PDFLoader("https://www.sfbu.edu/sites/default/files/Documents/sfbu-2024-2025-university-catalog-8-20-2024.pdf")
    pdf_documents = pdf_loader.load()

    youtube_loader = YouTubeLoader("https://www.youtube.com/watch?v=kuZNIvdwnMc")
    youtube_documents = youtube_loader.load()

    url_loader = URLLLoader("https://www.sfbu.edu/student-health-insurance")
    url_documents = url_loader.load()

    return pdf_documents + youtube_documents + url_documents

def split_documents(documents):
    """
    Splits documents into manageable chunks using a text splitter.
    """
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(documents)

def create_vectorstore(chunks):
    """
    Creates a vectorstore from document chunks for retrieval.
    """
    return Chroma.from_documents(chunks, embedding="text-embedding-ada-002")

def setup_conversation_chain(vectorstore):
    """
    Sets up a conversational retrieval chain with OpenAI and vectorstore.
    """
    llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    conversation_chain = ConversationalRetrievalChain(
        retriever=vectorstore.as_retriever(), llm=llm
    )
    memory = conversation_chain.create_memory()
    return conversation_chain, memory
