try:
    class UserList(Users):
        def __init__(self):
            self.borrowing = 0
            self.borrowing_list = ""
            Users.__init__(self)

    def add_values_UserList(self, orig_UserList, list_valuesUser):
        orig_UserList.append(list_valuesUser)
        return orig_UserList

    def store_collection_Users(self):
        global user_collection

        self.create_User()

        username = self.username
        Firstname = self.Firstname
        Surname = self.Surname
        house_address = self.house_address
        street_name = self.street_name
        zip_code = self.zip_code
        email_address = self.email_address
        DoB = self.date_of_birth
        borrowing = self.borrowing
        borrowing_list = self.borrowing_list

        list_valuesUSer = [username, Firstname, Surname, house_address, street_name, zip_code, email_address, DoB, borrowing, borrowing_list]
        user_collection = self.add_values_UserList(user_collection, list_valuesUSer)

    def remove_User(self):
        FirstName = input("Enter the First Name of the user to be removed: ")
        temp_Userlist = user_collection
        for value in temp_Userlist:
            if FirstName in value:
                user_collection.remove(value)
                print("User " + "\"" + FirstName + "\"" + " " + "Deleted.")
                break
    
    def total_Users(self):
        print("Total number of users are: ", len(user_collection))

    def user_details(self):
        username = input("Enter the Username of the user to be displayed: ")
        global user_collection
        for value in user_collection:
            for i in value:
                if username == i:
                    index = user_collection.index(value)
                    print("User " + "\"" + username + "\"" + " " +  "Found")
                    return user_collection[index]
except:
    print("MESSSSSAAAAGGGGEEEE")