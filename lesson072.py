def func1(a, b, c):
    print(a, b, c)

func1(1,2,3)
func1(1,c=3,b=2)
func1(c=3,b=2,a=1)
print('-'*80)

def func1(a, b, *args):
    print(a, b, args)

func1(1,2,3, 4)
print()

def func1(a, b, *args, d):
    print(a, b, args, d)

#func1(1,2,3, 4, 5)
func1(1,2,3, 4, d=5)
print('-'*80)

def func1(*args, d):
    print(args, d)

#func1(1,2,3, 4, 5)
func1(1,2,3,d='a')
func1(d='a')
print('-'*80)

def func1(*, d):
    print(d)

#func1(1,2,d=100)
func1(d=100)
print('-'*80)

def func(a,b,*,d):
    print(a)
    print(b)
    print(d)

#func(1,2, 3, d=4 )
func(1,2, d=4 )
print('-'*80)

def func(a,b=2,*args,d):
    print(a)
    print(b)
    print(args)
    print(d)

func(1,5,3,4,d='a' )
print('-'*80)

def func(a,b=20,*args,d=0, e):
    print(a)
    print(b)
    print(args)
    print(d)
    print(e)

#func(5,4,3,2,1)
func(5,4,3,2,1,e='all engines running')
print()
func(0,600,d='goood morning',e='python!')
print()
func(11,'m/s',24,'mph',d='unladen',e='swallow')
print('-'*80)



