def union(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    i=0
    j=0

    u=[]

    while i<n1 and j<n2:
        if arr1[i]<arr2[j]:
            if len(u)==0 or u[-1]!=arr1[i]:
                u.append(arr1[i])

            i+=1

        else:
            if len(u)==0 or u[-1]!=arr2[j]:
                u.append(arr2[j])

            j+=1

    while i<n1:
        if len(u)!=0 and u[-1]!=arr1[i]:
            u.append(arr1[i])
        i+=1

    while j<n2:
        if len(u)!=0 and u[-1]!=arr2[j]:
            u.append(arr2[j])
        j+=1

    return u

arr1=list(map(int,input("Enter the arr1:").split(" ")))
arr2=list(map(int,input("Enter the arr2:").split(" ")))

print(union(arr1,arr2))
    


