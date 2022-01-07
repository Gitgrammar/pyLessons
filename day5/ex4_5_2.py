temp =list()
for n in range(10):
    data=float(input('{}個目のデータを入力>>'.format(n+1)))
    temp.append(data)
for count in range(len(temp)):
    print('{}時 {}度'.format(count+8,temp[count]))
