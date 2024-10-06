import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setup(self):
        """Set up the SimpleCalculataor instance before each test"""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    
    def test_subtraction(self):
        """Test the subtraction method"""
        self.assertEqual(self.calc.subtract(8, 5), 3)
        self.assertEqual(self.calc.subtract(25, 10), 15)

    def test_multiplication(self):
        """Test the multiplication method"""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(4, 5), 40)

    def test_division(self):
        """Test the division method"""
        self.assertEqual(self.calc.divide(15, 3), 5)
        self.assertEqual(self.calc.divide(10, 0) 10)
