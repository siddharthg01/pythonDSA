""" def search(arr, key):
    for i in range(len(arr)):
        if arr[i]==key:
            print("Found at location:",i)
            return
    print("Not found")
    return

arr=[1,5,7,9,5,3,4,2,6,8,0,1,25]
search(arr,25) """
""" res=[]
def search(arr,ele,i):
    if i==len(arr):
        return res.append("Not found");
        
    if arr[i]==ele:
        res.append(i)
    
    search(arr,ele,i+1)


arr=[1,5,7,9,5,3,4,2,6,8,0,1,25]
i=0
search(arr,9,i)
print(res) """

def returnarr(arr):
    return arr

arr=[1,2,3]
print(returnarr(arr))