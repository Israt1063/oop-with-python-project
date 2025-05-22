from bus import Bus
from passenger import Passenger

class BusSystem:
    def __init__(self):
        self.buses=[]
        self.passengers=[]

    def add_bus(self,number,route,seats):
        bus=Bus(number,route,seats)
        self.buses.append(bus)
        print(f"Bus{number} added successfully.")

    def find_bus(self,number):
        for bus in self.buses:
            if bus.number==number:
                return bus
        return None
    
    def book_ticket(self,bus_number,name,phone):
        bus=self.find_bus(bus_number)
        if bus:
            if bus.book_seat():
                passenger=Passenger(name,phone,bus)
                self.passengers.append(passenger)
                print(f"Ticket booked for{name}.Fare:500 taka")
            else:
                print("No seats available on this bus.")
        else:
            print("Bus not found.")


    def show_buses(self):
        if not self.buses:
            print("No buses available yet.")
        else:
            print("\nAvailable Buses:")
            for bus in self.buses:
                print(f"Bus Number:{bus.number},Route:{bus.route},Available Seats:{bus.available_seats()}")