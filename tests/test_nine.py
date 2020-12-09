from AOC2020 import nine
import unittest 


class TestNine(unittest.TestCase):
    
    example = '35\n20\n15\n25\n47\n40\n62\n55\n65\n95\n102\n117\n150\n182\n127\n219\n299\n277\n309\n576'

    def test_part_one(self):
        self.assertEquals(nine.part_one(self.example, preamble_length=5), 127)
        self.assertEquals(nine.part_two(self.example, 127), 62)