import unittest
from formatted_name import get_formatted_name

class NamesTestCase(unittest.TestCase):
       """Tests for 'name_function.py'."""

       def test_first_last_name(self):
           formatted_name = get_formatted_name('janis', 'joplin')
           self.assertEqual(formatted_name, 'Janis Joplin')

       def test_first_last_name_middle(self):
           formatted_name = get_formatted_name('janis', 'joplin', 'janet')
           self.assertEqual(formatted_name, 'Janis Janet Joplin')

if __name__ == '__main__':
       unittest.main()
