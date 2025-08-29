import sys
def kadane(arr):
    start=0
    end=0
    maxsum=-sys.maxsize-1
    currsum=0
    tempstart=0

    for i in range(len(arr)):
        currsum+=arr[i]
        if currsum>maxsum:
            maxsum=currsum
            start=tempstart
            end=i

        if currsum<0:
            currsum=0
            tempstart=i+1

    return maxsum,start,end

def dkadane(arr):
    n=len(arr)
    m=len(arr[0])
    currsum=0
    maxsum=-sys.maxsize-1
    finalBottom=0
    ft=0
    fr=0
    fl=0

    for left in range(m):
        temp=[0]*n

        for right in range(left,m):
            for i in range(n):
                temp[i]+=arr[i][right]

            currsum,temptop,tempbottom=kadane(temp)

            if currsum>maxsum:
                maxsum=currsum
                ft=temptop
                finalBottom=tempbottom
                fr=right
                fl=left



    print("Maxsum=",maxsum)

    print("The sub array which produced max sum is:")
    
    for i in range(ft,finalBottom+1):
        print(arr[i][fl:fr+1])
    
          
n=int(input("Enter num of rows:"))
m=int(input("Enter num of cols:"))
array=[]
for i in range(n):
    temparr=[0]*m
    for j in range(m):
        n=int(input(f"Enter ele [{i}][{j}]"))
        temparr.append(n)

    array.append(temparr)

dkadane(array)

