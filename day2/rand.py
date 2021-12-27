import random
#ランダムを利用するにはimportが必要
n=random.randint(1,6)
#randint(最大最小含む)
print(n)
name=input("あなたの犬の名前は?")
age =input ("あなたの犬の年齢は？")
age=int(age)
print('{}人間換算で{}歳です'.format(name,age))
