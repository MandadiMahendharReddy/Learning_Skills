class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # public
        self.__balance = balance  # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ₹{amount}. New balance: ₹{self.__balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ₹{amount}. Remaining balance: ₹{self.__balance}"
        return "Insufficient funds."

    def get_balance(self):
        return f"Current balance: ₹{self.__balance}"


# 🧪 Test
account = BankAccount("Mahendhar", 1000)
print(account.deposit(500))  # ✅ Safe deposit
print(account.withdraw(300))  # ✅ Safe withdrawal
print(account.get_balance())  # ✅ Access via method
#print(account.__balance)  # ❌ Will raise error: attribute is private
