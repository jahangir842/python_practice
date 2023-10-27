class BankAccount:
    def __init__(self, initial_amount, balance) -> None:
        self.initital_amount = initial_amount
        self.balance = balance
    
acount1 = BankAccount(500, 500)

print(acount1.balance)
print(acount1.initital_amount)

