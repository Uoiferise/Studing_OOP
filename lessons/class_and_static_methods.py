class Vector:
    """Description"""

    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def __validation(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod
    def __check_value(arg):
        result = type(arg) in (int, float)
        return result if result else ValueError('Неверный формат или недопустимое значение')

    def __init__(self, x, y):
        self.__x = self.__y = 0
        if self.__validation(x) and self.__validation(y):
            self.__x, self.__y = x, y

    def set_coord(self, x, y):
        if self.__validation(x) and self.__validation(y):
            self.__x, self.__y = x, y
        else:
            raise ValueError('Неверный формат или недопустимое значение')

    def get_coord(self):
        return self.__x, self.__y

    @staticmethod
    def norm2(x, y):
        return x ** 2 + y ** 2
