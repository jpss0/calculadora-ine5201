"Test calculator arithmetic"
import unittest
from decimal import Decimal

from calculadora.core import calculate


class CalculateTests(unittest.TestCase):
    def test_basic_operations(self) -> None:
        self.assertEqual(calculate("8", "+", "3"), Decimal("11"))
        self.assertEqual(calculate("8", "-", "3"), Decimal("5"))
        self.assertEqual(calculate("8", "*", "3"), Decimal("24"))
        self.assertEqual(calculate("8", "/", "2"), Decimal("4"))

    def test_decimal_operations(self) -> None:
        self.assertEqual(calculate("1.25", "+", "2.5"), Decimal("3.75"))
        self.assertEqual(calculate("0.3", "-", "0.1"), Decimal("0.2"))


if __name__ == "__main__":
    unittest.main()