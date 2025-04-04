def func(**others):
    print(others)
func(a=1,b=2,c=3)
print('-'*80)

def func(*args, **kwargs):
    print(args)
    print(kwargs)
#func(1, 2, x=100, y=200, 12)
func(1, 2, x=100, y=200)
print('-'*80)




