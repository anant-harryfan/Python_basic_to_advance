from PyDictionary import PyDictionary
import pyttsx3
while True:
    dictionary = PyDictionary()
    x = input("Enter the word i will tell the meaning\n")
    a = dictionary.meaning(x)
    print(a)
    friend = pyttsx3.init()
    friend.say(a)
    friend.runAndWait()
    friend.stop()