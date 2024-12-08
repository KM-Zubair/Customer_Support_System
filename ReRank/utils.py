import cohere
import weaviate

def initialize_clients():
    cohere_client = cohere.Client(os.getenv("COHERE_API_KEY"))
    weaviate_client = weaviate.Client(
        url=os.getenv("WEAVIATE_API_URL"),
        auth_client_secret=weaviate.auth.AuthApiKey(api_key=os.getenv("WEAVIATE_API_KEY"))
    )
    return cohere_client, weaviate_client

def dense_retrieval(query):
    _, weaviate_client = initialize_clients()
    results = weaviate_client.query.get(
        "Documents", ["text", "title"]
    ).with_near_text({"concepts": [query]}).do()
    return results["data"]["Get"]["Documents"]

def rerank_responses(query, responses, num_responses=10):
    cohere_client, _ = initialize_clients()
    reranked = cohere_client.rerank(
        model="rerank-english-v2.0",
        query=query,
        documents=[r["text"] for r in responses],
        top_n=num_responses
    )
    return reranked
