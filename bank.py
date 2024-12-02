# bank project
class bankaccount:
    def __init__(self,name):
        self.name=name
        self.balance=0
        #self.statement=
    def withdraw(self,amount):
        if amount>self.balance:-jbn 
            print("insufficient balance")
        else:
            self.balance=self.balance-amount
            print(self.balance)        
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(self.balance)
    def get_balance(self):
        print(self.balance)

name=(input("enter your name:"))

def main():

    account=bankaccount(name)
    print("1 for get balance")
    print("2 for withdraw")
    print("3 for deposit")
    en=int(input("enter any number(1-3)"))
    if en==1:
        account.get_balance()
    elif en==2:
        amount=int(input("enter amount to withdaw "))
        account.withdraw(amount)    
    elif en==3:
        amount=int(input("enter amount to deposit"))
        account.deposit(amount)
main()        

print("1 for withdraw")
x=int(input("enter 1 for withdraw"))

if x==1:
    main()

