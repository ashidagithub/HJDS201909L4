# -*- coding: UTF-8 -*-
import random

# Define family names
family_words = ("赵", "钱", "孙", "李", "周", "吴", "郑", "王")

# Define given words
given_words = ["致浩", "明云", "浩烨", "兆忠", "予忻", "顺雨", "尚扬", "俊祥", "语禅", "予浩"]
given_words1 = [ \
"潮","彻","郴","琛","澈","臣","辰","晨","承","盛","程", "池", \
"炽","冲","重","崇","绸","畴","酬","筹","楚","处" \
]
given_words.extend(given_words1)

# Define sex
sex = ('Female', 'Male')

# Create a new full name
full_name = ''
class_name = []

times = 30
for i in range(times):
    fname = random.choice(family_words)
    lname = random.choice(given_words)
    full_name = fname + ' ' + lname
    #print(full_name)

    '''
    sex = random.randint(1,100)
    if (sex % 2) == 0:
        s_sex = 'Female'
    else:
        s_sex = 'Male'
    '''
    s_sex = random.choice(sex)
    student = (full_name, s_sex)
    print(student)

    class_name.append(student)

print('-----cutting line-----')
print(class_name)
