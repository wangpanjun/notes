# encoding=utf-8

__author__ = 'xiaowang'
__date__ = '18/2/16'


def singleton(cls, *args, **kw):
    instance = {}

    def get_instance():
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]

    return get_instance


@singleton
class MyClass:
    a =1


a1 = MyClass()
a2 = MyClass()

print(a1 is a2)
