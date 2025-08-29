mylist=list(map(int,input("Enter initial array eles:").split()))


print(mylist)
summ=0
for i in range(len(mylist)):
    summ += mylist[i]

print(summ)

