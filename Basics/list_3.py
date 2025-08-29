#finding the largest number fromm a list
list=[]
while True:
    i=int(input("Enter the numbers:"))
    if i==0:
        break
    else:
        list.append(i)
print(list)
large=list[0]
for i in list:
    if i>large:
        large=i
print("Largest is:",large)