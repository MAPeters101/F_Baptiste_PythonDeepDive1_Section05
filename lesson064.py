
def my_func(a,b,c):
    print("a={0}, b={1}, c={2}".format(a,b,c))

my_func(1,2,3)
#my_func(1,2)
print()

# def my_func(a,b=2,c):
#     print("a={0}, b={1}, c={2}".format(a,b,c))
# my_func(1,2,3)

def my_func(a=1,b=2,c=3):
    print("a={0}, b={1}, c={2}".format(a,b,c))
my_func(10,20,30)
my_func(10,20)
my_func(10)
my_func()
print('-'*80)


