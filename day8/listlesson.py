import pprint
data=list()
for i in range(10):
    temp=list()
    for j in range(10):
        temp.append(0)
    data.append(temp)
print(data)
pprint.pprint(data)
W=10
H=10
data=[None]*H
for i in range(H):
    data[i]=[0]*W
pprint.pprint(data)

data=[[0]*H]*H
pprint.pprint(data)

data[1][1]=5
pprint.pprint(data)


data=[None]*H
for i in range(10):
    i+=1
    for j in range(10):
        j+=1
pprint.pprint(data)

data=[[i*10+j for j in range(1,11)]for i in range(10)]
pprint.pprint(data)#内包

#2重
for i in range(H):
    temp=[None]*W
    for j in range(W):
        temp[j]=i*10+j+1
        data[i]=temp

pprint.pprint(data)

x=[i for i in range(1,8)]#1-7の要素
print(x)

x=[i**2 for i in range(1,8)]#2乗
print(x)

x=[i for i in range(1,8) if i %2==0]#偶数
print(x)

x=[i*10+j for i in range(1,3) for j in range(2,5)]#入れ子
print(x)

x=[[i*10+j for j in range(7,10)] for i in range(1,3)]#2次元
print(x)

row=col=3
matrix=[[1 if i==j else 0 for j in range(col)] for i in range(row)]
print(matrix)# 単位行列生成
