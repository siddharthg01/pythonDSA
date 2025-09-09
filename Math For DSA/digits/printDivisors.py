import math

def divisors(num):
    
    for i in range(1,num+1):
        if num%i==0:
            print(i,end=" ")
            
    print()
#Optimal
def optimalDivisors(num):
    sq=int(math.sqrt(num))
    for i in range(1,sq+1):
        if num%i==0:
            print(i,end=" ")
            
            if (n/i)!=i:
                r=int(n/i)
                print(r,end=" ") 
                
    print()  
n=int(input("Enter number:"))
print("Normal way=")
divisors(n)
print("Optimal way=")
optimalDivisors(n)