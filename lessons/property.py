class Vector:
    def __init__(self, x, y):
        self.__x, self.__y = x, y

    @property
    def x(self):
        print('вызов getter')
        return self.__x

    @x.setter
    def x(self, arg):
        print('вызов setter')
        self.__x = arg

    @x.deleter
    def x(self):
        print('вызов deleter')
        del self.__x
