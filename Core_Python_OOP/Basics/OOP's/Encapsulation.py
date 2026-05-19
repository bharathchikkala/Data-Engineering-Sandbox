#Understanding Encapsulation, like it mainly for to protect data which is inside the class

class Bank:

    def __init__(self):
        self.__balance = 2000

    def show_balance(self):
        print(self.__balance)

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,withdrawn_amount):
        self.__balance -= withdrawn_amount


bank_obj = Bank()

bank_obj.show_balance()
bank_obj.deposit(amount=1500)
bank_obj.show_balance()
bank_obj.withdraw(withdrawn_amount=1000)
bank_obj.balance = 0
bank_obj.show_balance()
