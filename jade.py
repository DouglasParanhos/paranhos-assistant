import speech_recognition as sr
import consult_action as actions
import time #to discover what time is it. ex.: currentH = int(datetime.datetime.now().hour) returns the hour 
import yaml
import random #to use random choices. ex.: random.choice(stMsgs)

recognizer = sr.Recognizer()
microphone = sr.Microphone()

with open("assistant.yaml", "r") as ymlfile:
    cfg = yaml.load(ymlfile)


def listen():

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        while True:
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio, language='pt-BR')
                transcription = transcription.lower()
                
                if cfg["assistant"]["name"].lower() in transcription:
                    print("Processando...")
                    actions.checkAction(transcription.replace(f'{cfg["assistant"]["name"]}', ''))

            except sr.UnknownValueError:
                print(".")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

def init():
    cfg["greeting"][f'{cfg["assistant"]["name"]}']

    listen()

init()
