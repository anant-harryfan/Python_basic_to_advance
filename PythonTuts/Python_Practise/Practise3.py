# You visited a restaurant called CodeWithHarry, and the food items in that restaurant are sorted, based on their amount of calories. You have to reserve this list of food items containing calories.
#
# You have to use the following three methods to reserve a list:
#
# In build method of python
# List name [::-1] slicing trick
# Swap the first element with the last one and second element with second last one and so on like,
# [6 7 8 34 5] -> [5 34 8 7 6]
#
#
#
# Input:
# Take a list as an input from the user
#
# [5, 4, 1]
#
# Output:
# [1, 4, 5]
#
# [1, 4, 5]
#
# [1, 4, 5]
#
# All three methods give the same results!
import time
listu = input("Enter the list\n")
# split karta , ke hisabse
listi = listu.split(", ") and listu.split(",")  # and listu.split(" ,")
# print(listi)
option = input("Enter:\n1 for build in method\n2 for slicing method\n3 for main_sol method\n")
if option == "1":
    print("You typed 1 so we are reversing the list by built in method...")
    listi.reverse()
    time.sleep(1)
    print(listi)
elif option == "2":
    print("You typed 2 so we are reversing the list by slicing method...")
    b = listi[::-1]
    time.sleep(1)
    print(b)
elif option == "3":
    print("You have typed 3 so we are reversing the list by main_sol method...")

    reverse3 = listi[:]
    for i in range(len(reverse3) // 2):
        # first value last se change or last wali 1st se change
        reverse3[i], reverse3[len(reverse3) - i - 1] = reverse3[len(reverse3) - i - 1], reverse3[i]
    time.sleep(1)
    print(reverse3)

