class Account:
    def __init__(self,name,balance = 50):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("Insufficient Balance")
            return False
        
    def get_balance(self):
        return self.balance




































































