# encoding=utf-8

__author__ = 'xiaowang'
__date__ = '17/2/16'


# def deco(func):
#     print 2
#     func()
#     print 3
#     return func
#
#
# @deco
# def func():
#     print 1
#
#
# func()
# func()
#
# def deco(func):
#     def _deco():
#         print 2
#         func()
#         print 3
#
#     return _deco
#
#
# @deco
# def myfunc():
#     print 1
#     return 'OK'
#
#
# myfunc()
# myfunc()

# def deco(func):
#     def _deco(a, b):
#         ret = func(a, b)
#         return ret
#
#     return _deco
#
#
# @deco
# def myfunc(a, b):
#     return a +b
#
#
# print myfunc(1,2)
# print myfunc(3,5)


def deco(func):
   def _deco(*args, **kwargs):
      print 3
      ret = func(*args, **kwargs)
      print 2
      return ret

   return _deco


@deco
def myfunc(a, b):
   print 1
   return a+b

