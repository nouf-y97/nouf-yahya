# ################################################################
# #   PROBLEM 1: ATM SYSTEM
# ################################################################

# ----------------------------------------------------------------
# PROBLEM
# ----------------------------------------------------------------
# Build an ATM that keeps running until the user chooses to exit.
# Start with a balance of 1000 SAR.

# Show a main menu with these options:
#     1 - Show Balance
#     2 - Deposit
#     3 - Withdraw
#     0 - Exit

# Rules:
#   - The program must KEEP showing the menu after each
#     transaction.
# It only stops when the user chooses 0.

#   - Show Balance: print the current balance.
#   - Deposit: ask the user to choose an amount — 50, 100, 200,
#     or 500. Add it to the balance and show the new balance.
# The user can press 0 to cancel and go back to the menu.
# If they type an invalid amount, ask again.

#   - Withdraw: ask the user to choose an amount the same way.
# If the balance is enough, subtract it and show the new
#     balance. If not, show "Insufficient funds".
# The user can
#     press 0 to cancel. Invalid amounts ask again.
# Use loops so the application never exits until the user chooses
# 0 at each step.

balance = 1000
selection = -1
while selection != 0:
    
    selection = input("Please select one of these options: \n1 - Show Balance\n" \
    "2 - Deposit\n3 - Withdraw\n0 - Exit\nYour selection: ")
    if selection.isdigit():        
        selection = int(selection)
        if selection == 1:
            print("Your current balance is: ",balance ,"SAR")

        elif selection == 2:
            while True:
                user_choice = input("Select an amount to deposit 50, 100, 200, 500 or (0 to cancel): ")
                if user_choice.isdigit(): 
                    user_choice = int(user_choice) 

                    if user_choice == 0:
                        break

                    if user_choice not in [50 , 100, 200, 500]:  
                        print("Invalid input")     
                        continue     

                    else:
                        balance += user_choice
                        print(balance , "SAR")
                        break                   
                else:
                    print("Invalid input")
                
                          
        elif selection == 3:
            while True:
                user_choice = input("Select an amount to withdraw 50, 100, 200, 500 or (0 to cancel): ")
                if user_choice.isdigit():
                    user_choice = int(user_choice)

                    if user_choice == 0:
                        break

                    if user_choice not in [50 , 100, 200, 500]:  
                        print("Invalid input")     
                        continue  

                    if balance < user_choice:
                        print("Insufficient funds")
                        continue

                    else:
                        balance -= user_choice
                        print(balance , "SAR")
                        break

                else:
                    print("Invalid input")
                    
        elif selection == 0:
            print("Goodbye & have good day :)")

        else: 
            print("Wrong selection")

    else:
            print("Invalid input")

    













