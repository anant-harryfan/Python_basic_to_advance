from pynput.keyboard import Key, Controller
import webbrowser
import wikipedia
import pyttsx3
import datetime
import speech_recognition as sr
import os
import random
import smtplib
from instabot import Bot
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.mouse import Button, Controller
import pywhatkit

# pls dlt config file before running programe
# os.chmod("C:\\Users\\xyz\\PycharmProjects\\PythonTuts\\Projects\\config", 0o777)
# os.remove("C:\\Users\\xyz\\PycharmProjects\\PythonTuts\\Projects\\config")
mouse = Controller()
keyboard = Controller()
true = False
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
name = "Anant"
engine.setProperty('voice', voices[0].id)
def speck(audio):
    """ Help to computer to speck """
    engine.say(audio)
    engine.runAndWait()
def wish_me():
    """This function wish the user"""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speck(f"Good Morning {name}")
        print(f"Good Morning {name}")
    elif 12 <= hour < 18:
        speck(f"Good AfterNoon {name}")
        print(f"Good AfterNoon {name}")
    elif 18 <= hour < 24:
        speck(f"Good Night {name}")
        print(f"Good Night {name}")
    speck(f"I am Jarvis {name}, Please tell how may i help you...")
    print(f"I am Jarvis {name}, Pls tell how may i help you...")
def takeCommand():
    """Help to enter user command by specking"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        r.pause_threshold = 1
        r.energy_threshold = 100

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"{name} said: {query}")

    except:
        # print(e)
        print(f"Jarvis can't understand what you say, Pls type it down")
        query = input("Enter query here\n")
        return query
    # query = input("Order Jarvis")
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('anantchandak5@gmail.com', 'master0820k')
    server.sendmail('anantchandak5@gmail.com', to, content)
    server.close()
if __name__ == '__main__':
    wish_me()
    print("Pls press ENTER to continue")
    speck("Please press ENTER to continue")

    while True:
        enter = input()
        if enter == "":
            query = takeCommand().lower()
            # print(query)
            # if query == "None":
            #     query = input('Enter query here\n')
            # logic to executing tasks based on query
            if "wikipedia" in query:
                query = query.replace("wikipedia", "")
                speck(f"Searching {query} on wikipedia...")
                results = wikipedia.summary(query, sentences=2)
                print(f"According to wikipedia {results}")
                speck(f"According to wikipedia {results}")
            elif "open" in query:
                openafter = query.split(" ")
                try:
                    webu = openafter[openafter.index("open") + 1]
                    if webu == "stack":
                        webbrowser.get(chrome_path).open("stackoverflow.com")
                    realwebu = str(webu) + ".com"
                    webbrowser.get(chrome_path).open(realwebu)

                except:
                    print("There is a problem to open your website")
                    speck("There is a problem to open your website")
                # print(realwebu, type(realwebu))
            elif "play music" in query:
                music_dir = 'C:\\Users\\xyz\\OneDrive\\Desktop\\songs'
                songs = os.listdir(music_dir)
                rand = random.randint(0, len(songs) - 1)
                print(songs[rand])
                os.startfile(os.path.join(music_dir, songs[rand]))
            elif "the time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(f'{name} the time is {strTime}')
                speck(f'{name} the time is {strTime}')
            elif "start code" in query:
                codePath = "C:\\Users\\xyz\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            elif 'email to' in query:
                try:
                    speck("Please tell to whom you have to send email")
                    to = input("Pls tell to whom you have to send email \n")
                    speck("What should I say?")
                    print("If you want to type your email just say 'want to type' and nothing else")
                    content = takeCommand()
                    if "want to type" == content.lower() or content.lower() == "wanted to type":
                        content = input("Type here:\n")
                    print(f"You send email to {to} whose content is: \n{content} \nPls tell me that your content is correct or not than i will send this email (Y/N)")
                    correct = input()
                    if correct == "Y" or correct == "y":
                        sendEmail(to, content)
                        print("Email has been sent!")
                        speck("Email has been sent!")
                    elif correct == "N" or correct == "n":
                        print("Ok we will not send this email")
                    else:
                        print("Pls give ans in Y/N or y/n (note: don't type yes or no just y or n)")
                except Exception as e:
                    print(e)
                    speck("Sorry my friend anant bhai. I am not able to send this email")
            elif 'send' and 'message' in query:
                speck("Please tell on which platform you have to message")
                platform = input("Please tell on which platform you have to message:\n").lower()
                if platform == "instagram":
                    print("To whom you want to send message")
                    speck("To whom you have to send message")
                    person = input()
                    speck("What message you want to send")
                    print("If you want to type just say 'want to type':")
                    mes = takeCommand().lower()
                    if mes == "wanted to type" or mes == "want to type" or mes == "i want to type":
                        mes = input("Type here: \n")
                    # print(mes)
                    # bot = Bot()
                    print(f"You send message to {person} whose content is: \n{mes} \nPls tell me that your content is correct or not than i will send this mes (Y/N)")
                    correctu = input()
                    if correctu == "Y" or correctu == "y":
                        bot = Bot()
                        bot.login(username="anant_the_coder", password="anant0820k")
                        bot.send_message(mes, person)

                        speck("Successfully send the message")
                        print("Successfully send the message")
                    elif correctu == "N" or correctu == "n":
                        print("Ok we will not send this mes")
                    else:
                        print("Pls give ans in Y/N or y/n (note: don't type yes or no just y or n)")
                elif platform == "whatsapp":
                    print("At what number you want to send message")
                    speck("At what number you want to send message")
                    person = input()
                    print("On which time I should send this message")
                    # speck("On which time I should send this message")
                    time = "0:1"
                    c = time.split(":")
                    hour = int(c[0])
                    mint = int(c[1])
                    speck("What message you want to send")
                    print("If you want to type just say 'want to type':")
                    mes = takeCommand().lower()
                    if mes == "wanted to type" or mes == "want to type" or mes == "i want to type":
                        mes = input("Type here: \n")
                    # print(mes)
                    # bot = Bot()
                    print(
                        f"You send message to {person} whose content is: \n{mes} \nPls tell me that your content is correct or not than i will send this mes (Y/N)")
                    correctu = input()
                    if correctu == "Y" or correctu == "y":
                        pywhatkit.sendwhatmsg(person, mes, hour, mint)
                        speck("Successfully send the message")
                        print("Successfully send the message")
                    elif correctu == "N" or correctu == "n":
                        print("Ok we will not send this mes")
                    else:
                        print("Pls give ans in Y/N or y/n (note: don't type yes or no just y or n)")
            elif "stop" in query:
                print(int("a"))
            elif "meeting" in query:
                path = 'C:\\Program Files (x86)\\chromedriver.exe'
                options = Options()
                options.add_argument("user-data-dir=C:\\Users\\xyz\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
                driver = webdriver.Chrome(executable_path=path, chrome_options=options)
                driver.get("https://meet.google.com/mma-hvvv-wwu?authuser=0")
                time.sleep(5)
                try:
                    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "GOH7Zb")))
                    time.sleep(10)
                    element.click()
                    print("Camera stop")
                    speck("Camera stop")
                    element2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ZB88ed")))
                    time.sleep(3)
                    element2.click()
                    print("microphone stop")
                    speck("microphone stop")
                    element3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".Y5sE8d")))
                    time.sleep(3)
                    element3.click()
                    print("Successfully joined meeting")
                    speck("Successfully joined meeting")
                    true = True
                except:
                    # driver.quit()
                    # print(e)
                    speck("There is a problem to join meeting")
                    print("There is a problem to join meeting")

            elif true and "microphone" in query:
                keyboard.press(Key.ctrl)
                keyboard.press("d")
                keyboard.release(Key.ctrl)
                keyboard.release("d")
                print("Microphone started")
                speck("Microphone started")

            elif true and "video" in query:
                keyboard.press(Key.ctrl)
                keyboard.press("e")
                keyboard.release(Key.ctrl)
                keyboard.release("e")
                print("Camera started")
                speck("Camera started")

            elif true and "present" in query:
                mouse.position = (-716, 713)
                mouse.press(Button.left)
                mouse.release(Button.left)
                speck("Presentation started")
                print("Presentation started")

            # elif "quit" or "q" in query:
            #     speck(f"Thanks for using jarvis {name}")
            #     print(f"Thanks for using jarvis {name}")
            #     break