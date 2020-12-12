import unittest
from AOC2020 import ten

class TestTen(unittest.TestCase):
    data = '16\n10\n15\n5\n1\n11\n7\n19\n6\n12\n4'
    data1 = '28\n33\n18\n42\n31\n14\n46\n20\n48\n47\n24\n23\n49\n45\n19\n38\n39\n11\n1\n32\n25\n35\n8\n17\n7\n9\n4\n2\n34\n10\n3'

    def test_sum_volt_diff(self):
        self.assertEqual(ten.sum_jolt_diff(self.data), 35)
        self.assertEqual(ten.sum_jolt_diff(self.data1), 220)

    def test_part_two(self):
        self.assertEqual(ten.part_two(self.data), 8)
        self.assertEqual(ten.part_two(self.data1), 19208)