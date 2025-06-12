"""
Create a test_simple_calculator.py script to define and run unit tests for each method in the SimpleCalculator class. Your tests should cover various scenarios to ensure the class functions correctly.
"""

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        # Add more assertions to thoroughly test the subtract method.
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        # Add more assertions to thoroughly test the multiply method.
        self.assertEqual(self.calc.multiply(-1, -1), 1)

    def test_division(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        # Add more assertions to thoroughly test the divide method.
        self.assertEqual(self.calc.divide(-1, -1), 1)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
        

        
