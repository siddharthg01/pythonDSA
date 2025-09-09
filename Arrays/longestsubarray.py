#Longest subarray(contigous part) with sum k(only positives in array)

arr=[1,2,3]
k=3
maxLen=0
n=len(arr)
start=0
end=0
longestsubarray=[]
for i in range(n):
    for j in range(i,n):
        s=0
        for l in range(i,j+1):
            s+=arr[l]
        currLen=j-i+1
        if s==k and currLen>maxLen:
            maxLen=currLen
            longestsubarray=arr[i:j+1]
            
print("Lenght",maxLen)  
print(f"Subarray{longestsubarray}")              



        