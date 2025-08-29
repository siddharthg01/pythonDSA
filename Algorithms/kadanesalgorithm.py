import sys

def kadaneAlgo(arr):
    maxsum= -sys.maxsize-1
    tempstart= 0
    start= 0
    end= 0
    currsum= 0
    n= len(arr)

    for i in range(n):

        currsum += arr[i]
        if currsum>maxsum:
            maxsum= currsum
            start = tempstart
            end= i

        if currsum<0:
            currsum=0
            tempstart=i+1

    return maxsum, arr[start:end+1]


n = int(input("Enter the size of the array:"))

arr = list(map(int,input("Enter the array elements:").split(",")))

print(kadaneAlgo(arr))