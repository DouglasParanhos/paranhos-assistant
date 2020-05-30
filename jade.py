import speech_recognition as sr
import consult_action as actions
import time
import yaml

recognizer = sr.Recognizer()
microphone = sr.Microphone()

with open("assistant.yaml", "r") as ymlfile:
    cfg = yaml.load(ymlfile)


def listen():

    with microphone as source:
        while True:
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio, language='pt-BR')
                transcription = transcription.lower()
                
                if cfg["assistant"]["name"].lower() in transcription:
                    actions.checkAction(transcription)


            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

def init():
    cfg["greeting"][f'{cfg["assistant"]["name"]}']

init()