# Customer Support System

This project implements a web-based Customer Support System that uses web crawling and AI-powered question answering to provide automated support for a website. 
[Presentation Slides](https://docs.google.com/presentation/d/1rKsmLHrEnVa7QTwT4w_B78AbU5fJGyFYbgopWkpXD_c/edit?usp=sharing)

## Project Overview

The Customer Support System consists of three main components:

1. **Web Crawler**: Scrapes content from a specified website.
2. **QA System**: Processes the scraped content and answers user questions using OpenAI's GPT model.
3. **Web Interface**: Allows users to interact with the QA system through a simple web application.

## Files in the Project

- `crawler.py`: Web crawler that fetches and processes content from the target website.
- `qa_system.py`: Implements the question-answering system using OpenAI's API.
- `app.py`: Flask web application that serves as the user interface.
- `requirements.txt`: Lists all Python dependencies for the project.
- `run.sh`: Shell script to set up and run the project.

## Prerequisites

- Python 3.7 or higher
- OpenAI API key

## Setup and Installation

1. Clone this repository to your local machine.

2. Navigate to the project directory.

3. Run the setup script:
   ```
   ./run.sh
   ```
   This script will:
   - Create a virtual environment
   - Install required dependencies
   - Prompt for your OpenAI API key if not set
   - Run the web crawler
   - Start the web application

   Note: If you encounter any permission issues with `run.sh`, you may need to make it executable using `chmod +x run.sh`.

4. Alternatively, you can set up the project manually:
   ```
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   export OPENAI_API_KEY='your-api-key-here'
   python crawler.py
   python app.py
   ```

## Usage

1. After running `run.sh` or `python app.py`, the web interface will be available at `http://localhost:5000`.

2. Enter your question in the provided input field and click "Ask" to get an answer.

3. The system will process your question, search through the crawled content, and provide an answer using the AI model.

## Customization

- To crawl a different website, modify the `domain` and `full_url` variables in `crawler.py`.
- Adjust the QA system parameters in `qa_system.py` to fine-tune the answer generation process.

## Troubleshooting

- If you encounter any issues with package installation, ensure you have the latest version of pip: `pip install --upgrade pip`
- For OpenAI API issues, verify that your API key is correct and you have sufficient quota.

## Contributing

Contributions to improve the Customer Support System are welcome. Please feel free to submit pull requests or open issues to discuss potential enhancements.
