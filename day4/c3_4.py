name=input("あなたの名前")
print("{}さんこんにちは".format(name))
food =input("{}さんの好きな食べ物を教えてください・".format(name))
if'カレー' in food:
    print('素敵ですね。カレーは最高ですよ。')
else:
    print('渡しも{}が好きですよ'.format(food))


n=10
if n in[5,10,15]:
    print('ok')
else:
    print('ng')

key='red'
if key in {'red':'赤','bleu':'青'}:
    print('ok')
else:
    print('ng')
