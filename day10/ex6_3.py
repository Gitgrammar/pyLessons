def welcome(u):
    print('ようこそ{}'.format(u['name']))
    u['age']=u['age']+1
    print('あなたは来年{}歳だから大吉です。!'.format(u['age']))

username=input('名前を入力してください>>')
userage=int(input('年齢を入力してください>>'))
user ={'name':username,'age':userage}
copied_user=user.copy()
welcome(copied_user)
print('{}歳の{}さんまたプレイしてくださいね'.format(user['age'],user['name']))

