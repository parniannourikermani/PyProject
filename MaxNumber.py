# Function Definition
def print_maximum(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        result = num1
    elif num2> num1 and num2 > num3:
        result = num2
    else:
        result = num3

    print("Maximum number between %d, %d and %d is %d" %(num1, num2, num3, result))


# Function Call
num1 = int(input("Please Enter Number 1: "))
num2 = int(input("Please Enter Number 2: "))
num3 = int(input("Please Enter Number 3: "))

print_maximum(num1, num2, num3)






# Another Way
num1 = int(input("Please Enter Number 1:"))
num2 = int(Input("PLease Enter Number 2: "))
num3 = int(input("Please Enter Number 3: "))

result = max(num1, num2, num3)
print("Maximum number between %d, %d, and %d id %d" %(num1, num2, num3, result))
