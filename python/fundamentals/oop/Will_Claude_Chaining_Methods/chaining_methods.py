class User:
    # declaring class attribute
    bank_name = "Dojo National Bank"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self,amount): #takes an argument that is the amount
    #of the deposit
        self.account_balance += amount
        return self
    # making a withdrawal from the account
    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self): #print the user's name and account balance to the terminal
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        self = other_user
        self.account_balance += amount
        return self
        
guido = User("Guido van Rossum","guido@email.com")
monty = User("Monty Python","pythonM@python.com")
tom = User("Tom Woodward","tom@email.com")

guido.make_deposit(500).make_deposit(500).make_deposit(300).make_withdrawal(300).display_user_balance()

monty.make_deposit(400).make_deposit(500).make_withdrawal(300).make_withdrawal(500).display_user_balance()

# make 1 deposit and 3 withdrawals for third user
tom.make_deposit(1000).make_withdrawal(300).make_withdrawal(300).make_withdrawal(300).display_user_balance()