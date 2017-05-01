# coding: utf-8

def color2value(color):
    if color=='Black':
        return 0
    elif color=='Blown':
        return 1
    elif color=='Red':
        return 2
    elif color=='Orange':
        return 3
    elif color=='Yellow':
        return 4
    elif color=='Green':
        return 5
    elif color=='Blue':
        return 6
    elif color=='Violet':
        return 7
    elif color=='Gray':
        return 8
    elif color=='White':
        return 9
    else:
        return 100
def gosa(color):
    if  color=='Blown':
        return 1
    elif color=='Red':
        return 2
    elif color=='Orange':
        return 0.05
    elif color=='Green':
        return 0.5
    elif color=='Blue':
        return 0.25
    elif color=='Violet':
        return 0.1
    elif color=='gold':
        return 5
    elif color=='Silber':
        return 10
    else:
        return 0.0000

print('抵抗の値を求めます')
n=input('カラーコードの数は？')
if n==4:
    print('\n抵抗の色を次の中から選んでください')
    print('黒：Black,茶：Brown,赤：Red,橙：Orange,黄：Yellow,緑：Green,青：Blue,紫：Violet,灰：Gray,白：White\n')
    color=raw_input('１つ目：')
    color1=raw_input('２つ目：')
    print('\n乗数の色は次の中から選んでください（黒：Black,橙：Orange,青：Blue）\n')
    color2=raw_input('乗数の色は? ：')
    print('\n誤差の色は次の中から選んでください(黒：Black,茶：Brown,赤：Red,橙：Orange,黄：Yellow,緑：Green,青：Blue,紫：Violet,灰：Gray,白：White,金：Gold,銀：Silver)\n')
    color3=raw_input('誤差の色は? ：')
    value=color2value(color)
    value1=color2value(color1)
    value2=color2value(color2)
    value3=gosa(color3)
    teikou=str(value)+str(value1)
    if value2==0:
        print('\n抵抗値は %sΩ、誤差は　±%0.2f％ です')%(teikou,value3)
    elif value2==3:
        print('\n抵抗値は %skΩ、誤差は　±%0.2f％です')%(teikou,value3)
    elif value2==6:
         print('\n抵抗値は %sMΩ、誤差は　±%0.2f％ です')%(teikou,value3)
    else:
        print('3つめの色はBlack,Orange,Blueです')

elif n==5:
    print('\n抵抗の色を次の中から選んでください')
    print('黒：Black,茶：Brown,赤：Red,橙：Orange,黄：Yellow,緑：Green,青：Blue,紫：Violet,灰：Gray,白：White\n')
    color=raw_input('１つ目：')
    color1=raw_input('２つ目：')
    color2=raw_input('３つ目 ：')
    print('\n乗数の色は次の中から選んでください（黒：Black,橙：Orange,青：Blue）\n')
    color3=raw_input('乗数の色は? ：')
    print('\n誤差の色は次の中から選んでください(黒：Black,茶：Brown,赤：Red,橙：Orange,黄：Yellow,緑：Green,青：Blue,紫：Violet,灰：Gray,白：White,金：Gold,銀：Silver)\n')
    color4=raw_input('誤差の色は? ：')
    value=color2value(color)
    value=color2value(color1)
    value1=color2value(color2)
    value2=color2value(color3)
    value4=gosa(color4)
    teikou=str(value)+str(value1)+str(value2)
    if value2==0:
        print('抵抗値は %sΩ、誤差は　±%0.2f％ です')%(teikou,value4)
    elif value2==3:
        print('抵抗値は %skΩ、誤差は　±%0.2f％ です')%(teikou,value4)
    elif value2==6:
         print('抵抗値は %sMΩ、誤差は　±%0.2f％ です')%(teikou,value4)
    else:
        print('3つめの色はBlack,Orange,Blueです')

    
