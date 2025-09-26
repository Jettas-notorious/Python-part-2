class Account:
    accounts_created=2
    def __init__(self,balance):
        self.balance=balance
        print("Youre current balance is R",self.balance)

    def deposit(self,amount):
        self.amount=amount
        self.balance+=self.amount
        print("You have deposited R",self.amount)
        return self.balance
    
    def withdraw(self,amount_draw):
        self.amount_draw=amount_draw
        if self.amount_draw>self.balance:
            print("Insuffisient funds,try again")
        else:
            self.balance-=amount_draw
            print("You have succesfully withdrawn R",self.amount_draw)
        return self.balance
    
    def balance_amount(self):
        print("You're current available funds is R",self.balance)

obj1=Account(50000)
obj1.accounts_created
obj1.deposit(1000)
obj1.withdraw(200)
obj1.balance_amount()

obj2=Account(25000)
obj2.deposit(10000)
obj2.withdraw(5000)
obj2.balance_amount()
print("There was in total",obj1.accounts_created,"accounts created")