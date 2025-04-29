#inheritence -> is a relation
#composition -> has a relation
class Engine:
    def __init__(self) :
        pass
    def start(self) :
        return "Engine started"
    
class Driver:
    def __init__(self):
        pass


# car has a engine
class Car:
    def __init__(self) :
        self.engine = Engine()
        slef.driver = Driver()
        
    def start(self):
        self.engine.start()
        
        