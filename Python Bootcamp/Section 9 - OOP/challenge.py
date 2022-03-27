class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account Owner: {self.owner}\nAccount balance: ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"You have deposited ${amount}. Your total balance is now {self.balance}."

    def withdraw(self, amount):
        if amount > self.balance:
            return f"The amount that you withdrew exceeds your total balance."
        else:
            self.balance -= amount
            return f"You have withdrew {amount}. Your total balance is now {self.balance}"


acct1 = Account('Jose', 100)
acct1.withdraw(500)
print(acct1)
print(acct1.owner)
print(acct1.balance)
print(acct1.deposit(50))
print(acct1.withdraw(75))
print(acct1.withdraw(500))
