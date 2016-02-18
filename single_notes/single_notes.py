# encoding=utf-8

__author__ = 'xiaowang'
__date__ = '18/2/16'


class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance



class MyClass(Singleton):
    a = 1

a1 = MyClass()
a2 = MyClass()

print(a1 is a2)

