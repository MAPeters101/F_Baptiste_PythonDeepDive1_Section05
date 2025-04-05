import time

def time_it(fn, * args, **kwargs):
    print(args, kwargs)

time_it(print, 1, 2, 3, sep=' - ', end=' ***')
print('-'*80)

def time_it(fn, * args, **kwargs):
    fn(args, kwargs)

time_it(print, 1, 2, 3, sep=' - ', end=' ***')
print((1,2,3), {'sep': ' - ', 'end': ' ***'})
print('-'*80)

def time_it(fn, * args, **kwargs):
    fn(*args, **kwargs)

time_it(print, 1, 2, 3, sep=' - ', end=' ***')
print()
print('-'*80)

