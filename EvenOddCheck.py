# Function Defenition
def odd_even(num):
    result = num % 2
    if (result == 0):
        print("%d is even!" %(num))
    else:
        print("%d is odd!" %(num))

# Function Call
num = int(input("Enter a number: "))
odd_even(num)
