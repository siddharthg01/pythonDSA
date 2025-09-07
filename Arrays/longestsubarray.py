#Longest subarray(contigous part) with sum k(only positives in array)

arr=[1,2,3]
subarry=[]
n=len(arr)
for i in range(n):
    for j in range(i,n):
        sub=[]
        for k in range(i,j+1):
            sub.append(arr[k])

        subarry.append(sub)

print(subarry)