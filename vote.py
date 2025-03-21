#Ask for the user's age.
#If the user is 18 or older, check if they are between 18 and 19 to 
#identify if they are still a teenager.


age = int(input("enter your age : "))
if age >= 18:
    print("you are 18 and above")
    if 18<= age <20:
        print("you are still as teenager")
else:
    print("you are underage")

''' enter your age : 17
you are underage
PS D:\all python 
enter your age : 25
you are 18 and above
PS D:\all python 
enter your age : 19
you are 18 and above
you are still as teenager
PS D:\a
enter your age : 18
you are 18 and above
you are still as teenager
PS D:\all 
enter your age : 20
you are 18 and above   '
'''