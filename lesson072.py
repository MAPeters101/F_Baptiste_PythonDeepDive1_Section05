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


