class PyCoordinates(object):

    def __init__(self):
        self._x = None
        self._y = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        val = int(val)
        if val >= 0 and val <= 4:
            self._x = int(val)
        else:
            raise ValueError('X has to be between 0 and 4.')

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        val = int(val)
        if val >= 0 and val <= 4:
            self._y = val
        else:
            raise ValueError('Y has to be between 0 and 4.')
