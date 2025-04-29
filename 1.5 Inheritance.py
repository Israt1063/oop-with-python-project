# base class, parent class,common attribute + functionality class
class Gadget :
    def __init__(self,brand,price,color,origin) :
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'Runnning laptop:{self.brand}'
    

#derived class, child class, uncommon attribute + functionality class
class Phone(Gadget):
    def __init__(self, brand, price, color, origin,dual_sim):
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)
       
    def phone_call(self,number,text):
        return f'Sending SMS to:{number} with:{text}'
    
    def __repr__(self) :
        return f'phone:{self.brand} {self.price} {self.dual_sim}'
    

#inheritence
my_phone = Phone('iphone',120000,'silver','uk',True)
print(my_phone)
print(my_phone.brand)