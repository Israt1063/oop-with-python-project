class shop :
    #cart = []   #cart is an class attribute
    shop_name = 'jamuna'

    def __init__(self,name) :
        self.name = name
        self.cart = []    # cart is an instance attribute

    def add_to_cart(self,item):
        self.cart.append(item)


ami=shop('Ira')
ami.add_to_cart('chair')
ami.add_to_cart('phone')
print(ami.cart)

she=shop('she')
she.add_to_cart('laptop')
she.add_to_cart('watch')
print(she.cart)
        