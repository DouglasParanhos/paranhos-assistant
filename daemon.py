import pyttsx3
import speech_recognition as sr
import time

engine = pyttsx3.init()
recognizer = sr.Recognizer()
microphone = sr.Microphone()

def initAssistant():
    setSpeechRate(150)
    setVolume(0.5)

    saluteUser()

def saluteUser():
    # engine.say("Hello my friend")
    # engine.say("what do you want to do?")
    engine.runAndWait()

    checkSettingsOk()

def checkSettingsOk():
    checkSpeechRate()
    checkVolume()

def checkSpeechRate():

    answer = ''

    while "yes" not in answer:
        engine.say("Is this speech rate ok?")
        engine.runAndWait()
        print("Listening...")

        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source,timeout=5)

            try:
                print("trying to decode")
                answer = recognizer.recognize_sphinx(audio)
                print(answer)

                if "up" in answer:
                    setSpeechRate(getSpeechRate() * 1.1)

                elif "down" in answer:
                    setSpeechRate(getSpeechRate() * 0.9)

                elif "stop" in answer:
                    break
            
            except sr.WaitTimeoutError:
                continue

            except sr.UnknownValueError:
                print("Sphinx could not understand audio")

def checkVolume():
    
    answer = ''

    while "yes" not in answer:
        engine.say("Is this volume ok?")
        engine.runAndWait()
        print("Listening...")

        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source,timeout=5)
            try:
                print("trying to decode")
                answer = recognizer.recognize_sphinx(audio)
                print(answer)

                if "up" in answer:
                    setSpeechRate(getSpeechRate() * 1.1)

                elif "down" in answer:
                    setSpeechRate(getSpeechRate() * 0.9)

                elif "stop" in answer:
                    break

            except sr.WaitTimeoutError:
                continue

            except sr.UnknownValueError:
                print("Sphinx could not understand audio")

def setSpeechRate(rate):
    engine.setProperty('rate', rate)

def getSpeechRate():
    return engine.getProperty('rate')

def setVolume(rate):
    engine.setProperty('volume',rate) 

def getVolume():
    return engine.getProperty('volume')

# def startDaemon():
#     while True:
#         print("")

if __name__ == '__main__':
    initAssistant()

    # startDaemon()
