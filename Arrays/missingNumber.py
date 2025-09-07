#Better solution

def missingNum(arr):
    n=len(arr)
    hash=[0]*(n+1)

    for num in arr:
        if num<=n:
            hash[num]=1

    for i in range(1,n+1):
        if hash[i]==0:
            return i
        
    return "No missing number"
#optimal solution
#Note: a(xor)a=0
def missingNumOptimum(arr):
    size=len(arr)
    N=arr[size-1]
    n=N-1
    xor1=0
    xor2=0
    for i in range(n):
        xor2=xor2^arr[i]
        xor1=xor1^(i+1)
    xor1=xor1^N
    return xor1^xor2

arr=list(map(int,input("Enter the array:").split(" ")))

print("Better solution:",missingNum(arr))
print("Optimum solution:",missingNumOptimum(arr))

