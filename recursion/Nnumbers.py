def numbers(n):
    if n==0:
        return 0
    

    numbers(n-1)
    print(n,end=" ")
    
    
numbers(5)