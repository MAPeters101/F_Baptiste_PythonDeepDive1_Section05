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


