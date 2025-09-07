
#Brute fore


arr= list(map(int,input("Enter the array:").split(" ")))

sett= set()

for i in arr:
    sett.add(i)

arr1=list(sett)
print("Brute force approach:")
print(arr1)

#optimal
print("Optimal approach:")

i=0

for j in range(1,len(arr)):
    if arr[j]!=arr[i]:
        arr[i+1]=arr[j]
        i+=1

print(arr[0:i+1])