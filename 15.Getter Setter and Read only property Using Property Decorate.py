# read only --> you can not set the value. value can not be changed
# getter --> get a value of a property through a method. Most of the time, you will get the value of a private attribute
# setter --> set a value of a property through a method. most of the time, you will set the value of a private property

class User:
    def __init__(self, name, age, money):
        self.name = name
        self._age = age
        self.__money = money
        
    # getter without any setter is reandomly attrinute
    @property
    def age(self):
        return self._age
    
    #getter
    @property
    def salary(self):
        return self.__money
    
    # setter
    @salary.setter
    def salary(self, value):
        if value < 0:
            return 'not negative'
        self.__money += value

samsu = User('kopa', 21, 120000) 
print(samsu.age)
print(samsu.salary)
samsu.salary = 4900
print(samsu.salary)