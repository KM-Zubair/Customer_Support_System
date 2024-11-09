from langchain.chains import ConversationalRetrievalChain
from langchain import OpenAI

def setup_conversation_chain(vectorstore):
    llm = OpenAI(api_key="your_openai_api_key")
    conversation_chain = ConversationalRetrievalChain(
        retriever=vectorstore.as_retriever(), llm=llm
    )
    memory = conversation_chain.create_memory()
    return conversation_chain, memory
