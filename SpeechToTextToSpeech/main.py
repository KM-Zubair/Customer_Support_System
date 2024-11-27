import threading
import queue
import time
from config import init_api
from record_audio import record_audio
from transcribe_audio import transcribe_audio
from generate_reply import reply_to_query

def main():
    init_api()
    audio_queue = queue.Queue()
    result_queue = queue.Queue()

    # Start threads for audio recording, transcription, and reply generation
    threading.Thread(target=record_audio, args=(audio_queue,)).start()
    threading.Thread(target=transcribe_audio, args=(audio_queue, result_queue)).start()
    threading.Thread(target=reply_to_query, args=(result_queue,)).start()

    # Prevent the main thread from exiting
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")

if __name__ == "__main__":
    main()
