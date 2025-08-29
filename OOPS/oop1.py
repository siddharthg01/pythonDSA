""" class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def avg(self):
        sum=0
        n=len(self.marks)
        for i in self.marks:
            sum+=i
        print("The avg of stud is:",sum/n)



name=input("Enter student name:")
marks=list(map(int,input("Enter the marks of three subjects:").split()))
s1=Student(name,marks)
print(s1.avg()) """
    

class Student:
    def __init__(self,p,m,c):
        self.p=p
        self.m=m
        self.c=c

    @property
    def percnt(self):
        return str((self.p+self.m+self.c)/3)+"%"
    
s1=Student(90,90,90)
print(s1.percnt)

s1.p=93
print(s1.percnt)