# coding:utf-8

print('今からあなたのローレル指数を測定します。')

print('あなたの体重を入力してください（ｋｇ）')
weight=input()

print('あなたの身長を入力してください（ｍ）')
high=input()

ri=weight/high**3*10

print('あなたのローレル指数は%0.2fです。'%ri)
