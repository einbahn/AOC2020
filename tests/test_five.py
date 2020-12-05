from AOC2020 import five
import unittest

class TestFive(unittest.TestCase):

    def test_decode_boarding_pass(self):
        self.assertEqual(five.decode_boarding_pass('BFFFBBFRRR'), (70, 7, 567))
        self.assertEqual(five.decode_boarding_pass('FFFBBBFRRR'), (14, 7, 119))
        self.assertEqual(five.decode_boarding_pass('BBFFBBFRLL'), (102, 4, 820))
