def vote(arr):
    count=0
    ele:int
    n=len(arr)
    m=n/2
    for i in range(len(arr)):
        if count==0:
            count+=1
            ele=arr[i]

        elif arr[i]==ele:
            count+=1

        else:
            count-=1

    count1=0

    for i in range(len(arr)):
        if arr[i]==ele:
            count1+=1

    if count1>m:
        return ele

    else:
        return -1
    
arr=list(map(int,input("Enter the array:").split()))

print("The majority element is:",vote(arr))