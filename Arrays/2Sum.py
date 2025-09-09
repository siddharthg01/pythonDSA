def two_sum(arr,target):
    arr_Sort=sorted(arr)
    
    start=0
    end=len(arr)-1
    sum=0
    for i in range(len(arr)):
        sum=arr_Sort[start]+arr_Sort[end]
        
        if sum==target:
            return arr_Sort[start],arr_Sort[end]
        elif start>end:
            break
        elif sum>target:
            end-=1
            
        else:
            start+=1
    return "No two sum"        
arr=list(map(int,input("Enter array").split(" ")))
target=int(input("Enter the target sum:"))

print(two_sum(arr,target))