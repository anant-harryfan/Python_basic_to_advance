"""
esa karna hai ki inspect module ki madat se ek class ko alag alag tarike se view karna
jaise ek class ke bas instace variable print karva
ya
attribute ko print kare
ya
class variable ko print kare
ya
purre ko print karva ke achhe se show kar
"""
import inspect

class Employee:
    # num = 1
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


skillf = Employee("Skill", "F")
num = 1
members = inspect.getmembers(skillf)
for item in members:
    print(f"{num}. {item}")
    num = num+1
# atribute = getattr(Employee, 'num')
# print(atribute)
