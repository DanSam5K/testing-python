import unittest
# from ...calculator_app.calc_app import Calculator
from calculator_app.calc_app import Calculator
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2,2))

    def test_add_method_raises_typeerror_if_not_ints(self):
        self.assertRaises(ValueError, self.calc.add, "Hello", "World")

    def test_add_method_raises_typeerror_if_one_not_int(self):
        self.assertRaises(ValueError, self.calc.add, 1, "World")

    def test_subtract_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.subtract(4,2))

    def test_subtract_method_raises_typeerror_if_not_ints(self):
        self.assertRaises(ValueError, self.calc.subtract, "Hello", "World")

    def test_subtract_method_raises_typeerror_if_one_not_int(self):
        self.assertRaises(ValueError, self.calc.subtract, 1, "World")

    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(6, self.calc.multiply(2,3))

    def test_multiply_method_raises_typeerror_if_not_ints(self):
        self.assertRaises(ValueError, self.calc.multiply, "Hello", "World")

    def test_multiply_method_raises_typeerror_if_one_not_int(self):
        self.assertRaises(ValueError, self.calc.multiply, 1, "World")


if __name__ == '__main__':
    unittest.main()