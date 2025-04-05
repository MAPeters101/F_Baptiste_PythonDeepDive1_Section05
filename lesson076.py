import time

def time_it(fn, *args, **kwargs):
    print(args, kwargs)

time_it(print, 1, 2, 3, sep=' - ', end=' ***')
print('-'*80)

def time_it(fn, *args, **kwargs):
    fn(args, kwargs)

time_it(print, 1, 2, 3, sep=' - ', end=' ***')
print((1,2,3), {'sep': ' - ', 'end': ' ***'})
print('-'*80)

def time_it(fn, *args, **kwargs):
    fn(*args, **kwargs)

time_it(print, 1, 2, 3, sep=' - ', end=' ***')
print()
print('.'*80)

def time_it(fn, *args, rep=1, **kwargs):
    for i in range(rep):
       fn(*args, **kwargs)

time_it(print, 1, 2, 3, sep=' - ', end=' ***\n', rep=5)
print('='*80)

def time_it(fn, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
       fn(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) / rep

print(time_it(print, 1, 2, 3, sep=' - ', end=' ***\n', rep=5))
print('='*80)

