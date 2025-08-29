#difference between two list
list1=[1,2,3,4,5]
list2=[1,2,3,4,5]
list3=[list1+list2]
print(list3)

#reversing the elements in list
list=[]
list1=[]
while True:
    j=int(input("Enter the numbers:"))
    if j==0:
        break
    else:
        list.append(j)
print(list1)
for i in range(1,len(list)+1):
    list1.append(list[-i])
    
print(list1)