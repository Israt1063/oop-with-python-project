class Person:
    def __init__(self,name,age,height,weight) :
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('vat dal vorta')


class Cricketer(Person):
    def __init__(self, name, age, height, weight,team):
        self.team = team
        super().__init__(name, age, height, weight)


    #overirde
        def eat(self):
            print('vegetables')


mahbub = Cricketer('mahbub',22,65,67,'BD')
mahbub.eat()