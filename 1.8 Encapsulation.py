# Access Modifiers (Public,Private,Protected)
# Encapsulation -> hide details

class Bank:
    def __init__(self,holder_name,initial_deposit):
        self.holder_name=holder_name # public
        self._branch='Banani 11'  #protected
        self.__balance=initial_deposit # private

    def deposit(self,amount):
        self.__balance +=amount

    def get_balance(self):
        return self.__balance
    
    def withdraw (self,amount):
        if amount <self.__balance:
            self.__balance = self.__balance-amount
            return amount
        else:
            return f'fokir tk nai'
        

Ira = Bank('Ira',1000)
Ira.deposit(200)
print(Ira.get_balance())
print(Ira.withdraw(500))

print(Ira._Bank__balance)    #access private
        