class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number  
        self.balance = balance 

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def get_balance(self):
        return self.balance


class Bank:
    def __init__(self):
        self.accounts = {}  
    
    def create_account(self, account_number, account_holder, initial_deposit=0):
        if account_number in self.accounts:
            print("Account number already exists.")
        else:
            new_account = Account(account_number, account_holder, initial_deposit)
            self.accounts[account_number] = new_account
            print(f"Account created successfully for {account_holder}. Initial deposit: {initial_deposit}.")

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account not found.")
            return None

    def deposit_to_account(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            account.deposit(amount)

    def withdraw_from_account(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            account.withdraw(amount)

    def display_account_info(self, account_number):
        account = self.get_account(account_number)
        if account:
            print(account)


if __name__ == "__main__":
    bank = Bank()
    
    bank.create_account(101, "Atish Sharma", 500)
    bank.create_account(102, "Arushi Sharma", 1000)
    
    bank.deposit_to_account(101, 200)  
    bank.deposit_to_account(102, 500) 
    
    bank.withdraw_from_account(101, 100)  
    bank.withdraw_from_account(102, 1500)  
    
