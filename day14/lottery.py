import random
import time
lotts=['{:04d}'.format(i) for i in range(10000)]
"""
print('{}の２倍は{}'.format(10,20))
print(f'{10}の２倍は{20}')
print(f'{10:04d}の２倍は{20:04d}')
print(f'{3.141592:.2f}の２倍は{20:04d}')
#print(lotts)#10000枚の宝くじを出力
n1=random.randint(1,6)
print(n1)
n2=random.randrange(2,10)
print(n2)
data=["red","green","blue"]
color=random.choice(data)
ret=random.shuffle(data)
print(ret)
print(type(ret))
print(color)
"""
n=int(input("宝くじを何枚買いますか?"))
my_lotts=sorted(random.sample(lotts,n))#重複なし指定枚数取れるメソッド
print(my_lotts)

lucky='{:04d}'.format(random.randrange(10000))
print("抽選開始...")
print(lucky[0])#先頭の文字

for c in lucky:#python は文字列を直接for文に書ける
    time.sleep(1)
    print(c)

result=[[]for i in range(4)]#骨組み作る後はappendで作る空の要素４つの２次元配列
for lott in my_lotts:
    if lucky==lott:
        result[0].append(lott)
    elif lucky[-3:]==lott[-3:]:
        result[1].append(lott)
    elif lucky[-2:]==lott[-2:]:
        result[2].append(lott)
    elif lucky[-1]==lott[-1]:
        result[3].append(lott)
        
for i in range (len(result)):#resultは要素４つの２次元配列０１２３の４回取り出す
    print('{}等賞({:*>4s})'.format(i+1,lucky[i]),result[i])#4桁分取り出して書式で右詰。足りない桁はアスタリスクを使う。配列をprintで渡す。第２引数に渡す。向きを変えれば><できる。ここは調べながらやる。場合の処理。覚えない。
        


