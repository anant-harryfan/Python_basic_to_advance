# Health Management System
# 3 clients - Anant, Arnav, Shrey


# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client


# bhai ye rha program
# mere client hai anant, arnav and shrey ek food or exe ka anant or dusare food exe ka arnav or tisara food exe ka shrey
# ab dekho hame kya karna hai ki mujhe anant me exercise deni hai(input by user) to vo input phir anant exe.txt me save hojae(matlab likh de) phir uske sath sath phele time aaye ki kabh mane ye kiya, or phir uaske bad ek esa func chalana hai jisse me dekh pau ki mane kya likha tha us file me vo yaha print ho jae

# Health Management System
# 3 clients - Harry, Rohan and Hammad

def getdate():
    import datetime
    return datetime.datetime.now()


# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client


# bhai ye rha program
import datetime


def gettime():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("tut32 harry-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("tut32 harry-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("tut32 rohan-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("tut32 rohan-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("tut32 hammad-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("tut32 hammad-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(harry),2(rohan),3(hammad)")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("tut32 harry-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("tut32 harry-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("tut32 rohan-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("tut32 rohan-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("tut32 hammad-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("tut32 hammad-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (harry,rohan,hammad)")


print("health management system: ")
a = int(input("Press 1 for log the value and 2 for retrieve "))

if a == 1:
    b = int(input("Press 1 for harry 2 for rohan 3 for hammad "))
    take(b)
else:
    b = int(input("Press 1 for harry 2 for rohan 3 for hammad "))
    retrieve(b)

