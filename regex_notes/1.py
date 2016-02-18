# encoding=utf-8

__author__ = 'xiaowang'
__date__ = '18/2/16'


import re

s = '<html><head><title>Title</title>'
print(re.match('<.*>', s).group())
print(re.match('<.*?>', s).group())
