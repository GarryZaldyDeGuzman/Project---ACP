try:
    class Books:

        def __init__(self):
            pass
            
        def set_book_id(self):
            import random
            self.ID = random.randint(1000,2000)

        def set_book_title(self):
            self.title = input("Enter the Book Title: ")
        
        def set_book_author(self):
            self.author = input("Enter the Book Author")

        def set_book_type(self):
            self.type = input("Enter the type of Book: ")

        def set_book_year(self):
            self.year = int(input("Enter the Book Publication Year: "))

        def set_number_of_copies_available(self):
            self.copies = int(input("Enter the number of copies available: "))

        def get_book_id(self):
            ID = self.ID
            return ID

        def get_book_title(self):
            title = self.title
            return title

        def get_book_author(self):
            author= self.author
            return author

        def get_book_type(self):
            type = self.type
            return type

        def get_book_year(self):
            year = self.year
            return year

        def get_number_of_copies_available(self):
            copies = self.copies
            return copies

except:
    print("Please Retry Again...")

        

