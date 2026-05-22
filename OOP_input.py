class Employee:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def display(self):
        return self.firstname + ' ' + self.lastname
    @classmethod
    def user_input(self):
        while True:
            try: 
                firstname = input("Enter first name: ")
                lastname = input("Enter last name: ")
                return self(firstname, lastname)
            except:
                print("Oops...Invalid input!")
                continue
e = Employee.user_input()
print(e.display())
            