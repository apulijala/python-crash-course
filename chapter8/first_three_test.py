import unittest
from first_three import *

class FirstThree(unittest.TestCase):
    def test_display_message(self):
        self.assertEqual(display_message(), "Om Aim Hreem Shreem Kleem Sree Matre Namaha")

    def test_favorite_book(self):
        self.assertEqual(favorite_book("alice in Wonderland"), "One of my favorite books is Alice In Wonderland")
        # for satisfying book requirement. 
        print(favorite_book("Devi Bhagvatham"))
    
    def test_make_shirt(self):
        message = make_shirt("Large", "Jaya Guru Datta")
        self.assertEqual(message, f"Large T-Shirt has Jaya Guru Datta on it")
        message = make_shirt(message="om aim hreem shreem kleem sree matre namaha", size="large")
        self.assertEqual(message, f"Large T-Shirt has Om Aim Hreem Shreem Kleem Sree Matre Namaha on it")
        print(message)
    
    def test_make_shirt_default(self):
        message = make_shirt()
        self.assertEqual(message, f"Large T-Shirt has I Love Python on it")

    def test_describe_city(self):
        msg = describe_city("london")
        self.assertEqual(msg, "London is in England")
        msg = describe_city("Reykjavik", "Iceland")
        self.assertEqual(msg, f"Reykjavik is in Iceland")
        msg = describe_city("tokyo", "japan")
        self.assertEqual(msg, f"Tokyo is in Japan")

    def test_city_country(self):
        msg = city_country("Santiago", "Chile")
        self.assertEqual(msg, "Santiago, Chile")

    def test_make_album(self):
        album = make_album("Krishna", "Bhagvad Gita")
        self.assertDictEqual(album, {"title": "Bhagvad Gita", "name": "Krishna"})
        album = make_album("Krishna", "Bhagvad Gita", 18)
        self.assertDictEqual(album, {"title": "Bhagvad Gita", "name": "Krishna", "songs" : 18})

    def test_input_user_albumn(self):
        
        name = input("Enter Artist Name or enter quit: ")
        while name != "quit":
            title = input("Enter Album title: ")
            album = make_album(title = title, name = name)
            print("Album is ", album)
            name = input("Enter Artist Name or enter quit: ")

    
if __name__ == "__main__":
    unittest.main()