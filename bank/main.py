from account import Account
from atm import ATM

accounts = []
exit = 0
logout = 0

def login():
    print("Welcome to Bank!")
    print("[1] Login\n[2] Register\n[3] Exit")
    choice = int(input("Enter: "))

    if choice == 1:
        number = int(input("Enter account number: "))
        pin = int(input("Enter pin: "))
        if not accounts: #checks if empty array
            print("No accounts registered.")
        else:
            array_length = len(accounts) # sets array_length to the # of indexes of accounts

            for i in range(array_length):
                if number == accounts[i].number:
                    if accounts[i].pin == pin:
                        atm = ATM(accounts[i])
                        print("Successfully Logged in", number)
                        return atm
                    else:
                        print("Invalid account number/pin")
                        return None
                else:
                    print("Invalid account number/pin")
                    return None
                    
    elif choice == 2: # Register
        acc = Account() # Initialize
        accounts.append(acc) # Append to account array
        atm = ATM(acc)
        return atm

    elif choice == 3:
        quit()

while exit == 0:
    atm = None
    logout = 0
    while atm is None:
        atm = login()

    while logout == 0:
        logout  = atm.main_menu()