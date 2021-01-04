import unittest
from AOC2020 import fifteen

class TestFifteen(unittest.TestCase):
    data  = [0,3,6]
    data1 = [1,3,2]
    data2 = [2,1,3]
    data3 = [1,2,3]
    data4 = [2,3,1]
    data5 = [3,2,1]
    data6 = [3,1,2]
    puzzle_input = [0,12,6,13,20,1,17]

    def test_consider(self):
        self.assertEqual(fifteen.consider(*fifteen.initialize(self.data), target=2020), 436)
        self.assertEqual(fifteen.consider(*fifteen.initialize(self.data1), target=2020), 1)
        self.assertEqual(fifteen.consider(*fifteen.initialize(self.data2), target=2020), 10)
        self.assertEqual(fifteen.consider(*fifteen.initialize(self.data3), target=2020), 27)
        self.assertEqual(fifteen.consider(*fifteen.initialize(self.data4), target=2020), 78)
        self.assertEqual(fifteen.consider(*fifteen.initialize(self.data5), target=2020), 438)
        self.assertEqual(fifteen.consider(*fifteen.initialize(self.data6), target=2020), 1836)
        self.assertEqual(fifteen.consider(*fifteen.initialize(self.data), target=30000000), 175594)
        self.assertEqual(fifteen.consider(*fifteen.initialize(self.puzzle_input), target=30000000), 110871)
