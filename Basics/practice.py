import sys
def kadane(arr):
    start=0
    end=0
    currsum=0
    tempstart=0
    maxsum=-sys.maxsize-1

    for i in range(len(arr)):
        currsum+=arr[i]

        if currsum>maxsum:
            maxsum=currsum
            start=tempstart
            end=i

        if currsum<0:
            currsum=0
            tempstart=i+1

    return maxsum, start, end
def k2d(arr):
    n=len(arr)
    m=len(arr[0])
    maxsum=-sys.maxsize-1
    for left in range(m):
        temp=[0]*n

        for right in range(left,m):
            for i in range(n):
                temp[i]+=arr[i][right]

            currsum, temptop, tempbottom=kadane(temp)

            if currsum>maxsum:
                maxsum=currsum
                top=temptop
                bottom=tempbottom
                finalright=right
                finalleft=left

    print("Maxsum is:",maxsum)

    print("The sub matrix which produced maxsum is:")

    for i in range(top,bottom+1):
        print(arr[i][finalleft:finalright+1])

arr=[]
n=int(input("Enter the number of rows"))
m=int(input("Enter the num of cols:"))

for i in range(n):
    temp=[]

    for j in range(m):
        ele=int(input(f"[{i}][{j}]:"))
        temp.append(ele)

    arr.append(temp)

k2d(arr)


