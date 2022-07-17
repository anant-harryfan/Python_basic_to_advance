from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        return 0

    @abstractmethod  # iska matlab jo bhi is class ko inherite karega uske nader ye walke method hone hi chahiye (its an order)
    def param(self):
        return 0

class Rectangle(Shape):
    def __init__(self):
        self.len = int(input("Enter length\n"))
        self.bre = int(input("Enter breath\n"))

    def area(self):
        return self.len * self.bre

    def param(self):
        return 2 * (self.len + self.bre)

idk = Rectangle()
print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ area ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n{idk.area()}")
print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ parameter ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n{idk.param()}")

# YOU CAN'T CREATE YOUR OWN OBJECT USING ABSTRACT BASE CLASS
# SHAPE = Shape()
# print(SHAPE)

# OUTPUT -
# Traceback (most recent call last):
#   File "C:\Users\xyz\PycharmProjects\PythonTuts\tut51_Abstract_Base_Class_&_@abstractmethod.py", line 28, in <module>
#     SHAPE = Shape()
# TypeError: Can't instantiate abstract class Shape with abstract methods area, param