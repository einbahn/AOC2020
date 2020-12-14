from AOC2020 import twelve
import unittest


class TestTwelve(unittest.TestCase):
    test_data = 'F10\nN3\nF7\nR90\nF11'

    def test_part_two(self):
        ship = twelve.Ship()
        for i in self.test_data.split('\n'):
            d = i[0]
            s = int(i[1:])
            if d == 'F':
                ship.move(s)
            else:
                ship.waypoint.move(d, s)
        self.assertEqual(ship.distance_from_start(), 286)



