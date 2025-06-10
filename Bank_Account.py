class BankAccount:
    def _init_(self, acc_no, holder, balance=0):
        self.__accountNumber = acc_no
        self.__accountHolder = holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            self.__balance = "Insufficient funds"

    def get_balance(self):
        return self.__balance
    def display(self):
        print("Account number: ",self._accountNumber,"account holder name:",self._accountHolder)
    

ac = BankAccount("12345", "madhu", 1000)
ac.display()
print("balance:",ac.get_balance())

ac.deposit(500)
ac.withdraw(200)
print("Balance:", ac.get_balance())