rows=int(input("Enter the num of rows:"))

col=int(input("Enter the num of columns:"))


matrix=[]

for i in range(rows):
    row=[]
    for j in range(col):
        val=int(input(f"Enter the values of [{i}][{j}]"))
        row.append(val)

    matrix.append(row)

print("2D Matrix u entered is:")
for row in matrix:
    print(row)

print(matrix.length)