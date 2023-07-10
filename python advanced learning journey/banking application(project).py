class account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = int(balance)
        self.min_balance = int(min_balance)

    def deposit(self, amount):
         self.balance += amount

    def withdrawl(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount

        else:
            print('sorry insufficient funds!!! ')


    def statment(self):
        print('the balance amount inyour account is={}'.format(self.balance))


class saving_account(account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=0)
    def __str__(self):
        return "the account holder name={}\nthe balance left inyour account is={}".format(self.name, self.balance)


class current_account(account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=-1000)
    def __str__(self):
        return "the account holder name={}\nthe balance left inyour account is={}".format(self.name,self.balance)


c1 = saving_account('saikiran',10000)
print(c1)
c1.deposit(100000)
c1.statment()
c1.withdrawl(999)
c1.withdrawl(1)
c1.statment()
print(c1)

c2 = current_account('reddy',10000)
print(c2)
c2.deposit(100000)
c2.statment()
c2.withdrawl(9999)
c2.withdrawl(11)
c1.statment()
print(c2)