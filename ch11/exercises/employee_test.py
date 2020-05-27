import unittest
from employee import Employee

class EmployeeTest(unittest.TestCase):

    def setUp(self):
        self.employee = Employee("Andrew", "Hughes", 50000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEquals(self.employee.salary, 55000)


    def test_give_custom_raise(self):
        self.employee.give_raise(8500)
        self.assertEquals(self.employee.salary, 58500)

if __name__ == "__main__":
    unittest.main()