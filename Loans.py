class Loans(User):
    def__init__(self):

Users.__init__(self)
def borrow_book(self):
    book_name = input("Enter the book name you want to borrow: ")
    username = input("Enter your username: ")

    global book_collection
    global user_collection
    
for key in book_collection.keys():
    if key == book_name:
        book_collection[book_name][0][6] = 'Unavailable'
        book_collection[book_name][0][7] = book_collection[book_name][0][7] + username + ','

for value in user_collection:
    for i in value:
        if i == username:
            index = user_collection.index(value)
            user_collection[index][8] = user_collection[index][8] + 1
            user_collection[index][9] = user_collection[index][9] + book_name + ','
            print("Book has been issued at your name")
            break

def return_book(self):
    book_name = input("Enter the book name you want to return: ")
    username = input("Enter the username: ")

    global book_collection
    global user_collection

if book_name in book_collection.keys():
    book_collection[book_name][0][6] = 'Available'

for value in user_collection:
    for i in value:
        if username == i;
        index = user_collection.index(value)
        user_collection[index][8] = user_collection[index][8] -1
        user_collection[index][9] = user_collection[index][9].replace(book_name + ',',")
        book_collection[book_name][0][7] = book_collection[book_name][0][7].replace(username + ',',")
        print("Book has been Returned by you")