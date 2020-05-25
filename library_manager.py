class Library:
    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        self.lenddict = {}

    def displaybook(self):
        print(f"We have following books in our library: {self.name}")
        for book in booklist:
            print(book)


    def lendbook(self,user,book):
        pass

    def returnbook(self):
        pass

    def addbook(self,book):
        pass