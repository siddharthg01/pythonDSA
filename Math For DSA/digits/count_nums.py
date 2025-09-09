#Count number of digits


n=int(input("Ente the digit to count:"))

count=0

while n>0:
    n=int(n/10)
    count+=1
    
print(f"Length of the digit is:{count}")