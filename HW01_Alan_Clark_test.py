"""
   File Name:    HW01_Alan_Clark_test.py
   Author:       Alan Clark
   Date:         11 Sep 2021
   Description:  Test the classify_triangle function using unittest instances
"""

from HW01_Alan_Clark import classify_triangle
import unittest

# Class of functions to test classify_triangle()
class TestHW01Function(unittest.TestCase):

    """ Values for a non-right scalene triangle """
    def test_scalene_triangle(self) -> None:
        self.assertEqual(classify_triangle(9, 6, 7), "scalene")

    """ Values for a scalene right triangle """
    def test_scalene_right_triangle(self) -> None:
        self.assertEqual(classify_triangle(3, 4, 5), "scalene, right triangle")
        
    """ Values for an equilateral triangle """
    def test_equilateral_triangle(self) -> None:
        self.assertEqual(classify_triangle(8, 8, 8), "equilateral")
        
    """ Values for an isoceles triangle """
    def test_isoceles_triangle(self) -> None:
        self.assertEqual(classify_triangle(12, 7, 12), "isoceles")

    """ Non-positive inputs raise value error """
    def test_non_positive_inputs(self) -> None:
        with self.assertRaises(ValueError):
            classify_triangle(5, 6, -10)

    """ Zero-value inputs raise value error """
    def test_zero_value_inputs(self) -> None:
        with self.assertRaises(ValueError):
            classify_triangle(11, 0, 14)

    """ Non-integer inputs raise type error """
    def test_non_integer_inputs(self) -> None:
        with self.assertRaises(TypeError):
            classify_triangle(7, 6.6, 14)


# This runs all the test case functions in TestHW01Function, although it's not clear to me how it works
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

