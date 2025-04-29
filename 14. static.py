#static attribute (class attribute)
#static method @staticmethod
#class method @classmethod

class Shopping:
    cart = []  #class attribute   #static attribute
    origin = 'china'

    def __init__(self,name,location) :
        self.name=name
        self.location=location  #instance attribute

    def purchase(self,item,price,amount):
        remaining = amount - price
        print(f'buying:{item} for price:{price} and remaining:{remaining}')

    @staticmethod
    def multiply(a,b):
        result = a*b
        print(result)

    @classmethod
    def view(self,item):
        print('just view',item)

    
shop = Shopping('shop','not popular')
shop.view('lungi')
Shopping.view('genzi')
Shopping.multiply(3,7)   #static method

        