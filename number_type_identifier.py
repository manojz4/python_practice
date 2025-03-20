num = int(input("enter the number : "))
if num %2 == 0 and num %4 == 0:
    print("The number is divisible by 4")
elif num %2 == 0 and num %4 != 0:
    print("The number is even")
else:
    print("The number is odd")