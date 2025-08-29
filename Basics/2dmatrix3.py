rows=int(input())
col=int(input())

matrix=[]

for _ in range(rows):
    row=[]

    for _ in range(col):
        val=int(input())
        row.append(val)

    matrix.append(row)


for row in matrix:
    print(row)

matrix2=[[0 for _ in range(col)] for _ in range(rows)]



for i in range(rows):

    for j in range(col):
        if i==j:
            matrix2[i][j]=matrix[i][j]
        else:
            matrix2[j][i]=matrix[i][j]

print("Transpose matrix=")

for row in matrix2:
    print(row)