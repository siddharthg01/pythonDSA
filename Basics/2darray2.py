r=int(input())
m=int(input())

matrix1=[]
matrix2=[]

n=1
while n!=3:
    print(f"Enter the elements of matrix{n}")
    if n==1:
        matrix1

    elif n==2:
        matrix2
    for i in range(r):
        row=[]
        for j in range(m):
            val=int(input())
            row.append(val)
        
        if n==1:
            matrix1.append(row)

        elif n==2:
            matrix2.append(row)

    n=n+1


for row in matrix1:
    print(row)

print("/t")

for row in matrix2:
    print(row)



