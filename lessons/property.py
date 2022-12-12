class Vector:
    """Description"""

    def __init__(self, x, y):
        print('вызов init')
        self.__x, self.__y = x, y

    @property
    def x(self):
        print('вызов getter')
        return self.__x

    @x.setter
    def x(self, x):
        print('вызов setter')
        self.__x = x

    @x.deleter
    def x(self):
        print('вызов deleter')
        del self.__x
