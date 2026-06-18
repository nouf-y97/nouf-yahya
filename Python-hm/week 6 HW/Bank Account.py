# Home Work:  Bank Account
# -----------------------
# Create a class called `BankAccount` with two attributes:
#     - owner  (the account holder's name)
#     - balance
 
# Add THREE methods:
#     deposit(amount)   →  add to balance, print new balance
#     withdraw(amount)  →  subtract from balance, print new balance
#     show()            →  print "<owner> has <balance> SAR"
 
# Then in your main code:
#     - Create:    a = BankAccount("Sara", 1000)
#     - Deposit:   a.deposit(500)
#     - Withdraw:  a.withdraw(300)
#     - Show:      a.show()


class BankAccount:
   
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show(self):
        print(f"{self.owner} has {self.balance} SAR")

a = BankAccount("Sara", 1000)
a.deposit(500)
a.withdraw(300)
a.show()
 