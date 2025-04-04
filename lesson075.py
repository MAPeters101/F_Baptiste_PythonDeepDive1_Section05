def func(a, b, *args):
    print(a)
    print(b)
    print(args)
func(1,2,'x','y','z')
#func(a=1,b=2,'x','y','z')
print('-'*80)

def func(a, b=2, c=3, *args):
    print(a)
    print(b)
    print(c)
    print(args)
func(1,2,3,'x','y','z')
func(1,4,3,'x','y','z')
print('-'*80)




