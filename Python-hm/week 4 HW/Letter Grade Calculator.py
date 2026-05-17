# Problem 1: Letter Grade Calculator
# ----------------------------------
# Ask the user for a score from 0 to 100 and print the letter grade:
#   - 90 to 100  -> A
#   - 80 to 89   -> B
#   - 70 to 79   -> C
#   - 60 to 69   -> D
#   - below 60   -> F
# Constraint: Do NOT use 'and'. Use the natural order of elif to
# handle the ranges.

#################################################################################

score = int(input("Please enter your score between 0 and 100: "))

if 0 <= score <=100:
    if  90 <= score <=100:
        print("A")
    elif  80 <= score <=89:
        print("B")
    elif  70 <= score <=79:
        print("C")
    elif  60 <= score <=69:
        print("D")
    else:
        print("F")
else:
    print("Please enter a valid score")


