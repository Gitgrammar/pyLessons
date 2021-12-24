a=[10,20,30,40,50]
print(a[1:3:])
print(a[2:])
print(a[:3])

print(a[-1])
print(a[-2])

print(a[-3:])

#範囲以外でもエラーにならない。
print(a[0:100])
#print(a[100]) エラー

#リストのコピー作成
b=a[:]
x=[100,200,300]
y=x
x[0]=500
print(y[0])

a=[1,2,3,4,5,6,7,8,9]
print(a[1:7:2])
print(a[5:2:-1])
print(a[ ::-1])
#文字列でも同様
s="Hello World"
s2=s[1:5]
print(s2)#ello
print(s[::-1])#dlrow olleH
print(s[-1])#d
