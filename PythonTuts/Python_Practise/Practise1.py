# Problem Statement:-
# Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).
current_year = 2021
last_year = current_year - 99
def age_calcu(a, b, c):
    if age > a:
        print("Have you come from future, Enter correct inputEnter correct input")
    elif age <= b:
        print("You are not born, Enter correct input")
    elif c == 4:
        print(f"You will be turn 100 in {age + 100}")
    elif c == 2 or 1:
        bornn_year = current_year - age
        print(f"You will turn to 100 in {bornn_year+100}")

age = int(input("Enter your age or Enter your birth year\n"))
p = len(str(age))
if p == 2 or p == 1:
    age_calcu(98, 0, p)
elif p == 4:
    age_calcu(current_year, last_year, p)
elif p == 3:
    print("Have you come from future")

boool = input("Do you want to see your age in random years\n")
if boool == "yes" or boool == "Yes":
    random_year = int(input("Tell the year you want to see your age\n"))
    born_year = current_year - age
    if p == 2:
        print(f"You will turn {random_year - born_year} in {random_year}")
    elif p == 4:
        print(f"You will turn {random_year - age} in {random_year}")
else:
    print("Thanks for visiting my code")
#
# Here are a few instructions that you must have to follow:
#
# Do not use any type of module like DateTime or date utils. (-5 points)
# Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
# Your code should handle all sorts of errors like :            (2 points)
# You are not yet born
# You seem to be the oldest person alive
# You can also handle any other errors, if possible!
