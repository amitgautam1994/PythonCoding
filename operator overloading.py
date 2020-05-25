class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}. Role is {self.role}."

    @classmethod
    def changeleaves(cls,new_leaves):
        cls.no_of_leaves = new_leaves


emp1 = Employee("Ravi", 2300 , "Programmer")
emp2 = Employee("Rohan", 4300, "Analyst")

emp1.changeleaves(5)

print(emp1.no_of_leaves)