def mergeSort(arr,low,high):
    if(low>=high):
        return
    
    mid=(low+high)//2

    mergeSort(arr,low,mid)
    mergeSort(arr,mid+1,high)

    return merge(arr,low,mid,high)

def merge(arr,l,m,h):
    temp=[]
    left=l
    right=m+1
    while left<=m and right<=h:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1

        else:
            temp.append(arr[right])
            right+=1

    while left<=m:
        temp.append(arr[left])
        left+=1
    while right<=h:
        temp.append(arr[right])
        right+=1

    for i in range(l,h+1):
        arr[i]=temp[i-l]

    return arr

arr=[3,2,4,1,3]
n=len(arr)
mergeSort(arr,0,n-1)

print(arr)