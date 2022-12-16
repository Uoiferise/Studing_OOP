from string import ascii_letters


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


class Person:
    """Description"""
    __ru_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    __letters = ascii_letters + __ru_letters + __ru_letters.upper()

    def __init__(self, fio, old, passport):
        self.__fio = fio
        self.__old = old
        self.__passport = passport

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('fio type must be str')

        fio = fio.split
        if len(fio) != 3:
            raise TypeError('wrong fio format')

        for item in fio:
            if len(item.strip(cls.__letters)) != 0:
                raise TypeError('fio must contain only letters and symbol "-"')
