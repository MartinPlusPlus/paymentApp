from user import User

bank = User("bank")
john = User("john")

bank.bal = 1000

bank.pay(john, 100)
print("John now has", john.bal, "dollars")