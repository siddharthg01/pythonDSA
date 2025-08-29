""" def subset(arr,k):
    res=[]
    def ksum(i,currset,sum):
        if i==len(arr):
            if sum==k: #Condition satisfied
                res.append(currset[:])
                return True
            #If condition not satisfied
            return False
        currset.append(arr[i])
        sum+=arr[i]
        if(ksum(i+1,currset,sum)==True):
            return True
        
        sum-=arr[i]
        currset.pop()
        if(ksum(i+1,currset,sum)==True):
            return True
        return False
    ksum(0,[],0)
    print(res)


arr=[1,2,1]
subset(arr,3) """
#----------To count the number of subsequences--------
def subset(arr,k):
    def ksum(i,currset,sum):
        if i==len(arr):
            if sum==k: #Condition satisfied
                return 1
            #If condition not satisfied
            return 0
        currset.append(arr[i])
        sum+=arr[i]
        left=ksum(i+1,currset,sum)
        
        sum-=arr[i]
        currset.pop()
        right=ksum(i+1,currset,sum)
        return left+right
    return ksum(0,[],0)
    

arr=[1,2,1]
print(subset(arr,3))