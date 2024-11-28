# Cybersecurity: Anomaly Detection (Classification Without Examples)

This project demonstrates how to build a cybersecurity anomaly detection system using generative AI. The system processes web server logs, generates vector embeddings for similarity-based classification, and identifies whether a new log entry is anomalous or normal. It includes a Flask-based web interface for interaction.

---

## [Presentation Slides](https://docs.google.com/presentation/d/12_FRpNJjY1wypXGc8DB285NvrhZ-O4_7rq0aKDqz-QM/edit?usp=sharing)


---

## **Table of Contents**
1. **Project Overview**
2. **Features**
3. **Technologies Used**
4. **Setup Instructions**
   - **Dependencies**
   - **Environment Variables**
   - **Running the Application**
5. **Usage**
6. **Folder Structure**

---

## **Project Overview**
- **Goal**: Detect anomalies in web server logs using similarity-based classification without labeled examples.
- **Core Features**:
  - Processes structured and unstructured log data.
  - Builds a vector database of normal log entries.
  - Uses similarity thresholds to classify new log entries as anomalous or normal.
- **Web Interface**:
  - Provides an easy-to-use web interface for submitting log entries and viewing results.

---

## **Features**
### **Core Functionalities**:
1. **Log Preprocessing**:
   - Parses raw web server logs into structured JSON format.
2. **Vector Embedding**:
   - Uses OpenAI embeddings to represent logs in vector space.
3. **Anomaly Detection**:
   - Compares new logs against normal embeddings using similarity thresholds.
4. **Web Interface**:
   - Flask-based frontend for log submission and real-time detection.

### **Enhanced User Experience**:
- Displays whether a log is anomalous or normal.
- Provides feedback directly in the browser.

---

## **Technologies Used**
1. **Programming Language**: Python
2. **Backend**: Flask
3. **APIs**:
   - OpenAI embeddings for vectorization.
4. **Vectorstore**:
   - ChromaDB for efficient similarity searches.
5. **Frontend**:
   - Embedded CSS and JavaScript for interaction.

---

## **Setup Instructions**

### **Dependencies**
Install the required Python libraries:
```bash
pip install openai langchain chromadb flask python-dotenv
```

### **Environment Variables**
Create a `.env` file in the project root and include the following API credentials:
```
OPENAI_API_KEY=<your_openai_api_key>
```

### **Running the Application**
Run the application:
```bash
python app.py
```

Access the system via `http://127.0.0.1:5000` in your web browser.

---

## **Usage**
1. **Landing Page**:
   - Provides an introduction to the anomaly detection system.
   - Click the "Start Detection" button to navigate to the detection page.

2. **Detection Page**:
   - Enter a web server log entry in the text area.
   - Click "Check Anomaly" to classify the log.
   - View the classification result (anomalous or normal).

---

## **Folder Structure**
```
cybersecurity-anomaly-detection/
├── app.py                     # Flask backend application
├── config.py                  # API initialization and environment setup
├── anomaly_detection.py       # Core logic for training and detecting anomalies
├── log_preprocessor.py        # Parses and preprocesses web server logs
├── vectorstore.py             # Handles vector database for log embeddings
├── templates/                 # HTML templates for frontend
│   ├── index.html             # Landing page
│   └── detection.html         # Anomaly detection interaction page
├── requirements.txt           # Python dependencies
├── webserver_logs/            # Directory for storing sample log data
│   ├── normal_logs.txt        # Sample normal traffic logs
└── .env                       # Environment variables
```

---
