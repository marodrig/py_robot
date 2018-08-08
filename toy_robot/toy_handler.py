import sys
from toy_robot.robot_toy import RobotToy

class ToyHandler(object):
    def __init__(self):
        self.toy = RobotToy()

    def read_command(self):
        with sys.stdin as py_stdin:
            for line in py_stdin:
                commands = list(line.split(','))
                if commands[0] == 'PLACE'