from AOC2020 import eight
import unittest

class TestEight(unittest.TestCase):
    data = 'nop +0\nacc +1\njmp +4\nacc +3\njmp -3\nacc -99\nacc +1\njmp -4\nacc +6'

    def test_handheld_halting(self):
        self.assertEqual(eight.handheld_halting(self.data), 5)
        self.assertEqual(eight.handheld_halting_brute_force(self.data), 8)

if __name__ == '__main__':
    unittest.main()