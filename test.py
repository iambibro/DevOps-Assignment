import unittest
from calculator import add, subtract, multiply

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(0, 0), 0)
        self.assertRaises(ValueError, add, -2, 3)

    def test_subtraction(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(5, 5), 0)
        self.assertRaises(ValueError, subtract, 5, -3)

    def test_multiplication(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(0, 5), 0)
        self.assertRaises(ValueError, multiply, 2, -3)

if __name__ == '__main__':
    unittest.main()
