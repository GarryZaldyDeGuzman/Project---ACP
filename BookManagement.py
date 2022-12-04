book_collection = {}

class Books:

        def __init__(self):
            pass
            
        def setBook_Title(self):
            self.Title = input("Enter the Book Title: ")
        
        def setBook_Author(self):
            self.Author = input("Enter the Book Author: ")

        def setBook_Type(self):
            self.Type = input("Enter the type of Book: ")

        def setBook_Year(self):
            self.Year = int(input("Enter the Book Publication Year: "))

        def setNumber_CopiesAvailable(self):
            self.Number_CopiesAvailable = int(input("Enter the number of copies available: "))

        def getBook_Title(self):
            Title = self.Title
            return Title

        def getBook_Author(self):
            Author= self.Author
            return Author

        def getBook_Type(self):
            Type = self.Type
            return type

        def getBook_Year(self):
            Year = self.Year
            return Year

        def getNumber_CopiesAvailable(self):
            Number_CopiesAvailable = self.Number_CopiesAvailable
            return Number_CopiesAvailable

class BookList(Books):

        def __init__(self):
            self.status = "Available"

            Books.__init__(self)

        def addvaluesin_dict(self, orig_dict, key, list_values):
            orig_dict[key] = list()
            orig_dict[key].append(list_values)
            return orig_dict

        def store_collection(self):
            global book_collection

            #set attribute methods
            self.setBook_Title()
            self.setBook_Author()
            self.setBook_Year()
            self.setNumber_CopiesAvailable()

            #get attribute methods
            Book_Title = self.getBook_Title()
            Book_Author = self.getBook_Author()
            Book_Year = self.getBook_Year()
            Number_CopiesAvailable = self.getNumber_CopiesAvailable()
            status = self.status

            #This list that was defined will house the following attributes
            list_of_values = [Book_Author, Book_Year, Number_CopiesAvailable, status]

            book_collection = self.addvaluesin_dict(book_collection, Book_Title, list_of_values)
            print("Book Updated Successfully.")

        def search_collection(self):
            Title = input("Enter the Book Title you are searching: ")
            for key in book_collection.keys():
                if Title == key:
                    position = key
                    print("The book is Found.")
                    break

        def remove_collection(self):
            Title = input("Enter the Book Title you want to Delete: ")
            temp_dict = book_collection
            for key in temp_dict.keys():
                if key == self.Title:
                    print("Book Deleted Successfully")
                    book_collection.pop(Title)
                    break
            
        def total_no_of_books(self):
            print("Total number of books are: ",len(book_collection))


def main():
    booklist = BookList()

    print("---------Welcome to Library Mananagement System---------")
    print("--------------------------------------------------------")
    print()

    while (True):
        print("--------Select an option from the list below--------")
        print("----------------------------------------------------")
        print()

        print('1. Add a Book in the Library.')
        print('2. Remove a Book in the Library.')
        print('3. Search a Book in the Library.')
        print('4. Total Number of Books in the Library.')
        print('5. Show All Books in the Library.')

        order = int(input('Select an Option in the Following:'))

        if (order==1):
            booklist.store_collection()

        elif (order==2):
            booklist.remove_collection()

        elif (order==3):
            booklist.search_collection()

        elif (order==4):
            booklist.total_no_of_books()

        elif (order==5):
            print(book_collection)

        else:
            print('-----Thank You For Visiting. Have a Nice Day..-----')

main()