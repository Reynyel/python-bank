from account import Account

class ATM:
    account = None

    def __init__(self, account):
        self.account = account

    
    def main_menu(self):
        print("[1] Deposit\n[2] Withdraw\n[3] Balance Inquiry\n[4] Logout")
        choice = int(input("Enter: "))

        if choice == 1: # Deposit
            value = int(input("Enter amount to deposit: "))
            self.account.deposit(value)
            return 0
        
        elif choice == 2: # Withdraw
            value = int(input("Enter amount to withdraw: "))
            self.account.withdraw(value)
            return 0
        
        elif choice == 3: # Check balance
            self.account.balance_inquiry()
            return 0
        
        elif choice == 4: #Logout
            account = None
            return -1
        
        else:
            print("Invalid Input")
            return 0