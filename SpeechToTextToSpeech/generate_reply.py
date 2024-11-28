import openai
from pydub import AudioSegment
from pydub.playback import play
import os
from sfbu_support import load_documents, split_documents, create_vectorstore, setup_conversation_chain

# Initialize document-based conversational retrieval
documents = load_documents()
chunks = split_documents(documents)
vectorstore = create_vectorstore(chunks)
conversation_chain, memory = setup_conversation_chain(vectorstore)

# Cache for query responses
response_cache = {}

def reply_to_query(result_queue, stop_word="stop", verbose=False):
    """
    Enhances the reply logic to integrate document-based conversational retrieval
    while replacing gTTS with OpenAI's Text-to-Speech.
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
            # Try document-based conversational retrieval first
            try:
                answer = conversation_chain.run(question, memory=memory)
                if verbose:
                    print("Answer retrieved from document-based conversation chain.")
            except Exception as e:
                if verbose:
                    print(f"Document retrieval error: {e}")
                answer = None

            # Fallback to OpenAI GPT if no document-based response is found
            if not answer or answer.strip() == "":
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
                    if verbose:
                        print("Answer retrieved from OpenAI GPT.")
                except Exception as e:
                    answer = "I'm sorry, I couldn't process your request."
                    if verbose:
                        print(f"GPT error: {e}")

            # Cache the result
            response_cache[question] = answer

        # Replace gTTS with OpenAI's Text-to-Speech
        try:
            tts_response = openai.Audio.create(
                model="text-to-speech",
                text=answer,
                voice="en-US-Wavenet-D"  # Adjust the voice as needed
            )
            audio_file = "reply.wav"
            with open(audio_file, "wb") as f:
                f.write(tts_response["audio_content"])

            # Play the audio
            audio = AudioSegment.from_file(audio_file, format="wav")
            play(audio)
            os.remove(audio_file)
        except Exception as e:
            print(f"Error with OpenAI TTS: {e}")
