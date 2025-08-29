def dnf(arr):
    mid=0
    high=len(arr)-1
    low=0
    
    while mid<=high:
        if arr[mid]==0:
            temp=arr[low]
            arr[low]=arr[mid]
            arr[mid]=temp
            mid+=1
            low+=1

        elif arr[mid]==1:
            mid+=1

        else:
            temp=arr[mid]
            arr[mid]=arr[high]
            arr[high]=temp
            high-=1

    print(arr)

arr=list(map(int,input("Enter the array consisting of 0's 1's and 2's:").split()))
dnf(arr)
help(dnf)