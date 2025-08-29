#removing the duplicates from the list
mylist=[1,2,1,2,3,4,3,4,5,6,5,6]
new=[]
print("Duplicates in the list are:")
for element in mylist:
    if element not in new:
        new.append(element)
print(new)

