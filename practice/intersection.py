def intersection(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)

    i=0
    j=0
    inter=[]
    while i<n1 and j<n2:
        if arr1[i]<arr2[j]:
            i+=1

        elif arr2[j]<arr1[i]:
            j+=1

        else:
            inter.append(arr1[i])
            i+=1
            j+=1
    return inter


arr1=list(map(int,input("Enter the array 1:").split(" ")))
arr2=list(map(int,input("Enter the array 2:").split(" ")))

print(intersection(arr1,arr2))