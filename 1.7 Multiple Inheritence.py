class Family:
    def __init__(self,address) :
         self.address = address

class School:
     def __init__(self,id,level):
          self.id=id
          self.level=level


class Sports:
     def __init__(self,game) :
          self.game=game


# Multiple Inheritence
class Student(Family,School,Sports) :
     def __init__(self, address,id,level,game):
          School.__init__(self,id,level)  
          Sports.__init__(self,game)   
          Family.__init__(self,address)   



          # Hybrid -> Multiple Inheritence + Multi-level Inheritence
