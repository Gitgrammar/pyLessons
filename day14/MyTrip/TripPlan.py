import random
import turtle
import time 
def setup():
		startline=150#画面の
		screen=turtle.Screen()#screenが現れる
		screen.setup(1290,720)#画面窓縦が７２０ｐｘ
		screen.bgpic('map_kanto.gif')#指定その大きさの背景

def turtle_move():
		
		t=turtle.Turtle()
		t.color('black')
		t.speed(1)
		t.penup()
		t.goto(140,-65)
		t.write('東京出発',font=('Arial Black',15,'normal'))
		t.pendown()#次動いた時線を描画
		t.shape('classic')
		t.goto(380,-65)#銚子
		t.write('さんま🐟食べる',font=('Arial Black',25,'normal'))

		t.goto(300,55)#水戸へ
		t.write('            納豆食べる',font=('Arial Black',25,'normal'))
		t.goto(145,130)#日光へ
		t.write('       🙈🙊🙉を見る!',font=('impact',45,'normal'))

		t.goto(30,-10)#軽井沢へ
		t.write('  涼む',font=('impact',25,'normal'))

		t.goto(30,-160)#箱根へ
		t.write('温泉で温まる!',font=('Arial Black',17,'normal'))

		t.goto(120,-140)#鎌倉へ
		t.write('    大仏を見る!',font=('Arial Black',17,'normal'))

		t.goto(140,-110)#横浜へ
		t.write('        餃子を食べる!',font=('Arial Black',17,'normal'))

		t.goto(150,-65)#東京へ
		t.write('　　  　戻って来て疲れる!',font=('Arial Black',15,'normal'))
		t.penup()#描くの終わり
		
setup()
turtle_move()
turtle.mainloop()
