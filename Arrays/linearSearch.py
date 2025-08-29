def linearSearch(arr,search):
    n=len(arr)

    for i in range(n):
        if arr[i]==search:
            return i
    return -1

arr=list(map(int,input("Enter the elements of array:").split(" ")))
search=int(input("Enter the element to search:"))
print(f"The element u searched has found in position:{linearSearch(arr,search)}")