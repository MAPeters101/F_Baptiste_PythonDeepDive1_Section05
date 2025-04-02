l = [1, 2, 3, 4, 5, 6]
a = l[0]
b = l[1:]
print(a)
print(b)
print()

a, b = l[0], l[1:]
print(a)
print(b)
print()

a, *b = l
print(a)
print(b)
print('-'*80)

s = {1,2,3}
# a = s[0]
# b = s[1:]
a, *b = s
print(a)
print(b)
print('-'*80)

s = 'python'
a = s[0]
b = s[1:]
print(a)
print(b)
print()

a, *b = s
print(a)
print(b)
print()

t = ('a', 'b', 'c')
a = t[0]
b = t[1:]
print(a)
print(b)
print()

a, *b = t
print(a)
print(b)
print()
print('-'*80)

[a,b,c] = 'XYZ'
print(a)
print(b)
print(c)
print('='*80)

a, b, *c = 'python'
print(a)
print(b)
print(c)
print()

a, b, *c, d = 'python'
print(a)
print(b)
print(c)
print(d)
print()

s = 'python'
a,b,c,d = s[0], s[1], s[2:-1] ,s[-1]
print(a)
print(b)
print(c)
print(d)
print()

s = 'python'
a,b,c,d = s[0], s[1], s[2:-1] ,s[-1]
*c, = c
print(a)
print(b)
print(c)
print(d)
print()

s = 'python'
a,b,c,d = s[0], s[1], s[2:-1] ,s[-1]
print(a)
print(b)
print(list(c))
print(d)
print('-'*80)








