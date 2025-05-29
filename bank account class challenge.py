class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        balance = self.balance
        if amount <= balance:
            self.balance -= amount
        else:
            print("insufficient balance")

    def show_balance(self):
        print(self.balance)


a1 = Account("justine", 0)

a1.deposit(200)
a1.withdraw(100)
a1.show_balance()