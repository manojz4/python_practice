'''Ask the user to enter a number.
First, check if the number is positive, negative, or zero.
If positive, check if it's even or odd.
'''
num = int(input("enter number : "))
if num > 0:
    print("number is positive")
    
    if num % 2 == 0:
        print(f"Also the number {num} is even ")
    else:
        print("number is odd")
elif num < 0:
    print("number is negative")
else:
    print("number is zero")

'''
enter number : -9
number is negative
PS D:\all 
enter number : 12
number is positive
number is even
PS D:\all 
enter number : 14
number is positive
Also the number14 is even
PS D:\all python 
enter number : 18
number is positive
Also the number 18 is even
enter number : 17
number is positive
number is odd
'''