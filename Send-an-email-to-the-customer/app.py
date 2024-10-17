import os
import json
from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

# Initialize the OpenAI client using the API key from the environment
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

# Define common languages used in the US
languages = ['English', 'Spanish', 'Chinese', 'Tagalog', 'Vietnamese', 'Arabic', 'French']

# Load products from the JSON file
def load_products():
    with open('products.json') as f:
        products = json.load(f)
    return products

@app.route('/', methods=['GET', 'POST'])
def chat():
    products = load_products()
    selected_action = ''  # Initialize selected_action
    selected_language = 'English'  # Set default language
    response = ''

    if request.method == 'POST':
        # Get language and question from the form
        selected_language = request.form.get('language', 'English')
        selected_action = request.form.get('action')  # Get selected action from form
        user_question = request.form['question']

        # Send question to ChatGPT
        response = answer_question(user_question)

    return render_template('index.html', response=response, products=products, languages=languages, selected_language=selected_language, selected_action=selected_action)


@app.route('/generate_comment', methods=['POST'])
def generate_comment():
    products = load_products()
    selected_language = request.form['language']
    selected_action = 'generate-comment-section'  # Set selected action
    selected_product = request.form['product']
    product_info = products.get(selected_product)

    if not product_info:
        return render_template('index.html', response="Product not found", products=products, languages=languages, selected_language=selected_language, selected_action=selected_action)

    # Generate customer comment
    comment = generate_customer_comment(product_info, selected_language)
    return render_template('index.html', comment=comment, products=products, languages=languages, selected_language=selected_language, selected_action=selected_action)


def generate_customer_comment(product_info, language):
    description = product_info['description']
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a customer of an electronics store. Please respond in {language}."},
                {"role": "user", "content": f"Here is a product description: {description}. Please generate a 100-word customer comment about this product."}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"


@app.route('/generate_subject', methods=['POST'])
def generate_subject():
    products = load_products()
    selected_language = request.form.get('language', 'English')
    customer_comment = request.form.get('comment')
    selected_action = 'generate-subject-section'  # Set selected action

    if not customer_comment:
        return render_template('index.html', comment=customer_comment, subject="No comment provided.", products=products, languages=languages, selected_language=selected_language, selected_action=selected_action)

    subject = generate_email_subject(customer_comment, selected_language)
    return render_template('index.html', comment=customer_comment, subject=subject, products=products, languages=languages, selected_language=selected_language, selected_action=selected_action)

def generate_email_subject(comment, language):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a customer support assistant."},
                {"role": "user", "content": f"Here is a customer's comment: {comment}. Please generate a short and relevant email subject in {language} based on this comment."}
            ],
            temperature=0.7,
            max_tokens=50
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"



@app.route('/generate_summary', methods=['POST'])
def generate_summary():
    products = load_products()
    selected_language = request.form.get('language', 'English')
    customer_comment = request.form['comment']
    selected_action = 'generate-summary-section'  # Set selected action

    summary = generate_comment_summary(customer_comment, selected_language)
    return render_template('index.html', comment=customer_comment, summary=summary, products=products, languages=languages, selected_language=selected_language, selected_action=selected_action)

def generate_comment_summary(comment, language):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a helpful assistant. Please respond in {language}."},
                {"role": "user", "content": f"Here is a customer's comment: {comment}. Please summarize this comment."}
            ],
            temperature=0.7,
            max_tokens=100
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"


@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    products = load_products()
    selected_language = request.form.get('language', 'English')
    customer_comment = request.form['comment']
    selected_action = 'analyze-sentiment-section'  # Set selected action

    sentiment = perform_sentiment_analysis(customer_comment, selected_language)
    return render_template('index.html', comment=customer_comment, sentiment=sentiment, products=products, languages=languages, selected_language=selected_language, selected_action=selected_action)

def perform_sentiment_analysis(comment, language):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a sentiment analysis assistant. Please respond in {language}."},
                {"role": "user", "content": f"Here is a customer's comment: {comment}. Please analyze the sentiment (positive, negative, or neutral)."}
            ],
            temperature=0.0,
            max_tokens=10
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/generate_email', methods=['POST'])
def generate_email():
    products = load_products()
    selected_language = request.form.get('language', 'English')
    customer_comment = request.form.get('comment')
    summary = request.form.get('summary')
    sentiment = request.form.get('sentiment')
    email_subject = request.form.get('subject')
    selected_action = 'generate-email-section'  # Set selected action

    email = generate_customer_email(customer_comment, summary, sentiment, email_subject, selected_language)
    return render_template('index.html', comment=customer_comment, summary=summary, sentiment=sentiment, subject=email_subject, email=email, products=products, languages=languages, selected_language=selected_language, selected_action=selected_action)

def generate_customer_email(comment, summary, sentiment, subject, language):
    try:
        # Compose the request to ChatGPT to generate the full email
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a customer support assistant. Please respond in {language}."},
                {"role": "user", "content": f"""
                    Please create an email in {language} to be sent to the customer based on the following:

                    1. The customer's comment: \"\"\"{comment}\"\"\"
                    2. The summary of the customer's comment: \"\"\"{summary}\"\"\"
                    3. The result of the sentiment analysis: \"\"\"{sentiment}\"\"\"
                    4. The Subject of the email: \"\"\"{subject}\"\"\"
                    
                    The email should include:
                    - The summary of the customer's comment.
                    - A response that addresses the customer’s sentiment and expands on their comment.
                    """}
            ],
            temperature=0.7,
            max_tokens=300
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"




if __name__ == '__main__':
    app.run(debug=True)
