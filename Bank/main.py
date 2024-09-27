class BankAccount: #your bank account
    def __init__(self, account_number, balance=0): #this is to define your bank account number
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount): #this is when you put money in
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount): #this is when you take money out
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):  #this is your balance
        return self.balance

def create_account():
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_number, initial_balance)

def main(): #your main code, this is for doing things with/making your account
    accounts = {}
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1': #this is for creating your account
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!")
        
        elif choice in ['2', '3', '4']: #you have this code
         # because you don't have a new bank account every time, 
         # so you have one assigned that you can use
            account_number = input("Enter account number: ")
            if account_number in accounts:
                account = accounts[account_number]
                if choice == '2': #this is depositing
                    amount = float(input("Enter deposit amount: "))
                    if account.deposit(amount):
                        print(f"Deposited ${amount:.2f} successfully!")
                    else:
                        print("Invalid deposit amount.")
                elif choice == '3':
                    amount = float(input("Enter withdrawal amount: ")) #this is for withdrawling
                    if account.withdraw(amount):
                        print(f"Withdrawn ${amount:.2f} successfully!")
                    else:
                        print("Invalid withdrawal amount or insufficient funds.")
                else:
                    print(f"Current balance: ${account.get_balance():.2f}") #this is to check your balance
            else:
                print("Account not found.") #this is if you don't have an 
                #account and used a random number
        
        elif choice == '5':
            print("Thank you for using our banking system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.") #this is if you don't press any numbers 1-5

if __name__ == "__main__":
    main()