#Dutch National Flag Algorithm


def dnf(arr):
    low=0
    mid=0
    high=len(arr)-1
    
    for i in range(len(arr)):
        if arr[mid]==0:
            temp=arr[mid]
            arr[mid]=arr[low]
            arr[low]=temp
            low+=1
            mid+=1
            
        elif arr[mid]==1:
            mid+=1
            
        elif arr[mid]==2:
            temp=arr[mid]
            arr[mid]=arr[high]
            arr[high]=temp
            high-=1
            
    return arr

arr=list(map(int,input().split(" ")))

print(f"Sorted={dnf(arr)}")
            