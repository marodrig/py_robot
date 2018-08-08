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

    def test_valid_placement(self):
        self.toy.place_robot('S', 2, 3)
        self.assertEqual(self.toy.position.x, 2)

    def test_move_forward_n_from_origin(self):
        self.toy.place_robot('N', 0, 0)
        self.toy.move_forward()
        self.assertEqual(self.toy.position.y, 1)

    def test_move_out_board_from_origin(self):
        self.toy.place_robot('S', 0, 0)
        with self.assertRaises(ValueError):
            self.toy.move_forward()

    def test_move_out_board_from_top_edge(self):
        self.toy.place_robot('N', 3, 4)
        with self.assertRaises(ValueError):
            self.toy.move_forward()

    def test_move_out_board_from_left_edge(self):
        self.toy.place_robot('W', 0, 2)
        with self.assertRaises(ValueError):
            self.toy.move_forward()

    def test_move_out_board_from_right_edge(self):
        self.toy.place_robot('E', 4, 2)
        with self.assertRaises(ValueError):
            self.toy.move_forward()

    def test_left_rotation_from_n(self):
        self.toy.place_robot('N', 1, 1)
        self.toy.rotate_left()
        self.assertEqual(self.toy.direction, 'W')

    def test_right_rotation_from_s(self):
        self.toy.place_robot('S', 2, 3)
        self.toy.rotate_right()
        self.assertEqual(self.toy.direction, 'W')

    def tearDown(self):
        self.toy = None


if __name__ == '__main__':
    unittest.main()
