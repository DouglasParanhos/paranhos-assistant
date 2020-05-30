import speech_recognition as sr
import time
import yaml
import webbrowser as browser
import wikipedia

from gtts import gTTS
from subprocess import call

recognizer = sr.Recognizer()
microphone = sr.Microphone()
wikipedia.set_lang("pt")

with open("assistant.yaml", "r") as ymlfile:
    cfg = yaml.load(ymlfile)

def checkAction(audio):
    print(audio)
    if "browser" in audio:
        querySearch = audio.replace("browser", "").replace(" ", "+")
        browser.open_new(f'https://www.google.com/search?q={querySearch}')

    if "o que é" in audio or "quem é" in audio:
        querySearch = audio.replace("o que é", "").replace("quem é", "").\
                        replace("?","").strip().title()
        print(wikipedia.summary(querySearch, sentences=2))

def listen():

    with microphone as source:
        while True:
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio, language='pt-BR')
                transcription = transcription.lower()
                
                if cfg["assistant"]["name"].lower() in transcription:
                    checkAction(transcription)


            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

def create_audio(mensagem):
    tts = gTTS(mensagem, lang='pt-br')
    filePath = f'audios/{cfg["assistant"]["name"].lower()}/mensagem.mp3'
    tts.save(filePath)
    print(cfg["assistant"]["name"], ':', mensagem)
    call(['mpg123', '-q', filePath])

checkAction("o que é elton john?")