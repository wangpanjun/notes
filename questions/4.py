# encoding=utf-8

__author__ = 'xiaowang'
__date__ = '18/2/16'


def my_range(start, stop=None, step=None):
    if not step: step = 1
    if (stop - start) * step <= 0: yield []
    if not stop:
        start, stop = 0, start
    while True:
        if (stop - start) * step > 0:
            yield start
            start += step

        else:
            break


sd = my_range(10, 11, -1)
for i in sd:
    print(i)
