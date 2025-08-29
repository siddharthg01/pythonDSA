#mystr=input("Enter some string to check whether it is palindrome or not: ")

#print("Reverse of the string u entered is:",mystr[::-1])
#if mystr==mystr[::-1]:
 #   print("Yes the string you entered is palindrome")

#else:
 #   print("Not palindrome")


mystr=input("Enter some string to check whether it is palindrome or not: ")

rev=""
n=len(mystr)
for i in range(n):
    rev += mystr[n-i-1]

print("Reverse of the string u entered is:",rev)
if rev==mystr:
    print("Palindrome")

else:
    print("Not palindrome")