class BankAccount:
    def _init_(self, initial_balance=0):
        self._account_balance = initial_balance

    #Depositing method
    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            

    #Withdrawal method
    def withdraw(self, amount):
        if amount > 0 and self._account_balance >= amount:
            self._account_balance -= amount
            return True # Withdrawal succesful
        elif amount > self._account_balance:
            return False # Withdrawal failed
        
    def display_balance(self):
        print(f"Current_Balance: {self._account_balance}") 
        