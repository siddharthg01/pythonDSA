def subset(arr):
    res=[]
    count=0
    def backtrack(i,currset):
        nonlocal count
        if i==len(arr):
            res.append(currset[:])
            count+=1
            return
        currset.append(arr[i])
        backtrack(i+1,currset)  #take
        currset.pop()
        backtrack(i+1,currset)  #Not take

    backtrack(0,[])
    print(count)
    return res

arr=[1,2,3,4,5,6,7,8,9,10]
print(subset(arr))