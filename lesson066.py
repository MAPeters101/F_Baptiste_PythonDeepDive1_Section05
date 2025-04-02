a = (1,2,3)
print(type(a))
a = 1,2,3
print(type(a))
print(a)
a = (1)
print(type(a))
print(a)

a = ('a')
print(type(a))
print(a)

a = (1,)
print(type(a))
print(a)

a = 1,
print(type(a))
print(a)
print('-'*80)

a = ()
print(type(a))
print(a)

# a = ,
# print(type(a))
# print(a)

# a = (,)
# print(type(a))
# print(a)
print('-'*80)

a, b, c = [1, 'a', 3.14]
print(a)
print(b)
print(c)
print()

(a, b, c) = [1, 'a', 3.14]
print(a)
print(b)
print(c)
print()

a, b = (1,2)
print(a)
print(b)
print()

(a, b) = (1,2)
print(a)
print(b)
print()
print('='*80)

a, b = 10, 20
print(a)
print(b)
print()

a, b, c = 10, 20, 30
print(a)
print(b)
print(c)
print()

a, b, c = 10, 'a', 3.14
print(a)
print(b)
print(c)
print()

a, b, c = 10, {1,2}, ['a','b']
print(a)
print(b)
print(c)
print()
print('-'*80)

a, b = 10, 20
print(a)
print(b)
print()

a, b = b, a
print(a)
print(b)
print()

c = (id(b), id(a))
print(c)
a,b = c
print(a)
print()

a, b = 10, 20
print(a)
print(b)
a, b = b, a
print(a)
print(b)
print()
print('='*80)

for e in 'XYZ':
    print(e)
print()

a,b,c = 'XYZ'
print(a)
print(b)
print(c)

s = 'XYZ'
print(s[0])
print(s[1])
print()

s = {1,2,3}
# print(s[0])
# print(s[1])
print()

s = {'p', 'y', 't', 'h', 'o', 'n'}
print(s)
for e in s:
    print(e)
print()
a,b,c,d,e,f = s
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print('-'*80)

d = {'a':1, 'b':2, 'c':3}
for e in d:
    print(e)
print()
a,b,c = d
print(a)
print(b)
print(c)
print()

d = {'a':1, 'b':2, 'c':3, 'd':4}
print(d)
a,b,c,d = d
print(a)
print(b)
print(c)
print(d)
print('.'*80)

d = {'a':1, 'b':2, 'c':3, 'd':4}
print(d)
d,a,b,c = d
print(a)
print(b)
print(c)
print(d)
print('-'*80)

