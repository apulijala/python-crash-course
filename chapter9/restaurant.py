class Restaurant():
    
    def __init__  (self, cuisine_type, restaurant_name):
       self.cuisine_type = cuisine_type
       self.restaurant_name = restaurant_name
       self.number_served = 0
    
    def get_number_served(self):
        return self.number_served
    
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, incvalue):
        self.number_served += incvalue
    
    def describe_restaurant(self):
        return f"{self.restaurant_name} is serving {self.cuisine_type}"
    
    def open_restaurant(self):
        return f"{self.restaurant_name} is open"


class IceCreamStand(Restaurant):
    def __init__(self, cuisine_type, restaurant_name, flavors):
        super().__init__(cuisine_type, restaurant_name)
        self.flavors = flavors
    
    def display_flavors(self):
        print("Ice Cream Flavours")
        for flavor in self.flavors:
            print(flavor)


class UserProfile():
    def __init__(self, last, first, **user_profile ):
        user_profile["last_name"] = last
        user_profile["first_name"] =first
        self.user_profile = user_profile
        self.login_attempts = 0
    
    def get_login_attempts(self):
        return self.login_attempts

    def increment_login_attempts(self, inc):
        self.login_attempts += inc
    
    def reset_login_attempts(self):
        self.login_attempts = 0
    
    
    def greet_user(self):
        return f'Hello, {self.user_profile["first_name"]} {self.user_profile["last_name"]}'

    def describe_user(self):
        """
        To meet the requirement of the exercise printing the result. 
        """
        for attr, val in self.user_profile.items():
            print(f"User's {attr} is {val}")
        return self.user_profile



