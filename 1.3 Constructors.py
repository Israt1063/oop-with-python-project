class phone :
    manufactured='Japan'
    #Constructors
    def __init__(self,owner,name,price) :
        self.owner = owner
        self.name = name
        self.price = price

my_phone = phone('ami','redmi','17000')
print(my_phone.manufactured)
print(my_phone.owner,my_phone.name,my_phone.price)

her_phone = phone('she','iphone','17000')
print(her_phone.owner,her_phone.name,her_phone.price)
        