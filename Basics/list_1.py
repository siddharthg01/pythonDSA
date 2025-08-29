#taking the user input
list=[]
while True:
    name=input("Enter the name:")
    if name.lower =='done':
        break
    else:
        list.append(name)
print(list)    
    
