x = int(input("Please Enter an Integer: "))
for i in range(2,x//2):
    if x%i==0:
        print(f"{x} is not Prime.")
        break
else:
    print(f"{x} is Prime.")