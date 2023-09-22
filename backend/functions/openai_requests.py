import openai
from decouple import config
import speech_recognition as sr

from functions.database import get_recent_messages

chatStr = ""

# Retrieve Enviornment Variables
# openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")

# Google Translate
# Convert audio to text
def convert_audio_to_text(audio_data, language_code):
    recognizer = sr.Recognizer()
    with sr.AudioFile("audio/input.wav") as source:
        recognizer.adjust_for_ambient_noise(source)  # Optional: Adjust for noise
        audio = recognizer.record(source, duration=len(audio_data) / 16000)
        try:
            text = recognizer.recognize_google(audio, language=language_code)
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

# Open AI - Whisper
# Convert audio to text
# def convert_audio_to_text(audio_file):
#   try:
#     transcript = openai.Audio.transcribe("whisper-1", audio_file)
#     message_text = transcript["text"]
#     return message_text
#   except Exception as e:
#     return

# Open AI - Chat GPT
# Convert audio to text
def get_chat_response(message_input):
  messages = get_recent_messages()
  print(messages)
  try:
    # global chatStr
    # chatStr = f"You: {message_input}\n SanjeevaniBot:"
    # print(chatStr)
    # response = openai.Completion.create(
    #     model="text-davinci-003",
    #     prompt=chatStr,
    #     temperature=0.7,
    #     max_tokens=256,
    #     top_p=1,
    #     frequency_penalty=0,
    #     presence_penalty=0
    # )
    # message_text = response["choices"][0]["text"]


    #use one of them
    
    # response = openai.ChatCompletion.create(
    #   model="gpt-3.5-turbo",
    #   messages=messages
    # )
    # message_text = response["choices"][0]["message"]["content"]
    return message_input
  except Exception as e:
    print(e)
    return
