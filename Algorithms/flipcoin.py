def countzero(char):
    if char=="0":
        return 1
    
    else:
        return -1


def kadanesalgo(arr):
    start=0
    currsum=0
    maxsum=0
    end=0
    tempstart=0
    n=len(arr)
    ans=0
    for i in range(n):
        if arr[i]=="1":
            ans +=1
    for i in range(n):
        currsum+=countzero(arr[i])
        if currsum>maxsum:
            maxsum=currsum
            start=tempstart
            end=i

        if(currsum<0):
            currsum=0
            tempstart=i+1
            
    return maxsum+ans, arr[start:end+1]

arr=input()

print("Maximum sum=",kadanesalgo(arr))