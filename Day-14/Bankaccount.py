class BankAccount:
    interest_rate = 5

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show(self):
        print(self.name, self.balance, self.interest_rate)

a = BankAccount("Ayush",1000000000)
b = BankAccount("Ashish",1000000)

a.show()
b.show()

a.balance = 1000000000000
a.show()

BankAccount.interest_rate = 10

a.show()
b.show()

a.interest_rate = 15
a.show()