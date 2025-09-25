Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
             print("Insufficient balance or invalid amount.")
    def check_balance(self):
         print(f"Account Holder: {self.account_holder}, Balance: ₹{self.balance}")

         
# Creating accounts
acc1 = BankAccount("Naveen", 5000)
acc2 = BankAccount("Rahul")
acc1.deposit(2000)
₹2000 deposited successfully.
acc1.withdraw(3000)
₹3000 withdrawn successfully.
acc1.check_balance()
Account Holder: Naveen, Balance: ₹4000
acc2.deposit(1000)
₹1000 deposited successfully.
acc2.check_balance()
Account Holder: Rahul, Balance: ₹1000
### Add Inheritance (CurrentAccount & SavingsAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of ₹{interest} added. New balance: ₹{self.balance}")
class CurrentAccount(BankAccount):
    
SyntaxError: invalid syntax
class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=5000):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit
    def  withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully (Overdraft allowed).")
        else:
            print("Overdraft limit exceeded.")

            
# Savings account
s_acc = SavingsAccount("Naveen", 10000)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s_acc = SavingsAccount("Naveen", 10000)
NameError: name 'SavingsAccount' is not defined
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

        
s_acc = SavingsAccount("Naveen", 10000)
s_acc.add_interest()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s_acc.add_interest()
AttributeError: 'SavingsAccount' object has no attribute 'add_interest'
# Creating accounts
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.05):
...         super().__init__(account_holder, balance)
...         self.interest_rate = interest_rate
...     def add_interest(self):
...         interest = self.balance * self.interest_rate
...         self.balance += interest
...         print(f"Interest of ₹{interest} added. New balance: ₹{self.balance}")
... 
>>> class CurrentAccount(BankAccount):
...     def __init__(self, account_holder, balance=0, overdraft_limit=5000):
...         super().__init__(account_holder, balance)
...         self.overdraft_limit = overdraft_limit
...     def withdraw(self, amount):
...         if amount <= self.balance + self.overdraft_limit:
...             self.balance -= amount
...             print(f"₹{amount} withdrawn successfully (Overdraft allowed).")
...         else:
...             print("Overdraft limit exceeded.")
... 
...             
>>> s_acc = SavingsAccount("Naveen", 10000)
>>> s_acc.add_interest()
Interest of ₹500.0 added. New balance: ₹10500.0
>>> s_acc.check_balance()
Account Holder: Naveen, Balance: ₹10500.0
>>> c_acc = CurrentAccount("Rahul", 2000)
>>> c_acc.withdraw(6000)  # overdraft allowed
₹6000 withdrawn successfully (Overdraft allowed).
>>> c_acc.check_balance()
Account Holder: Rahul, Balance: ₹-4000
