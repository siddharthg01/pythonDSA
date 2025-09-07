def consecutiveone(arr):
    max=0
    curr_max=0

    n=len(arr)

    for i in range(n):
        if arr[i]==1:
            curr_max+=1
            if curr_max>max:
                max=curr_max

        else:
            curr_max=0

    return max

arr=list(map(int,input("Enter the array of 0's and 1's").split(" ")))
print(consecutiveone(arr))
