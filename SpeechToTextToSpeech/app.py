from flask import Flask, render_template, jsonify
from threading import Thread
import queue
from config import init_api
from record_audio import record_audio
from transcribe_audio import transcribe_audio
from generate_reply import reply_to_query

app = Flask(__name__)

# Queues for communication
audio_queue = queue.Queue()
result_queue = queue.Queue()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/interaction")
def interaction():
    return render_template("interaction.html")

@app.route("/start", methods=["POST"])
def start_assistant():
    # Start threads for recording, transcription, and reply
    Thread(target=record_audio, args=(audio_queue,)).start()
    Thread(target=transcribe_audio, args=(audio_queue, result_queue)).start()
    Thread(target=reply_to_query, args=(result_queue,)).start()
    return jsonify({"status": "Assistant started"})

if __name__ == "__main__":
    init_api()  # Initialize API
    app.run(debug=True)
