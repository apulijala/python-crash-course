import unittest
from restaurant import *
from admin import Admin

class RestaurantTest(unittest.TestCase):
    def setUp(self):
        self.cuisine_type = "Vegetarian"
        self.restaurant_name = "Sarvanna Bhavan"
        self.restaurant = Restaurant(cuisine_type=self.cuisine_type, 
            restaurant_name = self.restaurant_name)
        self.user = UserProfile("Pulijala", "Arvind", 
            height="6.0 feet", weight = "90 Kg")


    def test_open_restaurant(self):
        description = self.restaurant.open_restaurant()
        self.assertEqual(description, f"{self.restaurant_name} is open")
    
    def test_increment(self):
        self.assertEqual(self.restaurant.get_number_served(), 0)
        self.restaurant.set_number_served(10)
        self.assertEqual(self.restaurant.get_number_served(), 10)
        self.restaurant.increment_number_served(8)
        self.assertEqual(self.restaurant.get_number_served(), 18)

    def test_describe_restaurant(self):
        description = self.restaurant.describe_restaurant()
        self.assertEqual(description, f"{self.restaurant_name} is serving {self.cuisine_type}")
    
    def test_crate_three_instances(self):
        restaurant = Restaurant("Manglore Tiffin", "Kamat Hotel")
        restaurant1 = Restaurant("Fast Food", "McDonalds")
        print(restaurant.describe_restaurant())
        print(restaurant1.describe_restaurant())
        print(self.restaurant.describe_restaurant())
    
    def test_greet_user(self):
        greeting = self.user.greet_user()
        self.assertEqual(greeting, "Hello, Arvind Pulijala")
    
    
    def test_describe_user(self):
        user = self.user.describe_user()
        self.assertEqual(user["first_name"], "Arvind")
        self.assertEqual(user["last_name"], "Pulijala")
        self.assertEqual(user["height"], "6.0 feet")

    def test_login_attemtps(self):
        self.assertEqual(self.user.get_login_attempts(), 0)
        self.user.increment_login_attempts(5)
        self.assertEqual(self.user.get_login_attempts(),5)
        self.user.reset_login_attempts()
        self.assertEqual(self.user.get_login_attempts(), 0)
    
    def test_ice_cream_flavours(self):
        flavours = ["Vanila", "StrawBerry", "Tuity Fruity"]
        icecreate_stand = IceCreamStand("Ice Cream", "Tuity Fruity", flavours)
        icecreate_stand.display_flavors()

    def test_user_privileges(self):
        privileges = ["can add post", "can delete post", "can ban user"]
        admin = Admin("Pulijala", "Arvind", privileges, height="6.0 feet", weight="80 Kg")
        admin.describe_user()
        admin.show_privileges()



if __name__ == "__main__":
    unittest.main()