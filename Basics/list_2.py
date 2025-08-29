#sum and avg of list elements
sum=0
list1=[]
while True:
    user_input=int(input("Enter the list elements:"))
    if user_input==0:
        break
    else:
        list1.append(user_input)
print(list1)
for i in list1 :
    sum += i
avg=sum/len(list1)
print(sum)
print(avg)