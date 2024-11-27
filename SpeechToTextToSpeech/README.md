# Real-time Speech to Text to Speech: Building Your AI-Based Alexa

This project demonstrates how to build a real-time AI voice assistant capable of transcribing speech to text, generating intelligent responses, and converting the response back into speech. The system integrates OpenAI GPT for generating text responses and Google Text-to-Speech (gTTS) for audio output. It provides an engaging and intuitive way to interact with AI through voice.

## Presentation Slides
- [Real-time Speech to Text to Speech Using gTTS and OpenAI GPT](https://docs.google.com/presentation/d/1CbL2lFYBnSoTADHjQwgMuR8LvWWeAMimzO6QSCxSjxI/edit?usp=sharing)

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup Instructions](#setup-instructions)
   - [Dependencies](#dependencies)
   - [Data Preparation](#data-preparation)
   - [Running the Application](#running-the-application)
5. [Usage](#usage)
6. [Folder Structure](#folder-structure)
7. [Future Enhancements](#future-enhancements)

---

## Project Overview
This project simulates the behavior of a personal AI assistant, similar to Alexa, but enhanced with OpenAI's GPT capabilities. It uses:
- OpenAI Whisper for speech-to-text transcription.
- GPT models to provide intelligent responses.
- Google Text-to-Speech (gTTS) for converting text responses to audio.

The assistant can answer questions, engage in simple conversations, and provide feedback audibly.

---

## Features
- Real-time voice input using a microphone.
- Transcription of speech to text via OpenAI Whisper.
- Intelligent response generation using OpenAI GPT models.
- Conversion of responses to audio using gTTS.
- Support for wake words and stop words for better control.
- Caching of repeated queries for faster responses.
- Error handling for robust performance.

---

## Technologies Used
- **Programming Language**: Python
- **APIs**: OpenAI GPT and Whisper, Google Text-to-Speech (gTTS)
- **Audio Processing**: PyDub, SpeechRecognition
- **Concurrency**: Python threading
- **Additional Tools**: Queue for communication between threads

---

## Setup Instructions

### Dependencies
Install the required Python libraries:
```bash
pip install openai whisper pydub speechrecognition gtts
```

### Data Preparation
No external datasets are required. Ensure `.env` contains your API credentials:
```
API_KEY=<your_openai_api_key>
ORG_ID=<your_openai_organization_id>
```

### Running the Application
Run the main program:
```bash
python main.py
```

---

## Usage
1. Launch the application using the command above.
2. Use your microphone to ask a question after the wake word, e.g., "Hey computer, what is the capital of France?"
3. Listen to the response played via the speakers.

---

## Folder Structure
```
project-root/
├── config.py              # API initialization and environment setup
├── record_audio.py        # Handles recording audio from the microphone
├── transcribe_audio.py    # Transcribes audio using OpenAI Whisper
├── generate_reply.py      # Generates responses and converts them to audio
├── main.py                # Orchestrates the entire workflow
├── requirements.txt       # List of dependencies (optional)
└── .env                   # Environment variables for API keys
```

---

## Future Enhancements
- Implement voice embeddings for personalized user interaction.
- Stream audio responses for faster playback without saving to disk.
- Add more control features like pause, resume, and custom wake words.
- Integrate with other APIs like calendars or messaging platforms for additional functionality.

---