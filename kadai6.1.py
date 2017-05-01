# coding: utf-8

import random

answer = random.randint(1, 100)
n = 0

while True:

    n = int(input('1〜100のなかから数字を入力してください: '))

    if n < answer:
        print('もっと大きい!')

    elif n > answer:
      print('もっと小さい!')

    else:
      print('正解!!')
      break

