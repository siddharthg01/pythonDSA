num=[1,2,3,4,5,6,7,8,9,10]
for i in num:
    for p in range(len(num)):
        if i%2==0:
             if num[p]==i:
                    num[p]='x'
                    
print(num)


    
  