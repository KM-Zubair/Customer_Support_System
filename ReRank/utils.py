import os
import numpy as np
from cohere import Client
from annoy import AnnoyIndex

co = Client(os.getenv("COHERE_API_KEY"))

def preprocess_text(text):
    """Split text into paragraphs and clean."""
    paragraphs = text.split('\n\n')
    return [p.strip() for p in paragraphs if p.strip()]

def generate_embeddings(chunks):
    """Generate vector embeddings for text chunks."""
    response = co.embed(texts=chunks)
    return np.array(response.embeddings)

def build_search_index(embeddings):
    """Build a search index using Annoy."""
    index = AnnoyIndex(embeddings.shape[1], 'angular')
    for i, vector in enumerate(embeddings):
        index.add_item(i, vector)
    index.build(10)  # Build 10 trees for efficiency
    return index

def search_query(query, chunks, index, num_results=5):
    """Search the index for the most similar chunks."""
    query_embed = co.embed(texts=[query]).embeddings[0]
    similar_ids = index.get_nns_by_vector(query_embed, num_results, include_distances=True)[0]
    return [chunks[i] for i in similar_ids]

def generate_answer(query, context_chunks):
    """Generate an answer using the top context."""
    top_context = context_chunks[0]  # Use the top result for simplicity
    prompt = f"""
    Context:
    {top_context}
    
    Question: {query}
    
    Answer based on the context above. If no answer is found, reply "Answer not available."
    """
    response = co.generate(
        model="command-nightly",
        prompt=prompt,
        max_tokens=100,
        temperature=0.5
    )
    return response.generations[0].text.strip()
