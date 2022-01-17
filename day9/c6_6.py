scores1=[80,40,50]
scores2=[80,40,50]
print('scores1のidentity: {}'.format(id(scores1)))
print('scores2のidentity: {}'.format(id(scores2)))

if scores1==scores2:
    print('scores1,scores2は同じ内容です。')
else:
    print('socres1,scores2は違う内容です。')

if id (scores1)==id(scores2):
    print('scoroes1,scores2は同じ存在です。')
else:
    print('scores1,scores2は違う存在です。')
