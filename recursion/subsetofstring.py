def subset(str):
    res=[]

    def backtrack(i,currstr):
        if i==len(str):
            res.append(currstr)
            return
        
        currstr=currstr+str[i]
        backtrack(i+1,currstr)
        currstr=currstr[:-1]
        backtrack(i+1,currstr)

    backtrack(0,"")
    return res

str="sid"
print(subset(str))