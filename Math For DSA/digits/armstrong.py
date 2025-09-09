def armstrong(num):
    
    N=num
    
    digit=0
    
    while N>0:
        digit+=((N%10)**3)
        N=int(N/10)
        
    if num==digit:
        print(digit)
        print("Yes the number u entered is armstrong number")
    else:
        print(digit)
        print("No its not")        

        
n=int(input("Enter the number to check whether it is armstrong or not:"))

armstrong(n)
