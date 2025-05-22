from admin import Admin
from bus_system import BusSystem

bus_system = BusSystem()
admin = Admin()

def admin_menu():
    while True:
        print("\t*** Admin Menu ***")   # Admin Menu (after successful login)
        print("1. Add Bus")
        print("2. View All Buses")
        print("3. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            number = input("Enter Bus Number: ")
            route = input("Enter Bus Route: ")
            try:
                seats = int(input("Enter Total Seats: "))
                bus_system.add_bus(number, route, seats)
            except ValueError:                                 # Input Validation & User Feedback
                print("Please enter a valid number for seats.")
        elif choice == "2":
            bus_system.show_buses()
        elif choice == "3":
            print("Logging out from Admin...")
            break
        else:
            print("Invalid choice. Try again.")


while True:
    print("\t***Bangladesh Bus Ticket Booking System***")    # User Menu
    print("1. Admin Login")
    print("2. Book Ticket")
    print("3. View Buses")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        if admin.login(username, password):
            print("Admin Login Successful!")
            admin_menu()
        else:
            print("Incorrect Admin Credentials.")
    elif choice == "2":
        bus_number = input("Enter Bus Number you want to book: ")
        name = input("Enter Your Name: ")
        phone = input("Enter Your Phone Number: ")
        bus_system.book_ticket(bus_number, name, phone)
    elif choice == "3":
        bus_system.show_buses()
    elif choice == "4":
        print("Thank you for using the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

