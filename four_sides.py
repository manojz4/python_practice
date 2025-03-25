# Taking four numbers as input from the user
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))
side4 = float(input("Enter the length of the fourth side: "))

# Check if the four numbers can form a valid quadrilateral
if (side1 + side2 + side3 > side4 and
    side1 + side2 + side4 > side3 and
    side1 + side3 + side4 > side2 and
    side2 + side3 + side4 > side1):
    
    # Nested if to classify the type of quadrilateral
    if side1 == side2 == side3 == side4:
        print("The quadrilateral is a Square.")
    elif (side1 == side3 and side2 == side4) or (side1 == side2 and side3 == side4):
        print("The quadrilateral is a Rectangle.")
    else:
        print("The quadrilateral is an Other Quadrilateral.")
else:
    print("The entered sides do not form a valid quadrilateral.")
