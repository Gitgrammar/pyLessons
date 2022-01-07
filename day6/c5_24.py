def eat(breakfast,lunch='ラーメン',dinner='curry'):
    print('朝は{}を食べました。'.format(breakfast))
    print('昼は{}を食べました。'.format(lunch))
    print('夜は{}をたべました。'.format(dinner))

eat(breakfast='納豆',dinner='カレーうどん')
eat(dinner='カレーうどん',breakfast='納豆ごはん')
eat('納豆ごはん',dinner='カレーうどん')
