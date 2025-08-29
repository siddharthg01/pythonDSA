def dnf(arr):
    count0=0
    count1=0
    count2=0

    for i in range(len(arr)):
        if arr[i]==0:
            count0+=1
        if arr[i]==1:

            count1+=1

        if arr[i]==2:
            count2+=1
    for i in range(0,count0):
        arr[i]=0
    for i in range(count0,count0+count1):
        arr[i]=1
    for i in range((count0+count1),(count0+count1+count2)):
        arr[i]=2

    print(arr)

arr=list(map(int,input("Enter the array containing 0's, 1's, 2's:").split()))
dnf(arr)
        