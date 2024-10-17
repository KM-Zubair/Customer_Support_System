#!/bin/bash

echo "Setting up and running the web crawler and QA system"

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install Python3 and try again."
    exit 1
fi

# Check if virtualenv is installed
if ! command -v virtualenv &> /dev/null
then
    echo "virtualenv is not installed. Installing virtualenv..."
    pip3 install virtualenv
fi

# Create and activate virtual environment
echo "Creating and activating virtual environment..."
virtualenv env
source env/bin/activate

# Install requirements
echo "Installing required packages..."
pip install -r requirements.txt

# Check if OPENAI_API_KEY is set
if [ -z "$OPENAI_API_KEY" ]
then
    echo "Please enter your OpenAI API key:"
    read api_key
    export OPENAI_API_KEY=$api_key
fi

# Run the crawler
echo "Running the web crawler..."
python3 crawler.py

# Run the QA system
echo "Starting the QA system..."
python3 app.py