import unittest
from toy_robot.robot_toy import RobotToy


class TestRobotToy(unittest.TestCase):
    
    def setUp(self):
        self.toy = RobotToy()

    def test_valid_direction(self):
        self.toy.direction = 'N'
        self.assertEqual(self.toy.direction, 'N')

    def tearDown(self):
        self.toy = None


if __name__ == '__main__':
    unittest.main()
