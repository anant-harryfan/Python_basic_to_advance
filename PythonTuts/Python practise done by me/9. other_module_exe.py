# import pyfiglet
# out = pyfiglet.figlet_format("I  am \nProgrammer ")
# print(out)
# output -  ___
#
# |_ _|    __ _ _ __ ___
#  | |    / _` | '_ ` _ \
#  | |   | (_| | | | | | |
# |___|   \__,_|_| |_| |_|
#
#  ____
# |  _ \ _ __ ___   __ _ _ __ __ _ _ __ ___  _ __ ___   ___ _ __
# | |_) | '__/ _ \ / _` | '__/ _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
# |  __/| | | (_) | (_| | | | (_| | | | | | | | | | | |  __/ |
# |_|   |_|  \___/ \__, |_|  \__,_|_| |_| |_|_| |_| |_|\___|_|
#                  |___/
#
#
# thumbnail downloader
# import ytimg
# import urllib.request
#
# thubhUrl = ytimg.get("https://www.youtube.com/watch?v=8-e1htTLHSI&t=6s")
# urllib.request.urlretrieve(thubhUrl, 'thumb.jpg')
#
# spell checker
# from textblob import TextBlob
# speller = input("Enter the word which you want to check\n")
# print(f"Original text: {str(speller)}")
#
# b = TextBlob(speller)
# print(f"Correct text: {str(b.correct())}")
#
# output: Original text: glas
#         Correct text: glad
#
# instaram id loader
# import instaloader
# ig = instaloader.Instaloader()
# dp = input("Enter the Username: ")
# ig.download_profile(dp, profile_pic_only=True)
# output : my full information came when i input my id
#
# newspaper
# import newspaper
# url = 'https://copyassignment.com/15-common-coding-mistakes-by-beginners'
# url_i = newspaper.Article(url="%s" % url, language='en')
# url_i.download()
# url_i.parse()
# print(url_i.text, end=" ")
# output tell all things in website (it should be informative website which support this otherwise it will not run)
#
# phone number detector
# import phonenumbers
# from phonenumbers import geocoder, carrier, timezone
#
# phoner = input("Enter your number:\n") # tell the code also like in india it is +91{number}
# phone_number = phonenumbers.parse(phoner)
# # print the country name
# print(geocoder.description_for_number(phone_number, 'en'))
# # this will print the service provider
# print(carrier.name_for_number(phone_number, 'en'))
# # this will print the timezone
# print(timezone.time_zones_for_number(phone_number))
# output: all info of phone number
#
# ip address
# built in
# import socket
# hostname = socket.gethostname()
# IPAddrs = socket.gethostbyname(hostname)
# print(hostname)  # tell your name if comp belong to you
# print(f"My IP address:\n{IPAddrs}")  # tell ip address
#
# captcha creator
# from captcha.image import ImageCaptcha
# image = ImageCaptcha(width=280, height=98)
# captcha = text = "Anant The Coder"
# data = image.generate("bruh")
# image.write(captcha, "9._Captcha.png")
#
# shoutdown computer
# import os
# os.system("shutdown now - h")
#
# source code of any website
# import urllib.request
# print(urllib.request.urlopen(input("Enter the website url:\n")).read())