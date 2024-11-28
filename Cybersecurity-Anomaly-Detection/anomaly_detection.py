from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from log_preprocessor import parse_log

def detect_anomaly(log_entry, model, vectorstore):
    """
    Detects if a log entry is anomalous.
    """
    try:
        structured_log = parse_log(log_entry)
        embedding = OpenAIEmbeddings().embed_query(str(structured_log))
        results = vectorstore.similarity_search_by_vector(embedding, k=3)

        # Simple logic: if similarity is below a threshold, it's an anomaly
        anomaly_threshold = 0.7
        similarity_scores = [result["score"] for result in results]
        average_score = sum(similarity_scores) / len(similarity_scores)
        
        if average_score < anomaly_threshold:
            return True  # Anomaly detected
        return False  # Normal behavior
    except ValueError as e:
        print(f"Error parsing log for anomaly detection: {e}")
        return True  # Treat unprocessable logs as anomalies
