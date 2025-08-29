def rzcz(arr):
    row=len(arr)
    col=len(arr[0])

    row_zero=False
    cols_zero=False

    for i in range(col):
        if arr[0][i]==0:

            row_zero=True

    for j in range(row):
        if arr[j][0]==0:
            cols_zero=True


    for i in range(1,row):
        for j in range(1,col):
            if arr[i][j]==0:
                arr[0][j]=0
                arr[i][0]=0


    for i in range(1,row):
        for j in range(1,col):
            if arr[0][j]==0 or arr[i][0]==0:
                arr[i][j]=0
    
    if row_zero:
        for i in range(row):
            arr[0][i]=0

    if cols_zero:
        for j in range(col):
            arr[j][0]=0


    print(arr)

n=int(input())
m=int(input())
arr=[]
for i in range(n):
    temparr=[]
    for j in range(m):
        n=int(input(f"[{i}][{j}]:"))
        temparr.append(n)
    arr.append(temparr)

rzcz(arr)

    
