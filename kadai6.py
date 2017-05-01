# coding: utf-8
import math
print('二次方程式y=ax^2+bx+cの係数を入れてください')

a=input('a:')
b=input('b:')
c=input('c:')
d=math.pow(b,2)
e=4*a*c

if d < e:
    print('解なし')

elif a == 0: 
    if b == 0:
        print('なし')

elif a == 0:
    x1 = -c/b
    print ('解は %0.2f です '%(x1))


else:
    f=math.sqrt(d-e)
    x3 = (-b + f / (2*a))
    x4 = (-b - f / (2*a))
    print ('解は %0.2f と %0.2f です '%(x3,x4))
