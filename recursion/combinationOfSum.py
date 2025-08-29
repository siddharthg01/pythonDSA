def combination(arr,target):
    res=[]

    def backtrack(i,target,currset):
        if i==len(arr):
            if target==0:
                res.append(currset[:])

            return

        if(arr[i]<=target):
            currset.append(arr[i])
            backtrack(i,target-arr[i],currset)
            currset.pop()

        backtrack(i+1,target,currset)

    backtrack(0,target,[])
    return res

arr=[2,3,6,7]
t=7
print(combination(arr,t))

    