from toy_robot.py_coordinates import PyCoordinates
from functools import wraps


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

    def robot_placed_required(func):

        @wraps(func)
        def wrapper_func(self, *args, **kwargs):
            if not self.position.x and not self.position.y:
                raise ValueError('Bad.')
            return func(self, *args, **kwargs)
        return wrapper_func

    def place_robot(self, dir_facing, coord_x, coord_y):
        self.direction = dir_facing
        self.position.x = coord_x
        self.position.y = coord_y

    @robot_placed_required
    def move_forward(self):
        if self.direction == 'N':
            self.position.y += 1
        elif self.direction == 'E':
            self.position.x += 1
        elif self.direction == 'S':
            self.position.y -= 1
        elif self.direction == 'W':
            self.position.x -= 1

    @robot_placed_required
    def rotate_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction == 'N'

    @robot_placed_required
    def rotate_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction == 'N'

    def __str__(self):
        return "Position:(x = {0}, y ={1}). Facing: {2}".format(
                self.position.x,
                self.position.y,
                self.direction)
