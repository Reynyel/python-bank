from random import randint

class Account:
    balance = 0
    number = 0
    pin = 0
    
    def __init__(self, balance, number): #constructor
        self.number = number
        self.balance = balance


    def __init__(self):
        gen_num = [] # Stores generated pin
        for i in range(15): # Loops 15 times
            self.number = randint(1000,9999)
            self.balance = 0

            if self.number not in gen_num: # Checks if num is in list already
                gen_num.append(self.number) # If not, append

        print("Your account number is ", self.number)

        value = int(input("Enter a security pin: "))
        self.set_pin(value)


    def set_pin(self, pin):
        self.pin = pin
        print("Pin has been set.")
    
    def deposit(self, amount): #deposits amount to account
        print("Deposited ", amount)
        self.balance += amount
        print("Current balancec: ", self.balance)

    def withdraw(self, amount): #withdraw balance from account
        print("Withdrew: ", amount)
        self.balance -= amount

        print("Current balancec: ", self.balance)

    def balance_inquiry(self): #checks balance
        print("Your balance is: ", self.balance)



