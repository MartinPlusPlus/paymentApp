import random

class User:
    def __init__(self, name):
        self.name = name
        self.bal = 0

    # usr is a User object and amnt is an integer
    def pay(self, usr, amnt):
        if self.bal >= amnt:
            self.bal -= amnt
            usr.amnt += amnt
        else:
            print("You do not have sufficient funds...\n")

    # usr is a User object and amnt is an integer
    def request(self, usr, amnt):
        pass