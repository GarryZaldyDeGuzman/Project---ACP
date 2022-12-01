try:
    class Books:

        def __init__(self):
            pass
            
            self.setBook_ID()
            self.setBook_Title()
            self.setBook_Author()
            self.setBook_Type()
            self.setBook_Year()
            self.setNumber_CopiesAvailable()
            
        def setBook_ID(self):
            import random
            self.ID = random.randint(1000,2000)

        def setBook_Title(self):
            self.Title = input("Enter the Book Title: ")
        
        def setBook_Author(self):
            self.Author = input("Enter the Book Author")

        def setBook_Type(self):
            self.Type = input("Enter the type of Book: ")

        def setBook_Year(self):
            self.Year = int(input("Enter the Book Publication Year: "))

        def setNumber_CopiesAvailable(self):
            self.Copies = int(input("Enter the number of copies available: "))

        def getBook_ID(self):
            ID = self.ID
            return ID

        def getBook_Title(self):
            Title = self.Title
            return Title

        def getBook_Author(self):
            Author= self.Author
            return Author

        def getBook_Type(self):
            Type = self.Type
            return Type

        def getBook_Year(self):
            Year = self.Year
            return Year

        def getNumber_CopiesAvailable(self):
            Copies = self.Copies
            return Copies

except:
    print("Please Retry Again...")

        

