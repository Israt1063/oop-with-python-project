class Book:
    def __init__(self,name) :
        self.name = name

        def read(self):
            pass

        def sleep(self):
            raise NotImplementedError
        

class Physics(Book):
    def __init__(self, name,lab):
        self.lab = lab
        super().__init__(name)
    
    def sleep(self):
        print('Ira is sleeping')

Ira = Physics('Ira',True)

print(issubclass(Physics,Book))   #True
print(isinstance(Ira,Physics))    #True
print(isinstance(Ira,Book))       #True

#Ira.read()    #Does nothing
Ira.sleep()   #print : Ira is sleeping