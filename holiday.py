# coding: UTF-8

import datetime
today=datetime.datetime.now()
if today.weekday()<4:
    print('学校に行こう！')
elif today.weekday()==4:
    print('明日は休みだ！')
else:
    print('ゆっくり休もう！')
