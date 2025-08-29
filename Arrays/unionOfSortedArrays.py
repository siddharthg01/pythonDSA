def union(arr1,arr2):
    n=len(arr1)
    m=len(arr2)

    s=set()

    for i in range(n):
        s.add(arr1[i])

    for j in range(m):
        s.add(arr2[i])
    

    unionof2=list(s)

    return unionof2

arr1=[1,1,2,3,4,5]
arr2=[2,3,4,4,5,6]

print(f"Union of array1 and array2 is:{union(arr1,arr2)}")
