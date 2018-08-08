import unittest
from toy_robot.py_coordinates import PyCoordinates


class TestPyCoordinates(unittest.TestCase):

    def setUp(self):
        self.coord = PyCoordinates()

    def test_valid_x(self):
        self.coord.x = 3
        self.assertEqual(self.coord.x, 3)

    def test_zero_x(self):
        self.coord.x = 0
        self.assertEqual(self.coord.x, 0)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            self.coord.x = int(-2)

    def test_valid_y(self):
        self.coord.y = 2
        self.assertEqual(self.coord.y, 2)

    def test_zero_y(self):
        self.coord.y = 0
        self.assertEqual(self.coord.y, 0)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            self.coord.y = int(-2)

    def tearDown(self):
        self.coord = None


if __name__ == '__main__':
    unittest.main()
