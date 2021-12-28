scores={'network':60,'database':80,'security':50}

key =input('追加する科目名を入力して下さい。')
if key in scores:
    print('もうあるよ。')
else:
    data=int(input('得点を入力してください。'))
    scores[key]=data
print(scores)
