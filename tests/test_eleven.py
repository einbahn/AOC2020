import unittest
from AOC2020 import eleven


class TestEleven(unittest.TestCase):
    data = 'L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\nL.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL'

    def test_part_one(self):
        self.assertEqual(eleven.part_one(self.data), 37)