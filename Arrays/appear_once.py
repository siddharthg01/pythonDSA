#Find the number that appears once in the array which contains elements twice

#Better solution algorithm

def whichnumber(arr):
    n=len(arr)
    maxsize=arr[n-1]
    hash=[0]*(maxsize+1)
    for num in arr:
        hash[num]+=1
    for i in range(maxsize+1):
        if hash[i]==1:
            return i
    return "No number appears once"

#Optimal approach





arr=list(map(int,input("Enter the elements:").split(" ")))
print("Better approach:")
print(whichnumber(arr))