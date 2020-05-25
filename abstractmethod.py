from abc import ABC ,abstractmethod

class Shapes(ABC):

    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shapes):
    type = "rectangle"
    sides = 4

    def __init__(self):
        self.lenght = 8
        self.breadth = 9

    def printarea(self):
        return self.lenght * self.breadth

rect1 = Rectangle()

print(rect1.printarea())
