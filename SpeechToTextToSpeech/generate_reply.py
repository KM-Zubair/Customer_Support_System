import openai
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os
import time

# Cache for query responses
response_cache = {}

def reply_to_query(result_queue, stop_word="stop", verbose=False):
    """
    Generates a reply using OpenAI's GPT and converts it to speech using gTTS.
    Includes caching and stop word handling.
    """
    while True:
        question = result_queue.get()

        # Stop word detection
        if stop_word.lower() in question.lower():
            print("Stop word detected. Interrupting response.")
            continue

        # Check cache for previous responses
        if question in response_cache:
            answer = response_cache[question]
            if verbose:
                print("Cached response used.")
        else:
            prompt = f"Q: {question}?\nA:"
            try:
                response = openai.Completion.create(
                    model="text-davinci-002",
                    prompt=prompt,
                    temperature=0.5,
                    max_tokens=100,
                    stop=["\n"]
                )
                answer = response["choices"][0]["text"].strip()
                response_cache[question] = answer  # Cache the result
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
