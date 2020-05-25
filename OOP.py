class A:
    classvar1 = "I am a variable in Class A"

    def __init__(self):
        self.var1 = "I am inside Class A's constructor"
        self.classvar1 = "I am a variable in Class A"
        self.special = "Special"


class B(A):
    classvar2 = "I am in Class B"
    def __init__(self):

        self.var1 = "I am inside Class B's constructor"

        super().__init__()
        self.classvar1 = "I am a variable in Class B"


a = A()
b = B()

print(b.var1,"\n", b.classvar1,"\n", b.special )

