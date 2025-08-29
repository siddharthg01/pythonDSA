arr=list(map(int,input("Enter the array:").split(",")))

n=len(arr)

for i in range(1,n):
    if arr[i]>=arr[i-1]:
        print()
    else:
        print(0)
        break


    

    