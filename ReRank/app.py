from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from utils import preprocess_text, generate_embeddings, build_search_index, search_query, generate_answer

load_dotenv()

app = Flask(__name__)

# Load and preprocess data
TEXT_DATA = """<Insert large text or documents here>"""  # Add your input data here
CHUNKS = preprocess_text(TEXT_DATA)
EMBEDDINGS = generate_embeddings(CHUNKS)
SEARCH_INDEX = build_search_index(EMBEDDINGS)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = search_query(query, CHUNKS, SEARCH_INDEX)
    answer = generate_answer(query, results)
    return render_template('results.html', query=query, results=results, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
