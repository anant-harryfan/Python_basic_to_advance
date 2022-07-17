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
print("Enter 1st number")
a = int(input())
print("Enter 2st number")
b = int(input())
print("Enter what you have to do *, /, +, -")
c = input()
calculator()