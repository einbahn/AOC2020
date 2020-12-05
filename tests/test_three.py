import unittest
from AOC2020 import three

class TestThree(unittest.TestCase):

    test_data = '..##.......\n#...#...#..\n.#....#..#.\n..#.#...#.#\n.#...##..#.\n..#.##.....\n.#.#.#....#\n.#........#\n#.##...#...\n#...##....#\n.#..#...#.#'

    test_slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    def test_part_a(self):
        self.assertEqual(three.part_a(self.test_data), 7)

    def test_part_b(self):
        self.assertEqual(three.part_b(self.test_data, self.test_slopes), 336)

if __name__ == '__main__':
    unittest.main()