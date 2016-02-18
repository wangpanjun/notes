# encoding=utf-8

__author__ = 'xiaowang'
__date__ = '18/2/16'


def multipliers():
    return [lambda x : i * x for i in range(4)]


print([m(2) for m in multipliers()])


