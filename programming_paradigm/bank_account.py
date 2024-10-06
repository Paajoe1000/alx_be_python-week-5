class BankAccount:
    def _init_(self, account_balance=0):
        self._account_balance = account_balance

    #Depositing method
    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposit: ${amount: .2f}. New balance: ${self._account_balance}")
        else:
            print("Please enter a valid amount")

    #Withdrawal method
    def withdraw(self, amount):
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return True # Withdrawal succesful
        elif amount > self._account_balance:
            print("You don't have sufficient funds.")
            return False # Withdrawal failed
        else:
            print("Something went wrong!")
            return False # Withdrawal failed
    def display_balance(self):
        print(f"Your balance is ${self._account_balance: 2f}") 
        