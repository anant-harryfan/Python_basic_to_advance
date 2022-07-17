"""
You have to take an integer type variable, and the input of the variable will define the length of the triangle.
You have to declare another Boolean variable.

*
**
***
****

When the value of Boolean is 1 i.e. True, the pattern will be printed as shown above.
But if the value of Boolean is 0 or false, then the triangle will be printed upside down.
"""

d = int(input("Enter the rows you want\n"))
e = bool(int(input("Enter 0 for false and 1 for true\n")))

def star(d, e):
    if e == True:
        c = 1
        while c <= d:
            print(c * "*")
            c = c + 1
    else:
        while d > 0:
            print(d * "*")
            d = d - 1


star(d, e)


