def sorted(arr,indx):
    if indx==len(arr)-1:
        return "True"
    if arr[indx]<arr[indx+1]:
        return sorted(arr,indx+1)

    else:
        return "False"
    
arr=[1,2,9,3,4,5,6]
i=0
print(sorted(arr,i))