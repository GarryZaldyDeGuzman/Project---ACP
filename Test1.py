class Book(object):
    def __init__(self,type):
        self.type = type
    def details(self):
        print("The type of book is:".format(self.type))

class Manga(Book):
    def __init__(self, type, name, author, price):
        self.name = name
        self.author = author
        self.price = price

        Book.__init__(self, type)

    def details(self):
        print("The type of book is:".format(self.type))
        print("The name of the book is: ".format(self.name))
        print("The name of the author is: ".format(self.author))
        print("The price of the book is: ".format(self.price))

class Manhwa(Book):
    def __init__(self, type, name, author, price):
        self.name = name
        self.author = author
        self.price = price

        Book.__init__(self, type)

    def details(self):
        print("The type of book is:".format(self.type))
        print("The name of the book is: ".format(self.name))
        print("The name of the author is: ".format(self.author))
        print("The price of the book is: ".format(self.price))
        
