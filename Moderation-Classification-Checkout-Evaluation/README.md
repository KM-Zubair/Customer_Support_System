# Customer Support System with OpenAI ChatGPT API

This project implements a Customer Support System that leverages OpenAI's ChatGPT API to moderate input, classify service requests, and answer customer questions using **Chain of Thought Reasoning**. The project is built using Python (Flask) for the backend and uses HTML/CSS for the frontend interface.

## [Presentation Slides](https://docs.google.com/presentation/d/1L_g4zw8f4YyRu5dIMp1oqZVhxe0B5vtqb-jsjk_9DwA/edit#slide=id.g2fc51b79cda_0_0)

## Features
1. **Input Moderation**: Checks customer input for inappropriate content.
2. **Service Request Classification**: Classifies customer messages into predefined categories.
3. **Answering Questions using Chain of Thought Reasoning**: Provides step-by-step answers to customer questions by breaking down the reasoning process.
4. **Evaluation of Responses**: Checks and evaluates the generated responses for factual accuracy and relevance.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your machine.
- An OpenAI API key. You can obtain one by creating an account at [OpenAI](https://beta.openai.com/signup/).
- Flask framework installed. You can install Flask by running:
  ```bash
  pip install flask
  ```
- A `.env` file containing your OpenAI API key:
  ```bash
  OPENAI_API_KEY=your_openai_api_key_here
  ```

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/customer-support-system.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd customer-support-system
    ```

3. **Install required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Add OpenAI API Key**:
   - Create a `.env` file in the root directory and add your OpenAI API key:
     ```bash
     touch .env
     echo "OPENAI_API_KEY=your_openai_api_key" >> .env
     ```

## Running the Project

1. **Start the Flask Server**:
   
   Run the following command to start the Flask development server:

   ```bash
   python app.py
   ```

2. **Access the Application**:

   Once the server is running, open your web browser and go to:

   ```
   http://127.0.0.1:5000
   ```

## Project Structure

```bash
.
├── app.py               # Flask application for backend
├── templates
│   └── index.html       # Frontend HTML interface
├── static               # CSS and JavaScript for the frontend
├── products.json        # Product data used in the project
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (OpenAI API key)
└── README.md            # Project README file
```

## API Endpoints

### `POST /answer_question`
- **Description**: Accepts a customer question and returns an answer using Chain of Thought reasoning.
- **Request Body**:
  ```json
  {
    "message": "Your question here"
  }
  ```
- **Response**:
  ```json
  {
    "response": "Response to the customer"
  }
  ```

## Example Request

Here’s an example of how to send a POST request to the `/answer_question` endpoint using `curl`:

```bash
curl -X POST http://127.0.0.1:5000/answer_question -H "Content-Type: application/json" -d '{"message": "by how much is the BlueWave Chromebook more expensive than the TechPro Desktop?"}'
```

## Frontend

The project includes a simple frontend to input customer queries:

1. **Step 3: Answering User Questions using Chain of Thought**:
   - The user enters their question in a text box, and the system uses OpenAI’s GPT model to respond.
   - This functionality can be accessed from the main page of the project.

## Deployment

1. **Production Deployment**:
   For deployment, ensure that your Flask app is hosted on a web server like `gunicorn` or `uwsgi` and behind a reverse proxy like `nginx`. You may also use a service like Heroku or AWS Elastic Beanstalk to deploy your application.

2. **Serving Static Files**:
   - Ensure that your `static` files (CSS, JS) and `templates` (HTML) are properly served when deploying in production.





