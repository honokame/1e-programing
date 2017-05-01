#coding:utf-8

f_name=raw_input("データファイル名：")
data_file=open(f_name,'w')

for n in range(3):
    name=raw_input("氏名：")
    tall=input("身長（m）：")
    weight=input("体重（kg）：")
    d=name+','+str(tall)+','+str(weight)+'\n'
    data_file.write(d)

data_file.flush()
data_file.close()
