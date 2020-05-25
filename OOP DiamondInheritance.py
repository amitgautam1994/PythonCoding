class A:
    def met(self):
        print("This is method from Class A")

class B(A):
    def met(self):
        print("This is method from Class B")

class C(A):
    def met(self):
        print("This is method from Class C")

class D(B,C):
    pass


a = A()
b = B()
c = C()
d = D()

d.met()