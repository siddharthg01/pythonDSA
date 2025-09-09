n=int(input("Enter the num of rows:"))
space=2*n-2
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    
    for k in range(space):
        print(" ",end="")
    space-=2
        
    for l in range(i,0,-1):
        print(l,end="")
        
    print()