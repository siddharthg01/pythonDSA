n=int(input("Enter the num of rows:"))

for i in range(n):
    #space
    for j in range(n-i-1):
        print(" ",end="")
    #star
    for k in range(2*i+1):
        print("*",end="")
    
    for j in range(n-i-1):
        print(" ",end="")
        
    print()