# coding:utf-8

height=input('身長(m)は')
weight=input('体重（kg）は')
bmi=weight/height**2

print('あなたのBMIは %0.2f です')%bmi

if bmi<18.5:
    print('低体重（痩せ型）')
elif bmi<25:
    print('普通体重')
elif bmi<30:
    print('肥満（１度）')
elif bmi<35:
    print('肥満（２度）')
elif bmi<40:
    print('肥満（３度）')
else:
    print('肥満（４度）')
