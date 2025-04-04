import time

def time_it(fn, * args, **kwargs):
    print(args, kwargs)

time_it(print, 1, 2, 3, sep=' - ', end=' ***')

