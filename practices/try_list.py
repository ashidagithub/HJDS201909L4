# -*- coding: UTF-8 -*-

import random

'''
1) Create list
'''
a = []

'''
2) Assignment list
'''
a = ['Archie', 'Leon', 'Cynthia', 'Eathson', 'Kevin']
b = [1, 2, 3, 4, 5, 6]

print(a)
print(b)

'''
3) Append/Extend
'''
a += ['Mike']
print(a)

for i in range(3):
    a.append('xxx')
print(a)

a.extend(b)
print(a)

'''
5) Joint
'''
c = a + b
print(c)

'''
6) Lenth
'''
lenth = len(a)
print('Lenth of list a is %d' % lenth)

'''
7) Pick
'''
index = 9
print(a[index])

lenth = len(a)
for i in range(lenth):
    print(a[i])

print('-----cutting line-----')
for element in a:
    print(element)

print('-----cutting line-----')
for i in range(5):
    lucky = random.choice(a)
    print(lucky)

'''
8) Change
'''
a = ['Archie', 'Leon', 'Cynthia', 'Eathson', 'Kevin']

index = 3
a[index] = 'Cosmo'
print('-----cutting line-----')
print(a)

'''
9) Delete
'''
a = ['Archie', 'Leon', 'Cynthia', 'Eathson', 'Kevin']

index = 3
del a[index]
print('-----cutting line-----')
print(a)

print('-----cutting line-----')
a.clear()
print(a)
