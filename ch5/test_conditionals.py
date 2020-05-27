from conditionals import *
import unittest

class ConditonalTest(unittest.TestCase):
    def test_string_equals(self):
        string_equals("hello")
        string_equals("Jaya Guru Datta")

    def test_string_not_equals(self):
        string_not_equals("Dattatreya")
        string_not_equals("hello")
    
    def test_string_equals_lower(self):
        string_equals_lower("HELLO")
        string_equals_lower("hELLo")
        string_equals_lower("HeLLo")
        string_equals_lower("datta")

    def test_numerical_comparision(self):
        numerical_comparision(5)
        numerical_comparision(7)
        numerical_comparision(3)
        numerical_comparision_less_equals(10)
        numerical_comparision_less_equals(8)
        numerical_comparision_less_equals(15)
        numerical_comparision_greater_equals(11)
        numerical_comparision_greater_equals(8)
        numerical_comparision_greater_equals(20)


    def test_item_exists_in_array(self):
        item_exists_in_array(10) # should not exist
        item_exists_in_array(11) # should not exist
        item_exists_in_array(5) # should exist
        item_exists_in_array(6) # should exist

    def test_item_not_exists_in_array(self):
        item_not_exists_in_array(10) # should not exist
        item_not_exists_in_array(11) # should not exist
        item_not_exists_in_array(5) # should exist
        item_not_exists_in_array(6) # should exist
    
    def test_or_condition(self):
        self.assertTrue(or_condition("Rama"))
        self.assertTrue(or_condition("rama"))
        self.assertTrue(or_condition("krishna"))
        self.assertTrue(or_condition("KRishna"))
        self.assertFalse(or_condition("datta"))
        self.assertFalse(or_condition("hanuman"))
        
    def test_and_condition(self):
        # Number should be >= 5 and <= 11 . other wise false
        print("Running And Conditions")
        self.assertTrue(and_condition(5))
        self.assertTrue(and_condition(6))
        self.assertTrue(and_condition(11))
        self.assertTrue(and_condition(11))
        self.assertFalse(and_condition(12))
        self.assertFalse(and_condition(13))
        self.assertFalse(and_condition(101))
        self.assertFalse(and_condition(-5))
        self.assertFalse(and_condition(4))
        
        


if __name__ == "__main__":
    unittest.main()