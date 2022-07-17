# The task you have to perform is to read the news using python. Build a program that will give you daily top 10 latest news. For that, you have to check the website  https://newsapi.org/ which gives the news API. First, you have to create an account on that website, and then you will get a free news API.

import requests
import json
from win32com.client import Dispatch

def speak(str):
    speaak = Dispatch("SAPI.SpVoice")
    speaak.Speak(str)

if __name__ == '__main__':

    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=33f4708b483a48d9b4a9ed068df97148"
    news = requests.get(url).text
    jsonwala = json.loads(news)
    art = jsonwala['articles']

    io = 0
    speak("Today's news is")
    for articles in art:
        io = io + 1
        print(f"{io}. {articles['title']}")
        speak({articles['title']})
        print("Full detail here")
        print(articles['url'])


        if io < 10:
            speak("Moving on the next news")
        else:
            print("Top 10 news ended")
            speak("Thanks for listening")
            break
            
