from AOC2020 import fourteen
import unittest

class TestFourteen(unittest.TestCase):
    test_data = 'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X\nmem[8] = 11\nmem[7] = 101\nmem[8] = 0'
    test_data_two = 'mask = 000000000000000000000000000000X1001X\nmem[42] = 100\nmask = 00000000000000000000000000000000X0XX\nmem[26] = 1'

    def test_solve_a(self):
        self.assertEqual(fourteen.solve_a(fourteen.split_input(self.test_data)), 165)

    def test_solve_b(self):
        self.assertEqual(fourteen.solve_b(fourteen.split_input(self.test_data_two)), 208)
