class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@PagaluWorld.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Tere bap ka email nahi hai jo bina set kare mang raha"
        return f"{self.fname}.{self.lname}@PagaluWorld.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None
anant = Employee("anant", "chandak")
# print(anant.explain())
# print(anant.email)
anant.fname = "arnav"
anant.lname = "kutta"
# print(anant.email)
anant.email = "anant.THEcoder@terebapkaemail.com"
# print(anant.fname, end=" ")
# print(anant.lname)
# print(anant.email)
del anant.email
print(anant.email)