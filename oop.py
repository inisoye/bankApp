# -------ATTEMPT 1--------
# Basic up to generation of of account number

# import random


# class User():

#     def __init__(self, name, age, email, phone):
#         self.name = name
#         self.age = age
#         self.email = email
#         self.phone = phone


# class Account(User):

#     #Class Attributes
#     balance = 0
#     accountNumber = ""

#     def __init__(self, name, age, email, phone):
#         super().__init__(name, age, email, phone) # Initialize attributes from parent class
#         self.balance = 0
#         self.accountNumber = self.generateAccountNumber()

#     def generateAccountNumber(self):
#         accountNumber = random.randint(3000000000, 3999999999)
#         return str(accountNumber)


# -------ATTEMPT 2--------

# import random


# class User():

#     def __init__(self, name, age, email, phone):
#         self.name = name
#         self.age = age
#         self.email = email
#         self.phone = phone


# class Account(User):

#     # Class Attributes
#     balance = 0
#     accountNumber = ""

#     def __init__(self, name, age, email, phone):
#         # Initialize attributes from parent class
#         super().__init__(name, age, email, phone)
#         self.balance = 0
#         self.accountNumber = self.generateAccountNumber()

#     def generateAccountNumber(self):
#         accountNumber = random.randint(3000000000, 3999999999)
#         return str(accountNumber)

#     # Default values make function parameters optional. The code will still run without them--hence the empty strings
#     def deposit(self, amount, comment=""):
#         self.balance += amount  # Add deposit value to balance
#         self.storeTransaction("credit", amount, comment)
#         print(
#             f"Welldone {self.name} your deposit of ₦{amount} was sucessful. Your new balance is ₦{self.balance}.")

#     def withdraw(self, amount, comment=""):
#         self.balance -= amount  # Remove withdrawal value from balance
#         self.storeTransaction("debit", amount, comment)
#         print(
#             f"Welldone {self.name} your deposit of ₦{amount} was sucessful. Your new balance is ₦{self.balance}.")

#     def transfer(self, amount, recipient, comment=""):
#         self.balance -= amount  # Remove transfer value from sender's balance
#         recipient.balance += amount  # Add transfer value to recipient's balance
#         self.storeTransaction("transfer", amount, comment)
#         print(
#             f"Congrats {self.name} your transfer of ₦{amount} to {recipient.name} was sucessful. Your new balance is ₦{self.balance}.")

#     def storeTransaction(self, type,  amount, comment, recipient="To No One"):
#         file = open("financial-statement.csv", "a")
#         file.write(f"{type}, {self.name}, {amount}, {comment}, {recipient}\n")
#         print(type, amount, comment, recipient)


# ini = Account("Ini", 23, "inisoye@gmail.com", "07089559879")
# print(ini.accountNumber)
# ini.deposit(20000)
# ini.withdraw(3000)

# ayo = Account("ayo", 23, "ayosoye@gmail.com", "07089559879")
# ini.transfer(2000, ayo, "flexing")


# -------ATTEMPT 3--------

import random


class User():

    def __init__(self, name, age, email, phone):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone


class Account(User):

    # Class Attributes
    balance = 0
    accountNumber = ""

    def __init__(self, name, age, email, phone):
        # Initialize attributes from parent class
        super().__init__(name, age, email, phone)
        self.balance = 0
        self.accountNumber = self.generateAccountNumber()

    def generateAccountNumber(self):
        accountNumber = random.randint(3000000000, 3999999999)
        return str(accountNumber)

    # Default values make function parameters optional. The code will still run without them--hence the empty strings
    # Source is empty (false) because money is assumed to be a personal deposit by default.
    def deposit(self, amount, comment="", source=""):
        transactionLabel = "credit"

        if source:
            transactionType = "transfer"
            source = source.name
        else:
            transactionType = "deposit"
            source = self.name

        self.balance += amount  # Add deposit value to balance
        self.storeTransaction(
            transactionType, transactionLabel, amount, self.name, source, comment)
        print(
            f"Welldone {self.name} your deposit of ₦{amount} was sucessful. Your new balance is ₦{self.balance}.")

    def withdraw(self, amount, comment="", collector=""):
        transactionLabel = "debit"

        if collector:
            transactionType = "transfer"
            collector = collector.name
        else:
            transactionType = "withdrawal"
            collector = self.name

        self.balance += amount  # Add deposit value to balance
        self.storeTransaction(
            transactionType, transactionLabel, amount, self.name, collector, comment)
        print(
            f"Welldone {self.name} your deposit of ₦{amount} was sucessful. Your new balance is ₦{self.balance}.")

    def transfer(self, amount, recipient, comment=""):
        # Remove transfer value from sender's balance
        self.withdraw(amount, comment, recipient)
        recipient.deposit(amount, comment, self)  # Add transfer value to recipient's balance

        print(
            f"Congrats {self.name} your transfer of ₦{amount} to {recipient.name} was sucessful. Your new balance is ₦{self.balance}.")

    def storeTransaction(self, transactionType, transactionLabel,  amount, source, comment, recipient="To No One"):
        file=open("financial-statement.csv", "a")
        file.write(
            f"{transactionType}, {transactionLabel}, {amount}, {source}, {comment}, {recipient}\n")
        print(transactionType, amount, comment, recipient)


ini=Account("Ini", 23, "inisoye@gmail.com", "07089559879")
print(ini.accountNumber)
ini.deposit(20000)
ini.withdraw(3000)

ayo=Account("Ayo", 23, "ayosoye@gmail.com", "07089559879")
ini.transfer(2000, ayo, "flexing")
