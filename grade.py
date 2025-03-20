"""
Write a program that asks for a student's score (out of 100) and prints their grade:

If the score is 90 or above, print "A."
If the score is 80 to 89, print "B."
If the score is 70 to 79, print "C."
If the score is 60 to 69, print "D."
If the score is below 60, print "F."

"""
sco = int(input("Enter grade : "))
if sco >=90:
    print("A")
elif sco >=80 and sco <=89:
    print("B")
elif sco >=70 and sco <=79:
    print("C")
elif sco >=60 and sco <=69:
    print("D")
else:
    print("F")
"""
    Enter grade : 80
B
PS D:\all 
Enter grade : 70
C
PS D:\all 
Enter grade : 79
C
PS D:\all .py"
Enter grade : 69
D
PS D:\all "
Enter grade : 59
F
"""