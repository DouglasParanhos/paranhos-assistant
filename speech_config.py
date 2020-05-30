
import yaml
from gtts import gTTS
from subprocess import call

with open("assistant.yaml", "r") as ymlfile:
    cfg = yaml.load(ymlfile)

assistantName = cfg["assistant"]["name"]

def create_audio(mensagem):
    tts = gTTS(mensagem, lang='pt-br')
    filePath = f'audios/{.lower()}/mensagem.mp3'
    tts.save(filePath)
    print(assistantName, ':', mensagem)
    call(['mpg123', '-q', filePath])