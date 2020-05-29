from restaurant import UserProfile


class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        print("User's privileges are: ")
        for privilege in self.privileges:
            print(privilege)


class Admin(UserProfile):
    def __init__(self, last, first, privileges, **user_profile):
        super().__init__(last, first, **user_profile)
        self.user_profile["privileges"] = Privileges(privileges)
    
    def show_privileges(self):
        self.user_profile["privileges"].show_privileges()