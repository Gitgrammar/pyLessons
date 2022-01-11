def eat(breakfast,lunch,dinner='curry',*desserts):
    print('朝は{}を食べました。'.format(breakfast))
    print('昼は{}を食べました。'.format(lunch))
    print('夜は{}をたべました。'.format(dinner))
    for d in desserts:
        print('おやつに{}をたべました。'.format(d))

eat('toast','pasta','curry','ice','choco','curry')
