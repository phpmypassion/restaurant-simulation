# MenuItem.py
# Goal: This class will represent a single item that a diner can order from the restaurant’s menu

class MenuItem(object):
    def __init__(self, name, type, time, description, chefs):
        self.__name = name
        self.__type = type
        self.__time = time
        self.__description = description
        self.__chefs = chefs

    # more format tricks: https://pyformat.info/
    def __str__(self):
        return '{p.name} ({p.type}) Num.of.Chefs Available({p.chefs}) Time Takes: {p.time} min\n{p.description}'.format(p=self)

    __repr__ = __str__

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        self.__time = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def chefs(self):
        return self.__chefs

    @chefs.setter
    def chefs(self, value):
        self.__chefs = value
