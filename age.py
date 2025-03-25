'''agee = int(input("Enter age to proceed : "))
if 120<= agee <0:
    print("invalid age",agee)
elif agee <18:
    print("You are minor")
    if agee >18 and agee <59:
        print("You are an adult")
    else:
        print("you are senior citizen")

        '''

agee = int(input("Enter age to proceed: "))

if agee < 0 or agee > 120:
    print("Invalid age:", agee)
elif agee < 18:
    print("You are a minor.")
elif 18 <= agee < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

