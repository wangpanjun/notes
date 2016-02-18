# encoding=utf-8

__author__ = 'xiaowang'
__date__ = '18/2/16'


class Singleton(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super(Singleton, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        print(ob)
        return ob



# class MyClass(Singleton):
#     a = 1
#
#
# a1 = MyClass()
# a2 = MyClass()
# print(a1 is a2)
