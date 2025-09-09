n=int(input("Enter the number to reverse:"))

while n>0:
    print(n%10,end="")
    n=int(n/10)