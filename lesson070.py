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



