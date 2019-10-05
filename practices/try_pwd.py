# -*- coding: UTF-8 -*-

import random

for times in range(10):
    # numberic
    password = random.randint(0,999999)
    # s_pwd = string_of_password
    s_pwd = '%06d' % password
    print(s_pwd)


print('\n---cutting line ---')
nums = ('0','1','2','3','4','5','6','7','8','9')

lenth = 8
pwd = ''
for i in range(lenth):
    s = random.choice(nums)
    pwd += s
print(pwd)


print('\n\n---cutting line 3---')
# 定义所有可用的字符
char1 = ['0','1','2','3','4','5','6','7','8','9']
char2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
char3 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
char4 = ['~','!','@','#','$','%','^','&','*','(',')','_','+','-','=','{','}','[',']',':','"',';','<','>','?',',','.','/']
# 合并到一个打的列表中去
char_All = char1 + char2 + char3 + char4
lenth = 16

for i in range(10):
    pwd = ''
    for i in range(lenth):
        s = random.choice(char_All)
        pwd += s
    print(pwd)
