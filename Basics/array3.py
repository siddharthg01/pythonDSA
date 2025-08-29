mylist=list(map(int,input("Enter array elements").split()))

for i in range(len(mylist)):
    for j in range(len(mylist)-i-1):
        if mylist[j]>mylist[j+1]:
            temp=mylist[j]
            mylist[j]=mylist[j+1]
            mylist[j+1]=temp

print(mylist)
n=len(mylist)
print(n)
print("min=",mylist[0])

print("max=",mylist[n-1])

