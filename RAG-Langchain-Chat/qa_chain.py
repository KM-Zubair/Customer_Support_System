from langchain.chains import RetrievalQA
from langchain import OpenAI

def setup_qa_chain(vectorstore):
    llm = OpenAI(api_key="your_openai_api_key")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())
    return qa_chain
