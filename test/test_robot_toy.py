import unittest
from toy_robot.robot_toy import RobotToy


class TestRobotToy(unittest.TestCase):
    
    def setUp(self):
        self.toy = RobotToy()

    def test_valid_direction(self):
        self.toy.direction = 'N'
        self.assertEqual(self.toy.direction, 'N')

    def test_sw_direction(self):
        with self.assertRaises(ValueError):
            self.toy.direction = 'SW'

    def test_valid_position(self):
        self.toy.position.x = 1
        self.assertEqual(self.toy.position.x, 1)

    def test_invalid_position(self):
        with self.assertRaises(ValueError):
            self.toy.position.y = 5

    def test_invalid_placement(self):
        with self.assertRaises(ValueError):
            self.toy.place_robot('S', -1, -1)

    def test_move_forward_n_from_origin(self):
        self.toy.place_robot('N', 0, 0)
        self.toy.move_forward()
        self.assertEqual(self.toy.position.y, 1)

    def tearDown(self):
        self.toy = None


if __name__ == '__main__':
    unittest.main()
