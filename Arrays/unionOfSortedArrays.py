#brute force approach

""" def union(arr1,arr2):
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

print(f"Union of array1 and array2 is:{union(arr1,arr2)}") """

#Optimal solution
#2pointer approach

def union(arr1, arr2):
    n1=len(arr1)
    n2=len(arr2)

    i=0
    j=0
    union_arr=[]

    while(i<n1 and j<n2):
        if arr1[i]<=arr2[j]:
            if len(union_arr)==0 or union_arr[-1]!=arr1[i]:
                union_arr.append(arr1[i])

            i+=1

        else:
            if len(union_arr)==0 or union_arr[-1]!=arr2[j]:
                union_arr.append(arr2[j])

            j+=1
            


    while j<n2:
        if len(union_arr)==0 or union_arr[-1]!=arr2[j]:
            union_arr.append(arr2[j])

        j+=1
    
    while i<n1:
        if len(union_arr)==0 or union_arr[-1]!=arr1[i]:
            union_arr.append(arr1[i])

        i+=1

    return union_arr


arr1=list(map(int,input("Enter the array1:").split(" ")))
arr2=list(map(int,input("Enter the array2:").split(" ")))

print(union(arr1,arr2))