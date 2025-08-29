def solve(givennums,target):
    givennums.sort()
    start=0
    end=len(givennums)-1

    while start<end:
        currsum=givennums[start]+givennums[end]
        if currsum==target:
            return start,end
        if currsum>target:
            end-=1
        else:
            start+=1

    return -1
arr=list(map(int,input("Enter the numbers:").split()))
tar=int(input("Enter the target sum:"))

n,m=solve(arr,tar)

print("Sum found in :",arr[n],arr[m])