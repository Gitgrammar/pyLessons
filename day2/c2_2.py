members=["工藤","松田","浅香"]
print(members)
print(members[0])
print(len(members))
members.append("山田")
print(members)
members[3]="山崎"
print(members)
members.remove("山崎")
print(members)#できない。
del members[0]
print(members)

nums=[10,20,30]
print(sum(nums))#60答え

print(sum(nums)/len(nums)) #平均は２０

