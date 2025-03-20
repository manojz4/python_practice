side1 =int(input("enter :"))
side2 =int(input("enter :"))
side3 =int(input("enter :"))

if side1+side2 > side3:
    print("it is valid triangle")

if side2+side3 > side1:
    print("it is valid triangle")

if side3+side1 > side2:
    print("it is valid triangle")


#if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
#    print("it is valid triangle")