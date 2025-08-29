number=int(input("Enter the number :"))
divisors=[]
for i in range(1,number+1):
    if number%i==0:
        divisors.append(i)
print("The divisors of ",number,"are :",divisors)