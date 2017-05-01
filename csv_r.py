#coding:utf-8

f_name=raw_input("データファイル名：")
data_file=open(f_name,'r')

for d in data_file:
    data=d.split(',') #リスト型で３つにくぎる
    name=data[0]
    tall=float(data[1]) #少数に戻す
    weight=float(data[2]) #少数に戻す
    bmi=weight/pow(tall,2)
    print("%sさんのBMIは%0.2fです" %(name,bmi))

data_file.close()
