class ATM:
    def __init__(self, pin):
        self.pin = pin          # store the ATM pin
        self.__balance = 0      # private balance variable

    # deposit money if PIN matches
    def deposit(self, amount, pin):
        if pin == self.pin:     # check if entered pin is correct
            self.__balance += amount
            print("Deposited =", amount)
        else:
            print("Invalid PIN")

    # withdraw money if PIN matches and balance is enough
    def withdraw(self, amount, pin):
        if pin == self.pin:     # check pin
            if self.__balance >= amount:   # check balance
                self.__balance -= amount
                print("Withdrawn =", amount)
            else:
                print("Insufficient balance")
        else:
            print("Invalid PIN")

    # check balance if PIN matches
    def check_balance(self, pin):
        if pin == self.pin:
            print("Balance =", self.__balance)
        else:
            print("Invalid PIN")


#               Main Program 
user_pin = int(input("Enter your 4-digit ATM pin to enable the facilities = "))

# create ATM object with user's pin
aryan = ATM(user_pin)

# Perform operations
aryan.deposit(1000, user_pin)    # deposit 1000
aryan.withdraw(400, user_pin)    # withdraw 400
aryan.deposit(1400, user_pin)    # deposit 1400
aryan.check_balance(user_pin)    # check balance
