# -*- coding: UTF-8 -*-
import random

family_words = ("赵", "钱", "孙", "李", "周", "吴", "郑", "王")

index = 3
print("%s" % (family_words[index]))

for name in family_words:
    print("%s " % name, end="")
print('\n')

print('-----cutting line-----')
times = 5
print('总共有 %d 个姓供挑选，计划挑选 %d 次' %  (len(family_words), times))

for i in range(times):
    print('picked family name is : %s' %
          (random.choice(family_words)))
