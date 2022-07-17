# ~~~~~~~~~~~~~~~~~~~~~~~~~classes~~~~~~~~~~~~~~~~~~~~~~~~ #
# classes (school me agar har ek bachhe ke liye ek ek cheez(code yaha pe) hota to dikat ho jata isliye class banae gae takki same same cheeze alag alag nahi ek sath hi padhade)
# class Student:
# """Docstring"""
#     pass

# harry = Student()
# larry = Student()
# # instance variable hai ye
# harry.name = "Harry"
# harry.std = 12
# harry.section = 1
# larry.std = 9
# larry.subjects = ["hindi", "physics"]
# print(harry.section, larry.subjects)

# ~~~~~~~~~~~~~~~~~~~~~instance variable ~~~~~~~~~~~~~~~~~~~~~~ #
# class Employee:
#     no_of_leaves = 8
#     pass
#
# harry = Employee()
# rohan = Employee()
#
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"

# print(Employee.no_of_leaves)
# print(Employee.__dict__)  # dict dictionary batata(sabhi instance variable ko dictionary me bata deta)
# Employee.no_of_leaves = 9
# print(Employee.__dict__)
# print(Employee.no_of_leaves)

# ~~~~~~~~~~~~~~~~ Self & __init__() (Constructors) ~~~~~~~~~~~~~~~~~~~ #
# `````````````````````````` Self keyword ````````````````````````````````````` #
# The self keyword is used in the method to refer to the instance of the current class we are using. The self keyword is passed as a parameter explicitly every time we define a method.
# class Employee:
#     no_of_leaves = 8
#
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
#
#
# harry = Employee("Harry", 255, "Instructor")

# rohan = Employee()
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"

# print(harry.printdetails())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Class Methods~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# class Employee:
#     no_of_leaves = 8
#
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
#     @classmethod  # kabhi bas self nahi class ko kuch edit karna tah ye aata
#     def change_leave(cls, new_leaves):
#         cls.no_of_leaves = new_leaves
#
#
# harry = Employee("Harry", 255, "Instructor")
# rohan = Employee("Rohan", 4554, "Student")
# rohan.change_leave(35)
# print(harry.no_of_leaves)

# cls jo hai co atribute ko change nahi karta vo atribute ke class(yaha employee) me jake vaha pe jo value hai usse change karta
# jaise yaha hua rohan ki value change ki to harry ki bhi ho gae

# ~~~~~~~~~~~~~~~~~~~~~~~~~~Class Methods As Alternative Constructors~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# class Employee:
#     no_of_leaves = 8
#
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
#
#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves
#
#     @classmethod
#     def from_dash(cls, string):
#         # params = string.split("-")
#         # print(params)
#         # return cls(params[0], params[1], params[2])
#         return cls(*string.split("-"))  # istde akte hai args me yyaha pe split karke ek list return karega
#
#
# harry = Employee("Harry", 255, "Instructor")
# rohan = Employee("Rohan", 455, "Student")
# karan = Employee.from_dash("Karan-480-Student")
#
# print(karan.no_of_leaves)
# rohan.change_leaves(34)
#
# print(harry.no_of_leaves)

# ~~~~~~~~~~~~~~~~~~~Static Methods~~~~~~~~~~~~~~~~~~~~~~ #

# class Employee:
#     no_of_leaves = 8
#
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
#
#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves
#
#     @classmethod
#     def from_dash(cls, string):
#         return cls(*string.split("-"))
#
#     @staticmethod   # simple def func but in a class used to speed up code
#     def printgood(string):
#         print("This is good " + string)
#
# harry = Employee("Harry", 255, "Instructor")
# rohan = Employee("Rohan", 455, "Student")
# karan = Employee.from_dash("Karan-480-Student")
#
# Employee.printgood("Rohan")


# ~~~~~~~~~~~~~~~~~~~~Abstraction & Encapsulation ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# Abstraction
#
# Encapsulation
#
# Abstraction is used to solves the problem and issues that arise at the design stage.
#
# Encapsulation is used to solves the problem and issue that arise at the implementation stage.
#
# Abstraction focuses on what the object does instead of how the details are implemented.
#
# Encapsulation focuses on hiding the code and data into a single unit to secure the data from the outside world.
#
#  Abstraction can be implemented by using Interface and Abstract Class.
#
# Encapsulation can be implemented using Access Modifiers (Public, Protected, and Private.)
#
#   Its application is during the design level.
#
# Its application is during the Implementation level.

# sidhha sat -> aam khao gutliya mat gino

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Single Inheritance ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# class Employee:
#     no_of_leaves = 8
#
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
#
#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves
#
#     @classmethod
#     def from_dash(cls, string):
#         return cls(*string.split("-"))
#
#     @staticmethod
#     def printgood(string):
#         print("This is good " + string)
#
#
# class Programmer(Employee):
#     no_of_holiday = 56
#     def __init__(self, aname, asalary, arole, languages):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#         self.languages = languages
#
#
#     def printprog(self):
#         return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"
#
#
#
# harry = Employee("Harry", 255, "Instructor")
# rohan = Employee("Rohan", 455, "Student")
#
# shubham = Programmer("Shubham", 555, "Programmer", ["python"])
# karan = Programmer("Karan", 777, "Programmer", ["python", "Cpp"])
# print(karan.no_of_holiday)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Multiple Inheritance ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# class Employee:
#     no_of_leaves = 8
#     var = 8
#
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
#
#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves
#
#     @classmethod
#     def from_dash(cls, string):
#         return cls(*string.split("-"))
#
#     @staticmethod
#     def printgood(string):
#         print("This is good " + string)
#
# class Player:
#     var = 9
#     no_of_games = 4
#     def __init__(self, name, game):
#         self.name = name
#         self.game =game
#
#     def printdetails(self):
#         return f"The Name is {self.name}. Game is {self.game}"
#
# class CoolProgramer(Player, Employee):
#
#     language = "C++"
#     def printlanguage(self):
#         print(self.language)
#
# harry = Employee("Harry", 255, "Instructor")
# rohan = Employee("Rohan", 455, "Student")
#
# shubham = Player("Shubham", ["Cricket"])
# karan = CoolProgramer("Karan",["Cricket"])
# # det = karan.printdetails()
# # karan.printlanguage()
# # print(det)
# print(karan.var)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Multilevel Inheritance ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# class Dad:
#     basketball = 6
#
# class Son(Dad):
#     dance =1
#     basketball = 9
#     def isdance(self):
#         return f"Yes I dance {self.dance} no of times"
#
# class Grandson(Son):
#     dance = 6
#     guitar = 1
#
#     def isdance(self):
#         return f"Jackson yeah!" \
#             f"Yes I dance very awesomely {self.dance} no of times"
#
# darry = Dad()
# larry = Son()
# harry = Grandson()

# print(darry.guitar)

# electronic device
# pocket gadget
# phone

# class Electronic:
#     def tool(self):
#         return "You can use electronic as your new source"
#
# class PocketGadget(Electronic):
#     def pocket(self):
#         return "Can be come in pocket"
#
# class Phone(PocketGadget):
#     def Call(self):
#         return f"You can talk anywhere"
#     def feature(self):
#         return f"Phone feature are \n1. {self.pocket()}\n2. {self.tool()} \n3. {self.Call()}"
#
#
# ele = Electronic()
# poc = PocketGadget()
# ph = Phone()
#
# print(ph.feature())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Public, Private & Protected Access Specifiers ~~~~~~~~~~~~~~~~~~~~~ #

# Public - default kahi par bhi use kar sakte
# Protected - bas apki file ko acees hai isko use karna (koi import karke nahi kar sakta)
# Private - bas us class ko anumati hai isse use karne ki or koi nahi kar sakta

# class Employee:
#     no_of_leaves = 8
#     var = 8
#     _protec = 9   # to make protect variable use only 1 (_)
#     __pr = 98     # to make private variable use 2 (__)

    # def __init__(self, aname, asalary, arole):
    #     self.name = aname
    #     self.salary = asalary
    #     self.role = arole
    #
    # def printdetails(self):
    #     return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    # @classmethod
    # def change_leaves(cls, newleaves):
    #     cls.no_of_leaves = newleaves

    # @classmethod
    # def from_dash(cls, string):
    #     return cls(*string.split("-"))

    # @staticmethod
    # def printgood(string):
    #     print("This is good " + string)

# emp = Employee("harry", 343, "Programmer")
# print(emp._Employee__pr)  # private ko bhar access ese karte hai

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ Polymorphism ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# In basic English language, Polymorphism means to exist in different states. The same object or thing changing its state from one form to another is known as polymorphic. A same function or method, being used differently in different scenarios can perfectly describe polymorphism. It occurs mostly with base and derived class.

# print(5+6)         # ek hi cheez ko difrent tarike se likhna (output ka nahi pata)
# print("5" + "6")   # ek hi cheez ko difrent tarike se likhna (output ka nahi pata)

# Abstraction
# Encapsulation
# Inheritance
# Polymorphism
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Super() and Overriding In Classes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
class A:
    clasa = "I am in a"

    def __init__(self):
        self.clsu = "clasu"
        self.blasu = "blasu"

class B(A):
    blasa = "I am in class b"

    def __init__(self):
        # super().__init__() # agar tu yaha pe call karta to itna achha nahi hota matlab samaj line number  399 pe ja
        self.clsu = "b clasu"
        self.blasu = "b blasu"  # isne a wale ko override kar diya to jabh tu iske madat se a ka use karna chahata to nahi kar sakta
        # par ek method hai jisse kar sakte
        super().__init__()  # ab iski madat se hamne uper wale A ko call kar diya

a = A()
b = B()
print(b.blasu)



# bhai matlab dekh kya hota super se vo b wale func ko bhul kar a me chale jata phir uske sare func dekhta uske bad vo vapis b me aata or uske func dekhta   agar a ne koisa banaya hai or b ne same banaya hai to b ka call hoiga (override)
# or same esa agar tu nichhe karta to b ke sare func a se overide ho jate (super matlab samaj kahika portal)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Diamond problem ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# class A:
#     def met(self):
#         print("This is a method from class A")
#
# class B(A):
#     def met(self):
#         print("This is a method from class B")
#
# class C(A):
#     def met(self):
#         print("This is a method from class C")
#
# class D(C, B):
#     def met(self):
#         print("This is a method from class D")
#
#
# a = A()
# b = B()
# c = C()
# d = D()
#
# d.met()

 # for more info see this -> https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/python-tutorials-for-absolute-beginners-66/base64.png

 # bhai ab agli file me ja

 # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Operator Overloading ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
""" (https://docs.python.org/2/library/operator.html is link me jao or cheezo ke liye)
"+" ye hai bulit in function
par agar hame iske value ko change karna hai to kaise kare
ese -->
"""

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is         {self.role}"

emp1 =Employee("Harry", 345, "Programmer")
# emp2 =Employee("Rohan", 55, "Cleaner")
# print(emp1 + emp2)

# ab soch tujhe kuch esa karna hai ki jabh bhi koi emp1 ko print kare to printdetail print hi jae
# bina kuch kare
# print(emp1)  # isme kuch esa bataega <__main__.Employee object at 0x00000152A02F0FA0>
# ye karke  (    def {__repr__ or __str__}(self)...)
print(emp1)  # output aagaya "The Name is Harry. Salary is 345 and role is Programmer"

"""
__str__ and __repr__ functions
Both of these built-in methods are used to return a presentable description about any object rather than the default one. The difference in them is the way of writing them. The __str__ method is mainly written for the end-user, while __repr__ is written for a developer. It is overridden to return a printable string representation of any user-defined class. An interesting thing to note here is that the priority of __str__ is greater than __repr__. This means that if we pass an object into a print statement, it will return us the __str__ string even if __repr__ is also present there. In such cases, if we want to print __repr__, we have to call it exclusively with the object name in the print statement.
"""
