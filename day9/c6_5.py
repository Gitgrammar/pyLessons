class Hero:
    def __init__(self,name,hp=100):
        self.name=name
        self.hp=hp
    def sleep(self, hours):
        print('{}は{}時間寝た!'.format(self.name, hours))
        self.hp+= hours

#ゲーム開始
print('スッキリファンタジー１金色の理想郷')
h=Hero('松田',100)
h1=Hero('鈴木')
print('鈴木'.format(h1))
h.sleep(3)
print('{}のHPは現在{}です。'.format(h.name, h.hp))
