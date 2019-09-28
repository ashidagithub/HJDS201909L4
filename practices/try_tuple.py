# -*- coding: UTF-8 -*-
import random

'''
1) Create tuple
'''
a = ()

'''
2) Assignment list
'''
a = ('Archie', 'Leon', 'Cynthia', 'Eathson', 'Kevin')
b = (1, 2, 3, 4, 5, 6)

print(a)
print(b)

'''
3) Append/Extend
'''
a = ('Archie', 'Leon', 'Cynthia', 'Eathson', 'Kevin', 'Mike')
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
print('Lenth of tuple a is %d' % lenth)


'''
7) Pick
'''
index = 3
print(a[index])

lenth = len(a)
for i in range(lenth):
    print(a[i])

print('-----cutting line-----')
for element in a:
    print (element)

print('-----cutting line-----')
for i in range(5):
    lucky = random.choice(a)
    print(lucky)
