class Users:
    def __init__(self):
        pass
    
    def Create_User(self):
        self.username = input("Enter Username: ")
        self.FirstName = input("First Name: ")
        self.Surname = input("Surname: ")
        self.house_address = int(input("House Address: "))
        self.street_name = input("Street Name: ")
        self.zip_code = input("Zip Code: ")
        self.email_address = input("Email Address: ")
        self.date_of_birth = input("Date of Birth (DD-MM-YYYY): ")

    def return_username(self):
        username = self.username
        return username
    
    def return_FirstName(self):
        FirstName = self.FirstName
        return FirstName
    
    def return_Surname(self):
        Surname = self.Surname
        return Surname

    def return_house_address(self):
        house_address = self.house_address
        return house_address
    
    def return_street_name(self):
        street_name = self.street_name
        return street_name

    def return_zip_code(self):
        zip_code = self.zip_code
        return zip_code

    def return_email_address(self):
        email_address = self.email_address
        return email_address

    def return_date_of_birth(self):
        date_of_birth = self.date_of_birth
        return date_of_birth

    def edit_username(self, new_username):
        self.username = self.new_username

    def edit_Surname(self, new_Surname):
        self.Surname = self.new_Surname

    def edit_email_address(self, new_email_address):
        self.email_address = self.new_email_address
    
    def edit_date_of_birth(self, new_date_of_birth):
        self.date_of_birth = self.new_date_of_birth

