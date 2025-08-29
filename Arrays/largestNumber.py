#Optimal Solution
arr = list(map(int,input("Enter the array:").split(",")))

if len(arr)<2:
    print("Arrays must have atleast 2 elements")

else:
    largest=largest2=float('-inf')

    for num in arr:
        if num>largest:
            largest2 = largest
            largest=num

        elif num>largest2 and num!=largest:
            largest2=num

    if largest2 == float('-inf'):
        print("there is no second largest element")

    else:
        print(f"Largest={largest}, 2nd-Largest={largest2}")
