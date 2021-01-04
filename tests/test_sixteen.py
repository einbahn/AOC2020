import unittest
from AOC2020 import sixteen

class TestSixteen(unittest.TestCase):
    data = 'class: 1-3 or 5-7\nrow: 6-11 or 33-44\nseat: 13-40 or 45-50\n\nyour ticket:\n7,1,14\n\nnearby tickets:\n7,3,47\n40,4,50\n55,2,20\n38,6,12'

    def test_solve(self):
        self.assertEqual(sixteen.solve(self.data), 71)
