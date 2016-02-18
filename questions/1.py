# encoding=utf-8

__author__ = 'xiaowang'
__date__ = '17/2/16'


import itertools
l1 = [1, 2, 3, 4, 1]
print {}.fromkeys(l1).keys()
print list(set(l1))
print reduce(lambda x, y: x if y in x else x+[y], [[]]+l1)
print [key for key, group in itertools.groupby(sorted(l1))]



print reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 0)
print map(lambda x: x * x, [1, 2, 3, 4, 5])



#
# class A(object):
#
#     def __init__(self, data):
#         self.data = data
#
#     def __len__(self):
#         return 1
#
#     def __add__(self, other):
#         return self.data + other.data
#
#
# a1 = A(1)
# a2 = A(2)
# print a1 + a2


