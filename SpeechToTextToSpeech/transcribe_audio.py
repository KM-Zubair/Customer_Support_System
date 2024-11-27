import torch
import whisper
import queue

def transcribe_audio(audio_queue, result_queue, model_name="base", english=False, wake_word="hey computer", verbose=False):
    """
    Transcribes audio using Whisper and checks for a wake word.
    """
    model = whisper.load_model(model_name + (".en" if english else ""))
    while True:
        audio_data = audio_queue.get()
        audio_tensor = torch.from_numpy(audio_data).float() / 32768.0
        result = model.transcribe(audio_tensor)
        text = result["text"]

        if text.lower().startswith(wake_word.lower()):
            command = text[len(wake_word):].strip()
            if verbose:
                print(f"Wake word detected: {command}")
            result_queue.put(command)
        else:
            if verbose:
                print("Wake word not detected.")
