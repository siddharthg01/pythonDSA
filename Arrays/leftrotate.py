

def leftrotate(arr,d):
    n=len(arr)
    d=d%n
    
    return arr[d:]+arr[:d]

def leftrotateGeneral(arr,d):
    n=len(arr)
    d=d%n

    temp=[]
    temp.extend(arr[0:d])

    for i in range(d,n):
        arr[i-d]=arr[i]
    j=0
    for i in range(n-d,n):
        arr[i]=temp[j]
        j+=1

    return arr

arr=list(map(int,input("Enter the array to left rotate:").split(" ")))
d=int(input("Enter how many positions you need to rotate:"))
print("Python Logic:")
print(leftrotate(arr,d))

print("General programming logic:")
print(leftrotateGeneral(arr,d))

