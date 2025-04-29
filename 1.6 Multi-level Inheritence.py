class Vehicle:
    def __init__(self,name,price) :
        self.name=name
        self.price=price

    def move(self):
        return f'Moving Car'
    
    def __repr__(self) :
        return f'{self.name}{self.price}'
    
# Multi-level Inheritence
class Bus(Vehicle):
    def __init__(self, name, price,seat):
        self.seat=seat
        super().__init__(name, price)

    def __repr__(self):
        return super().__repr__()
    

class Truck(Vehicle):
    def __init__(self, name, price,weight):
        self.weight=weight
        super().__init__(name, price)

    def __repr__(self):
        return super().__repr__()
    

class PickUpTruck(Truck):
    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)

    def __repr__(self):
        return super().__repr__()
    

class AcBus(Bus):
    def __init__(self, name, price, seat,temp):
        self.ac = temp
        super().__init__(name, price, seat)

    def __repr__(self):
        print(f'{self.seat}')
        return super().__repr__()
    


green_line = AcBus('green',50000000,22,18)
print(green_line)
        
    