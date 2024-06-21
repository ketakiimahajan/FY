class Account:
    def __init__(self, name, account_number, account_type):
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful.\nUpdated balance: ", self.balance)
    
    def display_balance(self):
        print(f"Account balance: {self.balance}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal successful.\nUpdated balance: ", self.balance)
        else:
            print("Insufficient balance.\nWithdrawal failed. ")
    
    def compute_interest(self, rate):
        interest = (rate / 100) * self.balance
        self.balance += interest
        print("Interest deposited.\nUpdated balance: ", self.balance)


class CurAccount(Account):
    def __init__(self, name, account_number):
        super().__init__(name, account_number, "Current Account")
    
    def check_balance(self, minimum_balance, penalty):
        if self.balance < minimum_balance:
            self.balance -= penalty
            print("Minimum balance is NOT maintained and PENALTY CHARGED. Updated balance: ", self.balance)
            
class SavAccount(Account):
    def __init__(self, name, account_number):
        super().__init__(name, account_number, "Savings Account")
    
    def check_balance(self, minimum_balance, penalty):
        if self.balance < minimum_balance:
            self.balance -= penalty
            print("Minimum balance is NOT maintained and PENALTY CHARGED. Updated balance: ", self.balance)

def createAccount(): 
    name = input("Enter customer name: ")
    account_number = input("Enter account number: ")
    account_type = input("Enter account type, either Current or Savings: ")
    
    if account_type.lower() == "current":
        return CurAccount(name, account_number)
    elif account_type.lower() == "savings":
        return SavAccount(name, account_number)
    else:
        print("INVALID account type.")
        return None

account = createAccount()
if account:
    while True:
        print("\n1. Deposit\n2. Display Balance\n3. Deposit Interest\n4. Withdraw\n5. Check Minimum Balance \n6. Exit")
        
        choice = input("Enter choice from 1 to 6: ")
        
        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == "2":
            account.display_balance()
        elif choice == "3":
            interest = float(input("Enter interest rate: ")) 
            account.compute_interest(amount)
        elif choice == "4":
            interest = float(input("Enter withdrawal amount: ")) 
            account.withdraw(amount)
        elif choice == "5":
            min_balance = float(input("Enter the minimum balance: "))
            penalty = float(input("Enter the penalty amount: "))
            account.check_balancee(min_balance, penalty)
        elif choice == "6":
            break
        else:
            print("Invalid Choice.\nEnter number from 1 to 6.")
            