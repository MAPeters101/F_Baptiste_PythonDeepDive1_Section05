from datetime import datetime
from time import sleep

print(datetime.utcnow())
sleep(.5)
print(datetime.utcnow())
sleep(.5)
print(datetime.utcnow())
sleep(.5)
print(datetime.utcnow())

def log(msg, *, dt=datetime.utcnow()):
    print('{0}: {1}'.format(dt, msg))

log('message 1', dt='2001_01-01 00:00:00.000')
log('message 1a', dt='2010_01-01 00:00:00.000')
log('message 2')
sleep(.5)
log('message 3')
sleep(.5)
log('message 3')
sleep(.5)
def log(msg, *, dt=datetime.utcnow()):
    print('{0}: {1}'.format(dt, msg))

log('message 4')
sleep(.5)
log('message 4')
print('-'*80)

def log(msg, *, dt=None):
    if not dt:
        dt = datetime.utcnow()
    print('{0}: {1}'.format(dt, msg))

log('message 1', dt='2001_01-01')

log('message 2')
sleep(1)
log('message 3')
print('.'*80)

def log(msg, *, dt=None):
    dt = dt or datetime.utcnow()
    # if not dt:
    #     dt = datetime.utcnow()
    print('{0}: {1}'.format(dt, msg))

log('message 1', dt='2001_01-01')

log('message 2')
sleep(1)
log('message 3', dt=None)
print('-'*80)

my_list = [1,2,3]
def func(a=my_list):
    print(a)

func()
func(['a', 'b'])
my_list.append(4)
func()
print('.'*80)




