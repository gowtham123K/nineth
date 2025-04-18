# testing_adding.py

import unittest
from main import add_numbers

class TestAddNumbers(unittest.TestCase):
    
    def test_add_positive(self):
        self.assertEqual(add_numbers(2, 3), 5)
        
    def test_add_negative(self):
        self.assertEqual(add_numbers(-2, -3), -5)
        
    def test_add_zero(self):
        self.assertEqual(add_numbers(0, 5), 5)

if __name__ == '__main__':
    unittest.main()
