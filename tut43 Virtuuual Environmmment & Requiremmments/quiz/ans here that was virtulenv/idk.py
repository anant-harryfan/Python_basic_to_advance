# def calculator(a, b, c):
#     if c == "+":
#          return print(f"Your ans is: \n{a+b}")
#     elif c == "*":
#          return print(f"Your ans is: \n{a*b}")
#     elif c == "-":
#          return print(f"Your ans is: \n{a-b}")
#     elif c == "/":
#         return print(f"Your ans is: \n{a/b}")
        
# print("Enter the number")
# n = int(input())
# print("Enter 2nd number")
# g = int(input())
# print("Tell what you want to do *,/,+,-")
# f = input()

# while True:
#     calculator(n,g,f)

import math

a = int(input("Enter a\n"))
b = int(input("Enter b\n"))
c = int(input("Enter c\n"))
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f"Your area is = \n{area} and s is = \n{s}")