import openai
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

def reply_to_query(result_queue, verbose=False):
    """
    Generates a reply using OpenAI's GPT and converts it to speech using gTTS.
    """
    while True:
        question = result_queue.get()
        prompt = f"Q: {question}?\nA:"
        try:
            response = openai.Completion.create(
                model="text-davinci-002",
                prompt=prompt,
                temperature=0.5,
                max_tokens=100,
                stop=["\n"]
            )
            answer = response["choices"][0]["text"]
        except Exception as e:
            answer = "I'm sorry, I couldn't understand the question."
            if verbose:
                print(f"Error: {e}")
        
        # Convert text to speech
        tts = gTTS(text=answer, lang="en", slow=False)
        tts.save("reply.mp3")
        audio = AudioSegment.from_mp3("reply.mp3")
        play(audio)
        os.remove("reply.mp3")
