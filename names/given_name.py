# -*- coding: UTF-8 -*-

import random

print('-----cutting line-----')
given_words = [ \
"致浩", "明云", "浩烨", "兆忠", "予忻", "顺雨", "尚扬", \
"俊祥", "语禅", "予浩" \
]

given_words1 = [ \
"潮","彻","郴","琛","澈","臣","辰","晨","承","盛","程", "池", \
"炽","冲","重","崇","绸","畴","酬","筹","楚","处" \
]

#all_given_words = given_words + given_words1
given_words.extend(given_words1)
print(given_words)

given_name = random.choice(given_words)
print(given_name)

times = 5
for i in range(times):
    print('picked given name is : %s' % (random.choice(given_words)))
