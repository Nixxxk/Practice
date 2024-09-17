class Account:
    def __init__(self, account_no, balance):
        self.acoount_no=account_no
        self.balance=balance


    #debit method
    def debit(self,ammount):
        self.balance-=ammount
        print(f"Debited ammount is {ammount}")
        print(f"total balance =", self.final_balance())

    #credit method
    def credit(self, ammount):
        self.balance+=ammount
        print(f"Credited ammount is {ammount}")
        print(f"total balance =", self.final_balance())


    #final balance returns here 
    def final_balance(self):
        return self.balance

account1=Account(98751,25000)
account2=Account(21254,30000)
account2.debit(5000)
account2.credit(90025)
account1.credit(21548)
account1.debit(12541)
#print(account2.balance, account2.acoount_no)