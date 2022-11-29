"""import os
from time import sleep

print("====================================")
print("1. Add a Book in the List...")
print("2. Delete a Book in the List...")
print("3. View all Book in the List...")
print("4. Update a Book in the List...")
print("5. Exit")
print("====================================")
print("\n")


choice = int(input("Enter a number: "))
sleep(1)
os.system('clear')


if (choice == 1):
    print("add")
    
elif (choice == 2):
    print("delete")
    
elif (choice == 3):
    print("view")
    
elif (choice == 4):
    print("update")
    
elif (choice == 5):
    print("exit")
    os.system('clear')
else:
    print("error")
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
