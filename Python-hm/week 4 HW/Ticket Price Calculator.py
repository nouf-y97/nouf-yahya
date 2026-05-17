# Problem 5: Ticket Price Calculator
# -----------------------------------
# A cinema charges tickets based on age and day:
#   - Age below 12         -> 20 SAR
#   - Age 12 to 17         -> 35 SAR
#   - Age 18 to 59         -> 50 SAR
#   - Age 60 or above      -> 25 SAR
# Additionally, on "Tuesday", every ticket gets a 10 SAR discount
# (minimum price must not go below 10 SAR).
# Ask the user for age and day, then print the final ticket price.
# Constraint: NO logical operators. Use nested conditions.

#######################################################################

age = int(input("Please enter your age: "))
day = input("Please enter a day: ").lower()
days = ('sunday' , 'monday' , 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'saturday')

if day not in days:
     print("Please enter a valid day")
else:
    if age < 12:
        ticket = 20
        if day == 'tuesday':
            ticket -= 10
            if ticket < 10:
                print("minimum price must not go below 10 SAR")
            else:
                print(f"{ticket} SAR")
    elif 12 <= age <= 17:
            ticket = 35
            if day == 'tuesday':
                ticket -= 10
            if ticket < 10:
                 print("minimum price must not go below 10 SAR")
            else:
                print(f"{ticket} SAR")                
    elif 18 <= age <= 59:
            ticket = 50
            if day == 'tuesday':
                ticket -= 10
            if ticket < 10:
                 print("minimum price must not go below 10 SAR")
            else:
                print(f"{ticket} SAR")
    else:
        ticket = 25
        if day == 'tuesday':
            ticket -= 10
            if ticket < 10:
                 print("minimum price must not go below 10 SAR")
            else:
                print(f"{ticket} SAR")


