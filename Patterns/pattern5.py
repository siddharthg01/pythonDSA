n=int(input("Enter num:"))
for i in range(n):
    for j in range(1,n-i+1):
        print(f"{j}",end=" ")
    print("\n") 
    