from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from utils import dense_retrieval, rerank_responses
from evaluation import calculate_metrics

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    example_queries = [
        "What is the capital of Canada?",
        "Who is the tallest person in history?",
        "What are the benefits of solar energy?"
    ]
    return render_template('index.html', queries=example_queries)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = dense_retrieval(query)
    reranked_results = rerank_responses(query, results)
    metrics = calculate_metrics(query, reranked_results)
    return render_template(
        'results.html', query=query, results=reranked_results, metrics=metrics
    )

if __name__ == '__main__':
    app.run(debug=True)
