import sys
from toy_robot.robot_toy import RobotToy


class ToyHandler(object):
    def __init__(self):
        self.toy = RobotToy()

    def read_command(self):
        with sys.stdin as py_stdin:
            for line in py_stdin:
                commands = list(line.split(','))
                if commands[0] == 'PLACE':
                    self.toy.place_robot(coord_x=commands[1], 
                                         coord_y=commands[2], 
                                         dir_facing=commands[3])
                elif commands[0] == 'MOVE':
                    self.toy.move_forward()
                elif commands[0] == 'LEFT':
                    self.toy.rotate_left()
                elif commands[0] == 'RIGHT':
                    self.toy.rotate_right()
                elif commands[0] == 'REPORT':
                    print(self.toy)
                else:
                    print('Bad command.')


if __name__ == '__main__':
    handler = ToyHandler()
    handler.read_command()
