"""choice = int(input("Enter a number: "))
print(choice)
"""

"""def switch(choice):
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    else:
        pass
"""

class Book(object):
    def __init__(self,type):
        self.type = type
    def details(self):
        print("The type of book is:", (self.type))

class Manga(Book):
    def __init__(self, type, name, author, price):
        Book.__init__(self, type)
        self.name = name
        self.author = author
        self.price = price

    def details(self):
        print("The type of book is:", (self.type))
        print("The name of the book is: ", (self.name))
        print("The name of the author is: ", (self.author))
        print("The price of the book is: ", (self.price))

class Manhwa(Book):
    def __init__(self, type, name, author, price):
        Book.__init__(self, type)
        self.name = name
        self.author = author
        self.price = price

    def details(self):
        print("The type of book is:", (self.type))
        print("The name of the book is: ", (self.name))
        print("The name of the author is: ", (self.author))
        print("The price of the book is: ", (self.price))



a = Manga("Manhwa","Solo Leveling", "geh", 500 )

a.details()
