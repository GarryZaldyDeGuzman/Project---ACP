class BookList(Books):

    def __intit__(self):
        self.status = "Available"
        self.borrowers - ""

        Books.__init__(self)

        def addvalues_dict(self, orig_dict, key, list_values):
            orig_dict[key] = list()
            orig_dict[key].append[list_values]
            return orig_dict

        def store_collection(self):

            global book_collection

            self.setBook_ID()
            self.setBook_Title()
            self.setBook_Author()
            self.setBook_Year()
            self.setBook_Publisher()
            self.setNumber_CopiesAvailable()
            self.set_PubDate()

            Book_ID = self.getBook_ID()
            Book_Title = self.getBook_Title()
            Book_Author = self.getBook_Author()
            Book_Year = self.getBook_Year()
            Book_Publisher = self.getBook_Publisher()
            Number_CopiesAvailable = self.getNumber_CopiesAvailable()
            Pub_Date = self.getPub_Date()
            status = self.status
            borrowers = self.borrowers

            list_values = [Book_ID, Book_Author, Book_Year, Book_Publisher, Number_CopiesAvailable, Pub_Date, status, borrowers]

            book_collection = self.addvalues_dict(book_collection, Book_Title, list_values)
            print("Book Updated Successfully")

            def search_collection(self):
                title = input("Enter the Title of the book you are searching: ")
                for key in book_collection.keys():
                    if title == key:
                        position = key
                        print("The book " + "\"" + title + "\"" + "is found.")
                        print(book_collection[position])
                        break 
            
            def remove_collection(self):
                title = input("Enter the title of the book you wanted to remove: ")
                temp_dict = book_collection
                for key in temp_dict.keys():
                    if key == self.title:
                        print("Book" + "\"" + title + "\"" + "Removed Successfully" )
                        book_collection.pop(title)
                        break
                
            def total_nobooks(self):
                print("Total number of books are: ", len(book_collection))
            


