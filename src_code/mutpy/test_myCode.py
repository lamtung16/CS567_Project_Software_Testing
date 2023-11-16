from unittest import TestCase
from myCode import find_most_common_number

class CalculatorTest(TestCase):
    def test(self):
        self.assertEqual(find_most_common_number([1, 2, 3, 2, 4, 2, 5, 2, 6]), 2)
        self.assertEqual(find_most_common_number([7]), 7)
        self.assertIsNone(find_most_common_number([]))
        self.assertEqual(find_most_common_number([1, 2, 3, 2, 4, 3, 5, 4, 6]), 2)
        self.assertEqual(find_most_common_number([-1, -2, -1, -3, -2, -4, -2, -5]), -2)
