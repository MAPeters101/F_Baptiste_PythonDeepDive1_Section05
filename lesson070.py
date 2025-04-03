a, b, *c = 10, 20, 'a', 'b'
print(a)
print(b)
print(c)
print()

def func1(a, b, *c):
    print(a)
    print(b)
    print(c)
    print()

func1(10, 20)
func1(10, 20, 1, 2, 3)

def func1(a, b, *args):
    print(a)
    print(b)
    print(args)
    print()

func1(10, 20)
func1(10, 20, 1, 2, 3)
print('-'*80)

def avg(*args):
    print(args)

avg()
avg(10, 20)
print()

def avg(*args):
    count = len(args)
    total = sum(args)
    return total/count

print(avg(2, 2, 4, 4))
#print(avg())
print('-'*80)

def avg(*args):
    count = len(args)
    total = sum(args)
    if count == 0:
        return 0
    else:
        return total/count

print(avg(2, 2, 4, 4))
print(avg())
print('-'*80)

def avg(*args):
    count = len(args)
    total = sum(args)
    return count and total/count

print(avg(2, 2, 4, 4))
print(avg())
print('-'*80)




