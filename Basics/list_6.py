#wap to check if the given key is present in the list , if yes ,print its position
list=[]
while True:
    inp=int(input("Enter the numbers:"))
    if inp==0:
        break
    else:
        list.append(inp)
print(list)
key=int(input("Enter the key to search:"))
for num in list:
    if(key==num):
        print("yes")
        pos=list.index(key)
        break
print(pos)
