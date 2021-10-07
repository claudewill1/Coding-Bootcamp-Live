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
    # making a withdrawal from the account
    def make_withdrawal(self,amount):
        self.account_balance -= amount
    def display_user_balance(self): #print the user's name and account balance to the terminal
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        self = other_user
        self.account_balance += amount
        return self
        
guido = User("Guido van Rossum","guido@email.com")
monty = User("Monty Python","pythonM@python.com")
tom = User("Tom Woodward","tom@email.com")

# 3 deposits for first user
guido.make_deposit(300)
guido.make_deposit(500)
guido.make_deposit(1000)
# withdrawal for first user
guido.make_withdrawal(400)
# print user balance for first user
guido.display_user_balance()


# second user with two deposits and two withdrawals
monty.make_deposit(400)
monty.make_deposit(500)
monty.make_withdrawal(300)
monty.make_withdrawal(500)
# display second user balance
monty.display_user_balance()

# make 1 deposit and 3 withdrawals for third user
tom.make_deposit(1000)
tom.make_withdrawal(300)
tom.make_withdrawal(300)
tom.make_withdrawal(300)
# display third user balance
tom.display_user_balance()

# transfer funds from first user to third user
guido.transfer_money(tom,200)
# print both users account balances
guido.display_user_balance()
tom.display_user_balance()