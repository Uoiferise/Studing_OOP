class Point:
    """Description"""

    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __getattribute__(self, item):
        print('__getattribute__')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print('__setattr__')
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        print('__getattr__')
        return False

    def __delattr__(self, item):
        print('__delattr__')
        object.__delattr__(self, item)