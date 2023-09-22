import io
import tempfile

import speech_recognition as sr
import os
import win32com.client
import webbrowser
import datetime
import openai
from config import apikey
from pydub import AudioSegment
import random


chatStr = ""
speaker = win32com.client.Dispatch("SAPI.SpVoice")
openai.api_key = apikey

def handle_health_query(query):
    if "cough" in query:
        print("Jeevan: I see you have a cough. Let me ask you a few questions to better understand your condition.\n")
        speaker.Speak("I see you have a cough. Let me ask you a few questions to better understand your condition.")
        print("Jeevan: How long have you had this cough?\n")
        speaker.Speak("How long have you had this cough?")
        duration = takeCommanden()
        print("Jeevan: Is your cough dry, or do you produce mucus?\n")
        speaker.Speak("Is your cough dry, or do you produce mucus?")
        cough_type = takeCommanden()
        print("Jeevan: Do you have a fever or any other symptoms along with the cough?\n")
        speaker.Speak("Do you have a fever or any other symptoms along with the cough?")
        other_symptoms = takeCommanden()
        # You can add more questions here based on the user's responses
        print("Jeevan: Thank you for providing that information. Based on your answers, it's advisable for you to Boil fresh ginger slices in water, Add honey and drink this ginger tea to reduce coughing or you can Inhale steam from a bowl of hot water. Remember that these remedies can provide relief for mild coughs. If your cough persists, worsens, or is accompanied by severe symptoms, it's essential to consult a healthcare professional for a proper diagnosis and treatment.\n")
        speaker.Speak("Thank you for providing that information. Based on your answers, it's advisable for you to Boil fresh ginger slices in water, Add honey and drink this ginger tea to reduce coughing or you can Inhale steam from a bowl of hot water.Remember that these remedies can provide relief for mild coughs. If your cough persists, worsens, or is accompanied by severe symptoms, it's essential to consult a healthcare professional for a proper diagnosis and treatment.\n")
    elif "headache" in query:
        print("Jeevan: I see you have a headache. Let me ask you a few questions to better understand your condition.\n")
        speaker.Speak("I see you have a headache. Let me ask you a few questions to better understand your condition.")
        print("Jeevan: How long have you had this headache?\n")
        speaker.Speak("How long have you had this headache?")
        duration = takeCommanden()
        print("Jeevan: Can you describe the type of headache? Is it a dull ache, throbbing pain, or something else?\n")
        speaker.Speak("Can you describe the type of headache? Is it a dull ache, throbbing pain, or something else?")
        headache_type = takeCommanden()
        print("Jeevan: Are you experiencing any other symptoms along with the headache, such as nausea or sensitivity to light?\n")
        speaker.Speak("Are you experiencing any other symptoms along with the headache, such as nausea or sensitivity to light?")
        other_symptoms = takeCommanden()
        print("Jeevan: Thank you for providing that information. Based on your answers, it's advisable for you to rest in a quiet, dark room, and consider taking over-the-counter pain relievers if needed. If your headache persists or worsens, or if you experience severe symptoms, it's essential to consult a healthcare professional for a proper diagnosis and treatment.\n")
        speaker.Speak("Thank you for providing that information. Based on your answers, it's advisable for you to rest in a quiet, dark room, and consider taking over-the-counter pain relievers if needed. If your headache persists or worsens, or if you experience severe symptoms, it's essential to consult a healthcare professional for a proper diagnosis and treatment.\n")
        # You can add similar handling for other health issues here
    elif "stomach ache" in query:
        print("Jeevan: I see you have a stomach ache. Let me ask you a few questions to better understand your condition.\n")
        speaker.Speak("I see you have a stomach ache. Let me ask you a few questions to better understand your condition.")
        print("Jeevan: How long have you had this stomach ache?\n")
        speaker.Speak("How long have you had this stomach ache?")
        duration = takeCommanden()
        print("Jeevan: Can you describe the type of pain? Is it a cramp, a constant ache, or something else?\n")
        speaker.Speak("Can you describe the type of pain? Is it a cramp, a constant ache, or something else?")
        pain_type = takeCommanden()
        print("Jeevan: Have you recently eaten something unusual or had any food-related issues?\n")
        speaker.Speak("Have you recently eaten something unusual or had any food-related issues?")
        food_related = takeCommanden()
        # You can add more questions here based on the user's responses
        print("Jeevan: Thank you for providing that information. Based on your answers, it's advisable for you to rest, drink clear fluids, and avoid heavy or spicy foods. If your stomach ache persists, worsens, or if you experience severe symptoms, it's essential to consult a healthcare professional for a proper diagnosis and treatment.\n")
        speaker.Speak("Jeevan: Thank you for providing that information. Based on your answers, it's advisable for you to rest, drink clear fluids, and avoid heavy or spicy foods. If your stomach ache persists, worsens, or if you experience severe symptoms, it's essential to consult a healthcare professional for a proper diagnosis and treatment.\n")

    elif "fever" in query:
        print("Jeevan: I see you have a fever. Let me ask you a few questions to better understand your condition.\n")
        speaker.Speak("I see you have a fever. Let me ask you a few questions to better understand your condition.")
        print("Jeevan: What is your current body temperature?\n")
        speaker.Speak("What is your current body temperature?")
        temperature = takeCommanden()
        print("Jeevan: Are you experiencing any other symptoms along with the fever, such as cough, headache, or body aches?\n")
        speaker.Speak("Are you experiencing any other symptoms along with the fever, such as cough, headache, or body aches?")
        other_symptoms = takeCommanden()
        print("Jeevan: Have you recently traveled or been in close contact with someone who tested positive for an infectious disease?\n")
        speaker.Speak("Have you recently traveled or been in close contact with someone who tested positive for an infectious disease?")
        travel_history = takeCommanden()
        # You can add more questions here based on the user's responses
        print("Jeevan: Thank you for providing that information. Based on your answers, it's advisable to rest, stay hydrated, and take over-the-counter fever-reducing medication if needed. If your fever persists, worsens, or if you develop severe symptoms, it's essential to consult a healthcare professional for a proper diagnosis and treatment.\n")
        speaker.Speak("Thank you for providing that information. Based on your answers, it's advisable to rest, stay hydrated, and take over-the-counter fever-reducing medication if needed. If your fever persists, worsens, or if you develop severe symptoms, it's essential to consult a healthcare professional for a proper diagnosis and treatment.\n")

def chat(query):
    global chatStr
    print(chatStr)
    chatStr += f"You: {query}\n Eleven: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    ai_response = response["choices"][0]["text"]



    print("Jeevan:",ai_response)  # Print AI response

    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(ai_response)  # Speak AI response
    chatStr += f"{ai_response}\n"
    chatStr = ""
    return ai_response

speaker = win32com.client.Dispatch("SAPI.SpVoice")


import pyttsx3

import pyttsx3

import pyttsx3


from gtts import gTTS
import pygame
import os


''''
def say1(text, lang='hi'):
    tts = gTTS(text=text, lang=lang)
    tts.save("temp.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

# Use the say function to speak in Hindi
#print("मैं हिंदी में बोल सकता हूँ।")
say1("मैं हिंदी में बोल सकता हूँ।")
#say1("मैं हिंदी में बोल सकता हूँ।")
#say1("नमस्कार,मैं हूँ इलेवन, कूल जेनजी एआई बॉट, जिसे प्रेरणा जोशी ने विकसित किया है")
'''


'''
from gtts import gTTS
from playsound import playsound

def say(text, lang='hi-in'):
    tts = gTTS(text=text, lang=lang)
    tts.save("temp.mp3")
    playsound("temp.mp3")
    os.remove("temp.mp3")
'''







def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommandhi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.5
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="hi-IN")

            print(f"user: {query}")
            return query
        except Exception as e:
            print("Sorry, I couldn't understand. Apologies from Eleven.")
            return ""

def takeCommanden():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.5
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-IN")

            print(f"user: {query}")
            return query
        except Exception as e:
            print("Sorry, I couldn't understand. Apologies from Eleven.")
            return ""

from langdetect import detect

if __name__ == '__main__':
    #print("नमस्कार, मैं हूँ इलेवन, कूल जेनजी एआई बॉट, जिसे प्रेरणा जोशी ने विकसित किया है")
    #say1("नमस्कार, मैं हूँ इलेवन, कूल जेनजी एआई बॉट, जिसे प्रेरणा जोशी ने विकसित किया है")
    #say1("मैं हिंदी में बोल सकता हूँ।")
    print("Hey, I am Jeevan, a telemedicine  BOT developed by Government of Kerala")
    say("Hey, I am Jeevan, a telemedicine  BOT developed by Government of Kerala")
    while True:
        command = takeCommanden().lower()
        if "exit" in command:
            #say("Okay, Goodbye!")
            break
        elif "cough" in command or "having fever" in command or "having stomach" in command or "having headache" in command:
            handle_health_query(command)
            print("Jeevan: take care")
            say("take care")
            break

        say("You said: " + command)

        #say1("आपने कहा: " + command)
        print("Chatting...")
        chat(command)





