# ChatGPT Customer Support Application

## Project Overview

This project is a customer support application using Flask and the OpenAI GPT-3.5 API. The application allows users to generate customer comments, email subjects, summaries, and perform sentiment analysis on customer comments. It supports multiple languages commonly used in the US.

## Features

- Generate customer comments based on product descriptions.
- Generate email subjects from customer comments.
- Summarize customer comments.
- Perform sentiment analysis on customer comments.
- Generate full customer support emails.

## Setup Instructions

### Prerequisites

- Python 3.7+
- Flask
- OpenAI Python library
- Ensure you have an OpenAI API key

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/KM-Zubair/Customer_Support_System.git
    cd project-repo
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

    Create a `.env` file in the project root and add your OpenAI API key:

    ```env
    OPENAI_API_KEY=your_openai_api_key
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
├── products.json           # JSON file with product information
├── templates
│   └── index.html          # HTML template for the web interface
├── static
│   └── style.css           # CSS for styling (if any)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
