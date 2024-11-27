import speech_recognition as sr
import queue

def record_audio(audio_queue, energy=300, pause=0.8, dynamic_energy=False):
    """
    Records audio from the microphone and puts it into an audio queue.
    """
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = energy
    recognizer.pause_threshold = pause
    recognizer.dynamic_energy_threshold = dynamic_energy

    with sr.Microphone(sample_rate=16000) as source:
        print("Listening...")
        while True:
            try:
                audio = recognizer.listen(source)
                audio_queue.put_nowait(audio.get_raw_data())
            except Exception as e:
                print(f"Error recording audio: {e}")