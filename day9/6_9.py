def add_suffix(names):
    for i in range(len(names)):
        names[i]=names[i]+'さん'
        return names

before_names =['松田','浅木','工藤']
copied_names=before_names[:]

after_names=add_suffix(before_names)
print('さんつけ後:'+after_names[0])
print('さんつけ前:'+before_names[0])
