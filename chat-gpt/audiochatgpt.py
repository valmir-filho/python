# Imports

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import openai


# Functions.

# Converting text into speech and playing the corresponding audio
def text_to_speech(text, output_file):
    tts = gTTS(text, lang="pt")
    tts.save(output_file)
    playsound(output_file)


# Get a textual response from a question using the OpenAI GPT-3.5 language model.
def get_answer(question):

    openai.api_key = 'your_api_key'

    answer = openai.Completion.create(
        engine='text-davinci-003',
        prompt=question,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )

    return answer.choices[0].text.strip()


# Speech recognition through a microphone.
rec = sr.Recognizer()

with sr.Microphone(1) as mic:
    rec.adjust_for_ambient_noise(mic)
    text_to_speech("Olá! Que bom você por aqui! Como eu posso te ajudar?", "recording.mp3")
    audio = rec.listen(mic)
    text = rec.recognize_google(audio, language="pt-BR")

# Stores the audio, in text form.
text_storage = text
# Send the text as a question to OpenAI GPT-3.5.
answer = get_answer(text_storage)
# Generate the audio response.
answer_audio_file = "answer.mp3"

text_to_speech(answer, answer_audio_file)
