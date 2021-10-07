class BankAccount:
    bankName = 'Dojo National Bank'
    
    def __init__(self,int_rate = 0,balance=0):
        self.int_rate = int_rate
        self.balance = balance
        

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdrawal(self, amount):
        if amount >= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Funds")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}\n{self.int_rate}% interest rate")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.int_rate/100) * self.balance
        else:
            print("This account currently does not have a positive balance. No interest added for this statement period.")
        return self
    @classmethod
    def printAllAccountInfo(cls):
        print(cls.bankName)
        for account in cls.allBankAccs:
            cls.display_account_info(account)

class User:
    def __init__(self,name,email, accounts):
        self.name = name
        self.email = email
        self.accounts = {
            'checking': BankAccount(int_rate=0, balance=0, accountType=''),
            'savings': BankAccount(int_rate=2, balance=0, accountType='')
        }

    def make_deposit(self, accountType, amount):
        self.accounts[accountType].deposit(amount)
        return self
    
    def make_withdrawal(self, accountType, amount):
        self.accounts[accountType].withdrawal(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()



bob = BankAccount("Bob Woodward",1,"checking")
bob = BankAccount("Bob Woodward",2,"savings")
tom = BankAccount("Tom Willard",2,"savings")
tom = BankAccount("Tom Willard",1,"checking")

bob.deposit('savings',300).deposit('checking',300).deposit('checking',300).withdrawal('savings',400).yield_interest().display_account_info()
tom.deposit('checking',400).deposit('savings',400).withdrawal('checking',200).withdrawal('checking',200).withdrawal('checking',200).withdrawal('savings',300).yield_interest().display_account_info()

BankAccount.printAllAccountInfo()