from abc import ABC
from Orders import Order

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item quantity exceeded!!")
            else:
                item.quantity = quantity
                self.cart.add_item(item, quantity)  # Assuming add_item method takes item and quantity
                print('Item added!!')
        else:
            print('Item not found!!!')

    def view_cart(self):
        print('\t***view cart***')
        print('Name\tPrice\tQuantity')
        # Assuming cart.items is a list of tuples (item, quantity)
        for item, quantity in self.cart.items:  # Iterate directly over cart items
            print(f'{item.name}\t{item.price}\t{quantity}')
        
        print(f"Total price: {self.cart.total_price}")

    def pay_bill(self):
        print(f'Total {self.cart.total_price} paid successfully')
        self.cart.clear()


class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
             
    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)
        
    def view_employee(self, restaurant):
        restaurant.view_employee()
        
    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)
    
    def remove_item(self, restaurant, item):
        restaurant.menu.remove_item(item)
        
    def view_menu(self, restaurant):
        restaurant.menu.show_menu()


# Assuming an example of the Order class:
class Order:
    def __init__(self):
        self.items = []  # List to store tuples of (item, quantity)
        self.total_price = 0

    def add_item(self, item, quantity):
        self.items.append((item, quantity))
        self.total_price += item.price * quantity

    def clear(self):
        self.items = []
        self.total_price = 0
