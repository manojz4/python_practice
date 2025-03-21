'''Temperature condition:
Ask the user to enter the temperature.
If it's above 30 degrees, print "Hot day." If it's below 30 but greater than 20, print "Warm day."
For temperatures below 20 but greater than 10, print "Cool day." Otherwise, print "Cold day."'''


tem = int(input("enter temperature : "))
if tem > 30:
    print("Hot Day")
elif 20<= tem <30:
        print("warm day")
elif 10<= tem <20:
    print("cool day")
else:
    print("cold day")


'''
    enter temperature : 55
Hot Day
PS D:\
enter temperature : 5
cold day
PS D:\
enter temperature : 24
cold day
PS D:
cool day
PS D:\
enter temperature : 24
warm day
'''