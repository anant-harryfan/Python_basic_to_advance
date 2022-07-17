print("What is your age")
age = input()
print("What is your brothers age")
bage = input()

try:
    print("You are", int(bage) - int(age),      "Years smaller than you brother")
except Exception as e:
    print("Teri age dal zayada shanna bana na uda dunga \n")
    print(e, "\n")

print("Chutta nahi hai agge badh")