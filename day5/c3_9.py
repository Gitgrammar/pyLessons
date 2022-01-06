score =int (input('試験の点数を入力してください。'))
if score<0 or score>100:
   print("以上な得点です。")
   print('入力しなおしてください')

elif score>=60:
   print('合格')
   print('よくがんばった')
else:
   print('残念ながら不合格です。')
   print("追試を受けてください。")
