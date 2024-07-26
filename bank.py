from account import Account

class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, name, initial_deposit):
        if name not in self.accounts:
            if initial_deposit >= 50:
                self.accounts[name] = Account(name, initial_deposit)
                print("Account Created Successfully")
            else:
                print("Initial deposit must not be 0")
        else:
            print("Account with that name already exists!")
    

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name].deposit(amount)
            print("Deposit Successful")
        else:
            print("Account not found")
    
    def withdraw(self, name, amount):
        if name in self.accounts:
            if self.accounts[name].withdraw(amount):
                print("Withdrawal successful.")
        else:
            print("Account not found")
    

    def check_balance(self, name):
        if name in self.accounts:
            balance = self.accounts[name].get_balance()
            print(f"Account Balance: {balance}")
        else:
            print("Account not found")
    
    
    










