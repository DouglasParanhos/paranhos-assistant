import webbrowser as browser
import wikipedia

wikipedia.set_lang("pt")

def checkAction(audio):
    print(audio)
    if "browser" in audio:
        querySearch = audio.replace("browser", "").replace(" ", "+")
        browser.open_new(f'https://www.google.com/search?q={querySearch}')

    if "o que é" in audio or "quem é" in audio:
        querySearch = audio.replace("o que é", "").replace("quem é", "").\
                        replace("?","").strip().title()
        print(wikipedia.summary(querySearch, sentences=2))