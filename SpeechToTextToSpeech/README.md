# Real-time Speech to Text to Speech: Building Your AI-Based Alexa

This project demonstrates how to build a real-time AI voice assistant capable of transcribing speech to text, generating intelligent responses, and converting the response back into speech. The system integrates OpenAI GPT for generating text responses and OpenAI's Text-to-Speech for audio output. It also incorporates document-based retrieval functionality for answering questions from specific sources, enhancing its capability to provide accurate and contextual responses.

---

## Presentation Slides
- [Real-time Speech to Text to Speech Using OpenAI GPT and Text-to-Speech](https://docs.google.com/presentation/d/1CbL2lFYBnSoTADHjQwgMuR8LvWWeAMimzO6QSCxSjxI/edit?usp=sharing)

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup Instructions](#setup-instructions)
   - [Dependencies](#dependencies)
   - [Environment Variables](#environment-variables)
   - [Running the Application](#running-the-application)
5. [Usage](#usage)
6. [Folder Structure](#folder-structure)
7. [Future Enhancements](#future-enhancements)

---

## Project Overview
The **Real-time Speech to Text to Speech** project simulates an AI assistant with the following workflow:
1. **Voice Input**: The user interacts via a microphone, starting with a wake word like "Hey Computer."
2. **Speech-to-Text**: OpenAI Whisper transcribes the voice input into text.
3. **Document-Based Retrieval**: Queries related to specific documents are resolved using a conversational retrieval system.
4. **Response Generation**: OpenAI GPT generates intelligent responses based on the query.
5. **Text-to-Speech**: OpenAI's Text-to-Speech converts the response to audio, which is then played back to the user.

The system provides a visually appealing web interface for both welcoming users and facilitating real-time interaction.

---

## Features
### **Core Functionalities**:
- **Real-Time Interaction**:
  - Transcribes speech to text using OpenAI Whisper.
  - Resolves queries via document-based conversational retrieval or GPT for fallback responses.
  - Plays responses using OpenAI's Text-to-Speech.

- **Web Interface**:
  - **Landing Page**: A polished welcome screen (`index.html`) with a button to start interaction.
  - **Interaction Page**: A real-time interaction page (`interaction.html`) with dynamic status updates and loading indicators.

- **Document-Based Support**:
  - Answers questions from specific sources (PDF, YouTube transcript, or URLs).
  - Implements conversational retrieval using LangChain and ChromaDB.

### **Enhanced User Experience**:
- Modern UI with a gradient background, animations, and responsive design.
- Feedback on system status, including success and error messages.

---

## Technologies Used
- **Programming Language**: Python
- **Backend**: Flask
- **APIs**:
  - OpenAI Whisper for speech-to-text transcription.
  - OpenAI GPT for generating text-based responses.
  - OpenAI Text-to-Speech for converting text to audio.
- **Frontend**:
  - Embedded CSS for styling.
  - Embedded JavaScript for interactivity.
- **Document-Based Retrieval**:
  - LangChain for conversational retrieval.
  - ChromaDB for vector storage and retrieval.
- **Audio Processing**: PyDub, SpeechRecognition.

---

## Setup Instructions

### Dependencies
Install the required Python libraries:
```bash
pip install openai whisper langchain chromadb pydub speechrecognition flask
```

### Environment Variables
Create a `.env` file in the project root and include the following API credentials:
```
API_KEY=<your_openai_api_key>
ORG_ID=<your_openai_organization_id>
```

### Running the Application
Run the application:
```bash
python app.py
```

Access the system via `http://127.0.0.1:5000` in your web browser.

---

## Usage
1. **Landing Page**:
   - Visit `http://127.0.0.1:5000`.
   - Click the "Start Talking" button to navigate to the interaction page.

2. **Interaction Page**:
   - Click the "Start Interaction" button to start the voice assistant.
   - Speak into the microphone and view real-time feedback.
   - Ask questions related to documents or general queries.

---

## Folder Structure
```
project-root/
├── app.py                 # Flask backend application
├── config.py              # API initialization and environment setup
├── sfbu_support.py        # Library for document-based conversational retrieval (Step 1 logic)
├── record_audio.py        # Handles recording audio from the microphone
├── transcribe_audio.py    # Handles transcription using Whisper
├── generate_reply.py      # Enhances response generation with document-based retrieval and GPT
├── templates/             # HTML templates for the frontend
│   ├── index.html         # Landing page
│   └── interaction.html   # Interaction page
├── requirements.txt       # Python dependencies
└── .env                   # Environment variables
```

---

## Future Enhancements
1. **Voice Embeddings**:
   - Use voice embeddings for personalized interactions.
2. **Audio Streaming**:
   - Stream responses directly for faster playback without saving to disk.
3. **Multi-Language Support**:
   - Expand transcription and response generation to multiple languages.
4. **Advanced Controls**:
   - Include additional features like pause/resume and custom wake words.
5. **Integration with APIs**:
   - Connect with other APIs (e.g., calendars, weather services) for extended functionality.

---