from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from log_preprocessor import preprocess_logs
import os

def create_vectorstore():
    """
    Creates a vector database from structured webserver logs.
    """
    embeddings = OpenAIEmbeddings()

    # Load and preprocess raw logs
    logs_path = os.path.join("webserver_logs", "normal_logs.txt")
    with open(logs_path, "r") as f:
        raw_logs = f.readlines()

    structured_logs = preprocess_logs(raw_logs)
    log_texts = [str(log) for log in structured_logs]  # Convert dicts to strings

    # Create a Chroma vectorstore
    vectorstore = Chroma.from_texts(log_texts, embedding=embeddings)
    print("Vectorstore created from normal logs.")
    return vectorstore
