x = float(input("Please Enter Your Score: "))
if 18 <= x <= 20:
    print("You Got an A.")
elif 16 <= x <= 18:
    print("You Got a B.")
elif 14 <= x <= 16:
    print("You Got a C.")
elif 12 <= x <= 14:
    print("You Got a D.")
elif 10 <= x <= 12:
    print("You Got an E.")
elif 0 <= x <= 10:
    print("You Failed.")
else:
    print("Your Score is not in the correct internal.")
