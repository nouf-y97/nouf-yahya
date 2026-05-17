# Problem 3: Triangle Type
# ------------------------
# Ask the user for the three sides of a triangle (a, b, c). Print:
#   - "Equilateral" if all three sides are equal.
#   - "Isosceles"   if exactly two sides are equal.
#   - "Scalene"     if no sides are equal.
# Constraint: NO logical operators. Use nested if-else.

############################################################

side1 = float(input("Please enter the first side: "))
side2 = float(input("Please enter the second side: "))
side3 = float(input("Please enter the third side: "))

if side1 == side2 == side3:
    print("Equilateral")
else:
    if side1 == side2:
        print("Isosceles")
    else:
        if side1 == side3:
            print("Isosceles")
        else:
            if side3 == side2:
                print("Isosceles")
            else:
                print("Scalene")
