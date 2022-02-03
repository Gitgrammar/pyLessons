import random

goal=15
total_money=0
print(f'{goal}マスでゴール！資産はいくら増えるかな')
while goal>0:
    select=input('サイコロを振るy/n(nで終了)>')
    if select =='n':
        break
    dice=random.randint(1,6)
    print(f'{dice}の目がでた。{dice}マス進む')
    goal-=dice;
    money=random.randint(-5,9)*100
    if money !=0:
        if money!=0:
             print(f'ビジネスに成功!{money}万円獲得した')
        else:
             print(f'ビジネスに失敗!{money}万円損失した')
        total_money+=money
    if goal>0:
        print(f'現在資産{total_money}万円。ゴールまであと{goal}マスです。')
else:
    print(f'ゴール！総資産は{total_money}万円です。')
print("ゲーム終了")
