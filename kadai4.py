# coding:utf-8

print('今からあなたのBMIを測定します')

import random

height=1*random.random()+1
heights=round(height,1)
weight=70*random.random()+30
weights=round(weight,1)

bmi=weights/heights**2


print('体重 %0.1f(kg)、身長 %0.1f (ｍ)の人のBMIは %0.1f です'%(weights,heights,bmi))