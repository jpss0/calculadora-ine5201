"Test calculator input and division errors"
import unittest

from calculadora.core import calculate


class ValidationTests(unittest.TestCase):
    def test_division_by_zero(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            calculate("9", "/", "0")

    def test_invalid_operands(self) -> None:
        with self.assertRaises(ValueError):
            calculate("abc", "+", "1")
        with self.assertRaises(ValueError):
            calculate("NaN", "+", "1")

    def test_invalid_operator(self) -> None:
        with self.assertRaises(ValueError):
            calculate("1", "%", "2")


if __name__ == "__main__":
    unittest.main()