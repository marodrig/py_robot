import sys
from toy_robot.robot import RobotToy


class ToyHandler(object):
    """
    Handles the commands for the toy robot
    """
    def __init__(self):
        self.toy = RobotToy()

    def read_command(self):
        """
        Reads commands from STDIN for the toy robot
        """
        with sys.stdin as py_stdin:
            for line in py_stdin:
                commands = list([str(x).rstrip() for x in line.split(' ')])
                if commands[0] == 'PLACE':
                    try:
                        self.toy.place_robot(
                            coord_x=commands[1].strip(','),
                            coord_y=commands[2].strip(','),
                            dir_facing=commands[3][0])
                    except ValueError as ve:
                        print(ve)
                elif commands[0] == 'MOVE':1
                    try:
                        self.toy.move_forward()
                    except ValueError as ve:
                        print(ve)
                elif commands[0] == 'LEFT':
                    self.toy.rotate_left()
                elif commands[0] == 'RIGHT':
                    self.toy.rotate_right()
                elif commands[0] == 'REPORT':
                    print(self.toy)
                else:
                    break


if __name__ == '__main__':
    handler = ToyHandler()
    handler.read_command()
