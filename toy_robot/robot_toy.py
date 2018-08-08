from toy_robot.py_coordinates import PyCoordinates


class RobotToy(object):

    def __init__(self):
        self._position = PyCoordinates()
        self._direction = None

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, val):
        if val in ('N', 'E', 'S', 'W'):
            self._direction = val
        else:
            raise ValueError('Direction can only be N, E, S, or W.')

    @property
    def position(self):
        return self._position

    def place_robot(self, dir, coord_x, coord_y):
        self.direction = dir
        self.position.x = coord_x
        self.position.y = coord_y

    def move_forward(self):
        if self.direction == 'N':
            self.position.y += 1
        elif self.direction == 'E':
            self.position.x += 1
        elif self.direction == 'S':
            self.position.y -= 1
        elif self.direction == 'W':
            self.position.x -= 1
    