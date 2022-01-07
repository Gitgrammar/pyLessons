count =0
time_sche=int(input('時間数を入力>>'))
temp_list=list()
for count<len(time_sche):
    count+=1
    temp=int(input('{}時の天気を入力>>'.format(count)))
    temp_list.append(temp)
print(temp_list)
