from AOC2020 import day_six
import unittest

class TestSix(unittest.TestCase):
    data = 'abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb'

    def test_solve_a(self):
        self.assertEqual(day_six.solve_a(data=self.data), 11)

    def test_solve_b(self):
        self.assertEqual(day_six.solve_b(data=self.data), 6)