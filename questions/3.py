# encoding=utf-8

__author__ = 'xiaowang'
__date__ = '18/2/16'


def my_range(start, stop=None, step=None):
    if not step: step = 1
    if (stop - start) * step <= 0: return []
    result = []
    if not stop:
        start, stop = 0, start
    while True:
        if (stop - start) * step > 0:
            result.append(start)
            start += step

        else:
            break

    return result


print my_range(10, 1, 0)

