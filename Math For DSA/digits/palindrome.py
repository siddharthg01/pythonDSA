def palindrome(num):
    rev=0
    N=num
    while N>0:
        rev=(rev*10)+(N%10)
        
        N=int(N/10)
        
    if num==rev:
        print(rev)
        print("The number u entered is palindrome")
        
    else:
        print(rev)
        print("Not a palindrome")
        
n=int(input("Enter the number to check the palindrome:"))
palindrome(n)        