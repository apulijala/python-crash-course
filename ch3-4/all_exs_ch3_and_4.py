import unittest
from greetings import *
from guest_list import *
from locations import *

class Ch3And4(unittest.TestCase):

    def test_enemy_with_greeting(self):
        enemy_with_greeting()
        

    """
        This is the trick that speeds up coding
        ability .  
    """
    def test_transportation(self):
        transportation()
        

    def test_guest_list(self):
        guest_list()
        guest_list_minus_one()


    def test_add_new_guests(self):
        add_new_guests()

    def test_add_new_guests(self):
        remove_all_except_two()
    
    def test_locations(self):
        places_to_visit()


    

if __name__ == "__main__":
    unittest.main()