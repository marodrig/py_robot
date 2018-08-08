from toy_robot.py_coordinates import PyCoordinates
from functools import wraps


class RobotToy(object):
    """
    Represents Robot Toy.
    """

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
        """
        Checks if the robot has been placed before executing the given method

        :param func: function called
        :func type: python function

        """

        @wraps(func)
        def wrapper_func(self, *args, **kwargs):
            if self.position.x and self.position.y or self.position.x == 0 or self.position.y == 0:
                return func(self, *args, **kwargs)
            print('Please place robot first.')
        return wrapper_func

    def place_robot(self, dir_facing, coord_x, coord_y):
        """
        Assigns the location and direction of the toy robot.

        :param dir_facing: Direction the toy is facing
        :dir_facing type: str

        :param coord_x: x coordinate of the toy 
        :coord_x type: int

        :param coord_y: y coordinate of the toy
        :coord_y type: int

        """
        self.direction = dir_facing
        self.position.x = coord_x
        self.position.y = coord_y

    @robot_placed_required
    def move_forward(self):
        """
        Moves robot forward in the direction it's facing
        """
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
        return "Position:(x = {0}, y = {1}). Facing: {2}".format(
                self.position.x,
                self.position.y,
                self.direction)
