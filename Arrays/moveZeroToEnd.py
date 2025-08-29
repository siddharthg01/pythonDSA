def zero(arr):
    n=len(arr)

    j=-1
    for i in range(n):
        if arr[i]==0:
            j=i
            break
    if j==-1:
        return arr
    for i in range(j+1,n):
        if arr[i]!=0:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            j+=1

    return arr


arr=list(map(int,input("Enter the array:").split(" ")))

print(zero(arr))