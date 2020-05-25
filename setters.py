class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname}.{self.lname}@gmail.com"

    def explain(self):
        return  f"This employee is {self.fname} {self.lname} "

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email in not set"
        else:
            return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        names = string.split("@")[0]

        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


obj1 = Employee("Raj", "Kumar")
obj2 = Employee("Amit", "Gautam")

print(obj1.email)

obj1.fname = "Rajesh"

print(obj1.email)

obj1.email = "this.that@gmail.com"

print(obj1.fname)

del obj1.email

print(obj1.email)

print(obj1.fname)