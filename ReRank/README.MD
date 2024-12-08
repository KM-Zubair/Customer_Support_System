# [Presentation Slides](https://docs.google.com/presentation/d/1HROtl9cXLolhXa1An-k2j9LtVpE1zkHFxuVQJRqV9PY/edit?usp=sharing) | ReRank Search System

## Project Overview

The ReRank Search System is a semantic search application built with Flask, Cohere, and Weaviate. It enhances search capabilities by integrating Dense Retrieval and ReRanking to provide more relevant results to user queries. The system also includes a **generative answer pipeline** to process queries, search for relevant contexts, and provide user-specific answers using large language models. Performance is evaluated using metrics such as MAP, MRR, and NDCG.

## Features

- Perform dense retrieval to fetch relevant documents.
- ReRank retrieved documents to improve search precision.
- Generate answers from context using generative AI.
- Display search results with relevance scores and contextual information.
- Evaluate search performance using MAP, MRR, and NDCG metrics.
- User-friendly web interface with example queries.

## Setup Instructions

### Prerequisites

- Python 3.7+
- Flask
- Cohere Python SDK
- Weaviate Python client
- Annoy for vector search
- Ensure you have Cohere and Weaviate API keys.

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/YourUsername/ReRank-Project.git
    cd ReRank-Project
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv env
    source env/bin/activate   # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the project root and add your Cohere and Weaviate API keys:

    ```env
    COHERE_API_KEY=your_cohere_api_key
    WEAVIATE_API_KEY=your_weaviate_api_key
    WEAVIATE_API_URL=your_weaviate_instance_url
    ```

5. **Run the application:**

    ```sh
    python app.py
    ```

    The application will be accessible at `http://127.0.0.1:5000/`.

## Project Structure

```plaintext
.
├── app.py                  # Main application file
├── utils.py                # Utility functions for preprocessing, embedding, and search
├── evaluation.py           # Functions for evaluation metrics (MAP, MRR, NDCG)
├── templates               # HTML templates
│   ├── index.html          # Home page template
│   └── results.html        # Results page template
├── static                  # Static files (CSS, JS)
│   ├── css
│   │   └── styles.css      # CSS styles
│   └── js
│       └── script.js       # Optional JavaScript functionality
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Example Queries

The system supports queries such as:
- **"What is the capital of Canada?"**
- **"Who is the tallest person in history?"**
- **"What are the benefits of solar energy?"**
- **"How does AI impact the job market?"**

## Generative Answer Workflow

1. **Input Query**: The user provides a query through the web interface.
2. **Text Chunking**: Preprocess input data into manageable chunks.
3. **Embedding**: Generate vector embeddings for text chunks.
4. **Search Index**: Build and search a vector-based index for relevant contexts.
5. **Generate Answer**: Use the most relevant context to generate a user-specific answer with Cohere's language model.

## Future Enhancements

- **Multilingual Support**: Enable querying and answering in multiple languages.
- **Advanced Visualizations**: Include graphical representations of relevance scores and metrics.
- **Improved Retrieval**: Enhance the search process with hybrid search techniques.
- **Deployment**: Containerize the application using Docker for production environments.

Feel free to contribute by submitting issues or pull requests!

--- 