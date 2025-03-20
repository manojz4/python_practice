#Triangle Type Checker:
#Write a program that takes the lengths of three sides of a triangle and checks the type of triangle:

side1 = int(input("enter length in cm: "))
side2 = int(input("enter length in cm: "))
side3 = int(input("enter length in cm: "))

if side1 == side2 == side3:
    print("Equilateral Triangle")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("Isosceles Triangle")
else :
    print("Scalene Triangle")

'''
    
enter length in cm: 5
enter length in cm: 5
enter length in cm: 5
Equilateral Triangle


PS D:\all python projects\PracticeFolder> & "C:/Program Files/Python313/python.exe" "d:/all python projects/PracticeFolder/triangle_type_checker.py"
enter length in cm: 6
enter length in cm: 6
enter length in cm: 7
Isosceles Triangle


PS D:\all python 
enter length in cm: 4
enter length in cm: 8
enter length in cm: 9
Scalene Triangle
'''


'''Explanation:
Equilateral Triangle: All three sides are equal (side1 == side2 == side3).
Isosceles Triangle: Two sides are equal, but not all three (side1 == side2 or side2 == side3 or side1 == side3).
Scalene Triangle: No sides are equal (else case).'''