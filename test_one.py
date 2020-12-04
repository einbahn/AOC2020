import unittest
import one


class TestOne(unittest.TestCase):
    test_data = [1721, 979, 366, 299, 675, 1456]

    def test_two_sum(self):
        self.assertEqual(one.two_sum(self.test_data), 514579)

    def test_three_sum(self):
        self.assertEqual(one.three_sum(self.test_data), 241861950)


if __name__ == '__main__':
    unittest.main()

