from personal_message import print_person_name
from famous_quote import persons_quote, strip_white_space, favorite_number
import unittest

class AllStringTestCases(unittest.TestCase):

    def test_print_person_name(self):
        result = print_person_name("Arvind")
        print(result)
        self.assertEqual(result, "Hello Arvind, Would you like to learn some Python today?")


    def test_persons_quote(self):
        famous_person = "albert einstein"
        message = "A person who never made a mistake never tried anything new."
        result = persons_quote(famous_person, message)
        print(result)
        expected = "Albert Einstein once said, A person who never made a mistake never tried anything new."
        self.assertEqual(result, expected )


    def test_strip_white_space(self):
        name = "Hello "
        self.assertEqual(strip_white_space(name), "Hello")
        name = " Hello "
        self.assertEqual(strip_white_space(name), "Hello")

        name = " Albert Einstein hello \t"
        self.assertEqual(strip_white_space(name), "Albert Einstein hello")
        
        name = "\n\n Albert Einstein hello \t\n"
        self.assertEqual(strip_white_space(name), "Albert Einstein hello")
        

    def test_favorite_number(self):
        print(favorite_number(8))

    """
        This is not a acutal test case. 
        Just a place holder printing arithematic operators.
        Addition, Multiplication and substraction.
    """
    def test_numeric_ops(self):
        print(" 5 + 3 = ",  5+ 3)
        print(" 2 * 4 = ",  2 * 4)
        print(" 32 - 24 = ",  32 - 24)
        print(" 16 / 2 = ",  16 / 2)
        num_array = [3, 4, 5, 89]
        print("HEllo aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") 




if __name__ == "__main__":
    unittest.main()