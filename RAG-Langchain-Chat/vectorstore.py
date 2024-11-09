from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

def create_vectorstore(chunks):
    embeddings = OpenAIEmbeddings(api_key="your_openai_api_key")
    vectorstore = Chroma.from_documents(chunks, embeddings)
    return vectorstore
