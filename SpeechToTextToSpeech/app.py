from flask import Flask, request, jsonify, render_template
from record_audio import record_audio
from transcribe_audio import transcribe_audio
from generate_reply import reply_to_query
import threading
import queue
import os

app = Flask(__name__)

# Initialize queues for audio and text processing
audio_queue = queue.Queue()
result_queue = queue.Queue()

@app.route("/")
def index():
    """
    Landing page for the assistant.
    """
    return render_template("index.html")

@app.route("/interaction")
def interaction():
    """
    Interaction page where the real-time assistant runs.
    """
    return render_template("interaction.html")

@app.route("/chat", methods=["POST"])
def chat():
    """
    Endpoint to process text-based chat input (document retrieval + GPT).
    """
    user_input = request.json.get("message")
    result_queue.put(user_input)  # Add the user input to the processing queue

    # Process the query and get the response
    try:
        response = result_queue.get(timeout=5)  # Wait for the processing result
        return jsonify({"response": response})
    except queue.Empty:
        return jsonify({"response": "I'm sorry, I couldn't process your request at this time."}), 500

@app.route("/start", methods=["POST"])
def start_assistant():
    """
    Start the assistant's real-time audio processing threads.
    """
    try:
        # Start threads for audio recording, transcription, and reply generation
        threading.Thread(target=record_audio, args=(audio_queue,), daemon=True).start()
        threading.Thread(target=transcribe_audio, args=(audio_queue, result_queue), daemon=True).start()
        threading.Thread(target=reply_to_query, args=(result_queue,), daemon=True).start()
        return jsonify({"status": "Assistant started successfully!"})
    except Exception as e:
        return jsonify({"status": f"Error starting assistant: {str(e)}"}), 500

if __name__ == "__main__":
    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv()

    # Run the Flask app
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
