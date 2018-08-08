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

    