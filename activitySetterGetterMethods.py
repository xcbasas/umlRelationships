class BankAccount:
    def __init__(self,account_number,balance):
        self._account_number = account_number
        self._balance = balance

    @property
    def account_number(self):
        print("Account Number:  ", self._account_number)

    @property
    def balance(self):
        print(f"Account Balance:  {self._balance:.2f}")

    @account_number.setter
    def account_number(self,new_number):
        self._account_number = new_number

    @balance.setter
    def balance(self,new_balance):
        print(f"Update balance to {new_balance}")
        if new_balance >= 0:
            self._balance = new_balance
        else:
            print("Balance must not be negative")

a1 = BankAccount(12345,1000)
print("Account 1")
a1.account_number
a1.balance

print("")
a1.balance = -100
a1.account_number
a1.balance