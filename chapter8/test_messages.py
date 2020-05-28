import unittest
from messages import *

class MessageTest(unittest.TestCase):
    def test_send_messages(self):
        messages = ["Jaya Guru Datta", "Hello World", "Om Aim Hreem Shreem Kleem Sree Matre Namaha", "Wonderworld"]
        sent_messages = []
        send_messages(messages, sent_messages)
        self.assertListEqual(messages, sent_messages)

    def test_send_messages_with_copy(self):
        messages = ["Jaya Guru Datta", "Hello World", "Om Aim Hreem Shreem Kleem Sree Matre Namaha", "Wonderworld"]
        sent_messages = []
        send_messages(messages[:], sent_messages)
        self.assertListEqual(messages, sent_messages)
    
    def test_sandwiches(self):
        sandwiches("Tomato", "Cheese", "Mayonase", "Egg")
        print("\nSecond Run")
        sandwiches("Kheema", "Potato", "Lettuce")
        print("\nThird Run")
        sandwiches("Pineapple", "Bun Maska", "Chilli")
        print("\n")
    
    def test_user_profile(self):
      result = user_profile(last="Pulijala", first= "Arvind Kumar", 
      height="6.0 feet", citizen = "UK Citizen", devotee="Datta Devotee" )
      self.assertEqual(result["height"], "6.0 feet")
      self.assertEqual(result["last"], "Pulijala")
      self.assertEqual(result["first"], "Arvind Kumar")
      self.assertEqual(result["devotee"], "Datta Devotee")
        
    def test_make_car(self):
        result = make_car('subaru', 'outback', color='blue',  tow_package=True)
        print(result)
        self.assertEqual(result["manufacutrer"], 'subaru')
        self.assertEqual(result["model"], 'subaru')
        self.assertEqual(result["model"], "outback")
        self.assertEqual(result["color"], "Pulijala")
        self.assertEqual(result["tow_package"], True)
        

if __name__ == "__main__":
    unittest.main()