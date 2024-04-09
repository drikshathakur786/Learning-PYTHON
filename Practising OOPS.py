# bank class represent a person
# bank class object should represent a real human and its details
# 2 things ya paise deposit kr skta hai ya withdraw

class Bank():
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.bank_name = 'HDFC'
    
    def deposit(self,money):
        self.balance = self.balance + money
        print('Money added successfully')
        else:
            print('Incorrect PIN. Deposit failed.')
    
    def withdraw(self, money):
        if self.balance >= money:
            self.balance = self.balance - money
                return money
            else:
                print('Invalid Amount')
        else:
            print('Incorrect PIN. Withdrawal failed')
        

ria = Bank('Ria',500,1234)
jia = Bank('Jia',1000,4321)


ria.deposit(1234, 2000)  
print(ria.balance, jia.balance)

ria.withdraw(1234, 1500)  
print(ria.balance, jia.balance)

ria.deposit(5678, 1000)  
print(ria.balance, jia.balance)

# Add functionality
# Whenever a person becomes object take pin too 
# Enter pin before withdrawl and deposit






