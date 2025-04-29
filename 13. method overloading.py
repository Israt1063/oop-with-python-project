class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        
    def eat(self):
        print('val dal mangso')
    
class Cricketer(Person):
    def __init__(self, name, age, height, weight, team):
        self.team = team
        super().__init__(name, age, height, weight)

    #overload
    def __add__(self,other):
         return self.age + other.weight
        
    def __mul__(self,other):
        return self.weight * other.weight
        
    def __gt__(self,other):
        return self.age > other.age
        
    def __len__(self):
        return self.height
        

saraf = Cricketer('saraf', 22, 65, 67,'BD')
anjum = Cricketer('anjum', 22, 65, 67,'BD')
print(saraf + anjum)
print(saraf * anjum)
print(len(saraf))
print(saraf > anjum)