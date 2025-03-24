num = int(input("Enter Number : "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both")
elif num % 3== 0:
    print("Divisible by 3")
elif num % 5== 0: 
    print("divisible by 5 ")
else:
    print("Not divisible by 3 or 5")