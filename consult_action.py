import webbrowser as browser
import wikipedia
import sys

wikipedia.set_lang("pt")

def checkAction(audio):
    print(audio)
    audio = audio.lower()
    if "pesquisa no google " in audio:
        querySearch = audio.replace("pesquisa no google", "").replace(" ", "+")
        browser.open(f'https://www.google.com/search?q={querySearch}', autoraise=False)

    elif "pesquisa na wikipedia" in audio:
        querySearch = audio.replace("pesquisa na wikipedia ","").strip().title()
        try:
            print(wikipedia.summary(querySearch, sentences=2))
        except wikipedia.exceptions.PageError:
            print(f'Não achei {audio} na wikipedia')
        except wikipedia.exceptions.DisambiguationError:
            print(f'Achei mais de um resultado para {audio}')

    elif "mensagem" in audio:
        print("mensagem enviada")

    elif "tchau" in audio:
        print("tchau")
        sys.exit()

    else:
        print("Não entendi a ação")

checkAction("mensagem")