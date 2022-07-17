# Problem Statement:-
# It's result day at school and not everyone is happy. You decided to make your friends laugh by jumbling their names to come up with some funny names.
#
# Your program should take the number of names and the names separated by space as input. Output should be funny names in the same order.
#
#
#
# Input:
# Enter number of friends:
#
# 3
#
# Enter the name of your 3 friends:
#
# Rohan Das
#
# Shubham Agarwal
#
# Ritesh Arora
#
# Output:
# Ritesh Das
#
# Shubham Arora
#
# Rohan Agarwal
import random
print("Welcome to jumbled name")
# i = int(input("Enter the numbers of people\n"))
name = input("Enter names with surname (pls put ',')\n")
# lol = name.split(", ")
# print(lol)
nama = name.split(" ")
namee = nama[::2]
surnme = nama[::-2]
# print(surnme)
for i in range(len(nama)):
    b = random.choice(namee)
    # print(b)
    c = random.choice(surnme)
    d = b + " " + c
    print(d)