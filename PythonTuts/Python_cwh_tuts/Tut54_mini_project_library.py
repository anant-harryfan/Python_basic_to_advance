# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input



class Library:

    def __init__(self, name, book_list):
        self.name = name
        self.book_list = book_list
        self.lend_book = []
# display kar vata
    def display_book(self):
        print("BOOKs - ")
        num = 1
        # if self.book_list > 5:
        #     print("You can't make library more than 5 books")
        # else:
        for item in self.book_list:
            print(f"{num}. {item}")
            num = num + 1
    # lend karvata
    def lendd_book(self, book):
        self.lend_book.append(book)
        self.book_list.remove(book)
        with open("tut54_lended_book", "a") as lb:
            lb.write(f"You rent {book} at {time.asctime(time.localtime(time.time()))} \n")
    # return karvata
    def return_book(self, book):
        if book not in self.lend_book:
            print("This book has not been rented to anyone\nif this is wrong so pls contact us on discord")
        elif book in self.lend_book:
            self.book_list.append(book)
            self.lend_book.remove(book)
            print("You successfully return the book")
            num = 1
            # ye batata ki kitne book or dene hai
            if len(self.lend_book) > 0:
                for bukku in self.lend_book:
                    print(f"These books are left to give back to library{num}. {bukku}")
                    num = num+1
        with open("tut54_lended_book", "a") as lb:
            lb.write(f"You return {book} at {time.asctime(time.localtime(time.time()))} \n")
    # add karvata
    def add_book(self, book):
        self.book_list.append(book)
        print(f"Book [{book}] successfully added to library")
# variables
money = 0
name_lib = "anant-library"
price = [5000, 600, 450, 550, 1000, 2000]
bookk_list = ["Harry bhai - 5000rs", "Python - 800rs", "Harry potter - 1000rs", "Java - 600rs", "C++ - 450rs", "Vinay Patrika - 2000rs"]
anant_lib = Library(name_lib, bookk_list)
namee = input("Enter your name - ")
info = f"\nLibrary Name: {name_lib}\n\nOwner: Anant \n\nBhopal Ranking: 2nd\n\nBooks we have: 2,50,000\n\nDiscord Server: https://discord.gg/wPC7n38TsE"
                                                      # because 1st is always harry-lib
# imports
import time
import random
import datetime
import calendar
from PyDictionary import PyDictionary

def get_time():
    return datetime.datetime.now()

from datetime import datetime
timi = time.asctime(time.localtime(time.time()))
timii = datetime.now()
while True:
    print(f"Welcome {namee} to {name_lib}")
    print(f"{namee} has {money}rs now")
    input_t = input("(0) Cash - to make money\n(1) Display - to display books\n(2) Lend Book - to lend books\n(3) return - to return books\n(4) Add Book - to add books\n(5) Dictionary - You can use online dictionary here\n(6) Calculator - You can use online calculator here\n(7) Time Spent - tell how much time you spent till now \n(8) Calender - You can use a year calender here\n(9) Info - to see info about this libary\n(10) Quit - to exit this library\n")  # isme kar bhai func ke use
    # cash func
    if input_t == "0":
        if money <= 5000:
            cash = random.randint(500, 700)
            money = money + cash
            print(f"{namee} you earned {cash}rs this time")
            # print(f"Now you have {money}rs")
        elif money > 5000:
            print(f"{namee} you can't make more money, You already have 5000+ rs")
            # print(money)

    # display func
    elif input_t == "1":
        print(f"{name_lib} has these many books\n")
        anant_lib.display_book()
    # lend func
    elif input_t == "2":
        try:
            bk_lend = input("Enter name of the book like this format - \n [{book_name} - {price}rs] - example Harry bhai - 5000rs\n")
            # batata ki bk_lend hai ki nahi lib me
            book_find = bk_lend in bookk_list
            # print(book_find)
            inndexx = bookk_list.index(bk_lend)
            # print(inndexx) # isme index aajaega int me
            PRICE = price[inndexx]  # to agar indexx 1 hai to price 1 ko selec karlo
            # print(PRICE - 20)

            if book_find:
                # money system
                if money >= PRICE:
                    money = money - PRICE
                    anant_lib.lendd_book(bk_lend)
                    print(f"Successfully bought the book {bk_lend}")
                elif money < PRICE:
                    print("You Don't Have Money. PLS type (0) to make money")
            elif not book_find:
                print(f"There is no book like {bk_lend} in our library now\n it is owned by {namee}")
        except:
            print(f"There is no book like {bk_lend} in our library")
    # return book func
    elif input_t == "3":
        boooooks = input("Enter name of the book which you want to return like this format - \n [{book_name} - {price}rs] - example Harry bhai - 5000rs\n")
        anant_lib.return_book(boooooks)
    # donate func
    elif input_t == "4":
        try:
            BOOK = input("Enter book name you want to donate in this format\n[{book} - {price}rs]\n")
            # split karke book ko book wali list me dalta or price ko price wali list me
            faku_pricecc = BOOK.split("-")[1]
            # print(faku_pricecc)
            pricesssssss = int(faku_pricecc.split("rs")[0])

            price.append(pricesssssss)
            # print(price)
            anant_lib.add_book(BOOK)
        except:
            print("Pls write book name in right way \n[{book} - {price}rs] eg - Harry bhai - 5000rs")
    # dictionary
    elif input_t == "5":

        dictionary = PyDictionary()
        x = input("Welcome to online dictionary \nEnter thee word to get the meaning \n")
        a = dictionary.meaning(x)
        print(a)
    # calculator
    elif input_t == "6":
        print("Welcome to online calculator")

        def calculator():
            if c == "*":
                print("The ans is", a * b)
            elif c == "+":
                print("The ans is", a + b)
            elif c == "-":
                print("The ans is", a - b)
            elif c == "/":
                print("The ans is", a / b)
            else:
                print("Pls put a valid statement")
        while True:
            d = input("If you want to quit Type 'quit' here or you want to continue type anything\n")
            if d == "quit":
                break
            print("Enter 1st number")
            a = int(input())
            print("Enter 2st number")
            b = int(input())
            print("Enter what you have to do *, /, +, -")
            c = input()
            calculator()
            if d == "quit":
                break
    # hours spend
    elif input_t == "7":
        timmmi = time.asctime(time.localtime(time.time()))
        timmi = datetime.now()
        print(f"You come to library at {timi} and ended at {timmmi}")
        hour = timmi - timii
        h2 = int(hour.total_seconds() / 60 ** 2)
        h3 = int(hour.total_seconds() / 60 * 2)
        print(f"You spend {h2} hours and {h3} minutes till now")
    # calender
    elif input_t == "8":
        year = int(input("Enter the year\n"))
        print(f"The calendar of year {year} is : \n")
        print(calendar.calendar(year, 2, 1, 6))
    # info
    elif input_t == "9":
        print(f"The info of this library is\n{info}")
        print("Pls join our discord server\n")
    # tata - bye bye
    elif input_t == "10":
        print("Thank you to come to my library")
        break
    time.sleep(2)  # mane ye isliye lagaya taki user jo hai vo cheeze padh pae varna agge ka ekdam se run hota to kuch samaj nahi aata

# bhai aap discord chalao bhhot kam aayega pls, aap apne subscriber se bhi puch sakte ki unhe chahiye ki nahi pls