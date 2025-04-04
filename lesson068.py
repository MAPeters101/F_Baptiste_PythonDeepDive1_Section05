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

l1 = [1,2,3]
l2 = [4,5,6]
l = [*l1, *l2]
print(l)
print()

l1 = [1,2,3]
s = 'abc'
print([*l1, *s])
print()

l1 = [1,2,3]
s1 = {'x', 'y', 'z'}
print([*l1, *s1])
print('-'*80)

s1 = 'abc'
s2 = 'cde'
print([*s1, *s2])
print()

print({*s1, *s2})
print('-'*80)

s = {10, -99, 3, 'd'}
for c in s:
    print(c)
print()

a,b,c,d = s
print(a)
print(b)
print(c)
print(d)
print()

a,b,*c = s
print(a)
print(b)
print(c)
print()
print('-'*80)

s = {10, -99, 3, 'd'}
print(list(s))

*c, = s
print(c)
print('-'*80)

s1 = {1,2,3}
s2 = {3,4,5}
#print(s1 + s2)
print({*s1, *s2})
c = {*s1, *s2}
print(c)
help(set)
print(s1.union(s2))
print('-'*80)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = {5,6,7}
s4 = {7,8,9}
print(s1.union(s2).union(s3).union(s4))
print(s1.union(s2, s3, s4))
print([*s1, *s2, *s3, *s4])
print({*s1, *s2, *s3, *s4})
print('-'*80)

d1 = {'key1': 1, 'key2': 2}
d2 = {'key1': 3, 'key4': 4}

print({*d1, *d2})
print({**d1, **d2})
print({**d2, **d1})
print('-'*80)

print({'a':1, 'b':2, **d1, 'c':3})
print('-'*80)

a,b,e = [1,2,'XY']
print(a)
print(b)
print(e)
c,d = e
print(c)
print(d)
print()

a,b,(c,d) = [1,2,'XY']
print(a)
print(b)
print(c)
print(d)
print()

a,b,(c,d, *e) = [1,2,'python']
print(a)
print(b)
print(c)
print(d)
print(e)
print()
print('-'*80)

l = [1,2,3,4,'python']
a,*b,(c,d, *e) = l
print(a)
print(b)
print(c)
print(d)
print(e)
print()

l = [1,2,3,4,'python']
print(l[0], l[1:-1], l[-1][0], l[-1][1], l[-1][2:])
print(l[0], l[1:-1], l[-1][0], l[-1][1], list(l[-1][2:]))

a,b,c,d,e = l[0], l[1:-1], l[-1][0], l[-1][1], list(l[-1][2:])
print(a)
print(b)
print(c)
print(d)
print(e)
print()
print('-'*80)

l = (1,2,3,4,['a','b','c','d'])
a,*b,(c,d, *e) = l
print(a)
print(b)
print(c)
print(d)
print(e)
print()

a,b,c,d,e = l[0], l[1:-1], l[-1][0], l[-1][1], list(l[-1][2:])
print(a)
print(b)
print(c)
print(d)
print(e)
print()

a,b,c,d,e = l[0], list(l[1:-1]), l[-1][0], l[-1][1], list(l[-1][2:])
print(a)
print(b)
print(c)
print(d)
print(e)
print()



