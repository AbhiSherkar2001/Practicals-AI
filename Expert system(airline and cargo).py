Expert system(airline and cargo)
class AirlineSchedulingExpertSystem:
    def __init__(self):
        self.flights = []
        self.aircrafts = {}
        self.crew = {}

    def add_flight(self):
        flight_id = input("Enter Flight ID: ")
        aircraft = input("Enter Aircraft Model: ")
        crew_member = input("Enter Crew Member Name: ")
        departure = input("Enter Departure Time (YYYY-MM-DD HH:MM): ")
        arrival = input("Enter Arrival Time (YYYY-MM-DD HH:MM): ")

        if self.is_aircraft_available(aircraft) and self.is_crew_available(crew_member):
            self.flights.append({
                'flight_id': flight_id,
                'aircraft': aircraft,
                'crew_member': crew_member,
                'departure': departure,
                'arrival': arrival
            })
            self.aircrafts[aircraft] = "Assigned"
            self.crew[crew_member] = "Assigned"
            print(f"Flight {flight_id} scheduled successfully.\n")
        else:
            print("Error: Aircraft or Crew not available.\n")

    def is_aircraft_available(self, aircraft):
        return self.aircrafts.get(aircraft, "Available") == "Available"

    def is_crew_available(self, crew_member):
        return self.crew.get(crew_member, "Available") == "Available"

    def show_flights(self):
        if not self.flights:
            print("No flights scheduled yet.\n")
        else:
            print("\nScheduled Flights:")
            for flight in self.flights:
                print(f"Flight {flight['flight_id']} | Aircraft: {flight['aircraft']} | Crew: {flight['crew_member']} | Departure: {flight['departure']} | Arrival: {flight['arrival']}")
            print()

class CargoSchedulingExpertSystem:
    def __init__(self):
        self.cargo_schedule = []

    def add_cargo(self):
        cargo_id = input("Enter Cargo ID: ")
        flight_id = input("Enter Flight ID for the Cargo: ")
        weight = float(input("Enter Cargo Weight (in kg): "))
        priority = input("Enter Priority (High/Medium/Low): ")

        self.cargo_schedule.append({
            'cargo_id': cargo_id,
            'flight_id': flight_id,
            'weight': weight,
            'priority': priority
        })
        print(f"Cargo {cargo_id} scheduled for flight {flight_id}.\n")

    def show_cargo_schedule(self):
        if not self.cargo_schedule:
            print("No cargo scheduled yet.\n")
        else:
            print("\nScheduled Cargo:")
            for cargo in self.cargo_schedule:
                print(f"Cargo {cargo['cargo_id']} | Flight: {cargo['flight_id']} | Weight: {cargo['weight']}kg | Priority: {cargo['priority']}")
            print()

def main():
    airline_system = AirlineSchedulingExpertSystem()
    cargo_system = CargoSchedulingExpertSystem()

    while True:
        print("=== Airline and Cargo Scheduling System ===")
        print("1. Add Flight")
        print("2. Show Scheduled Flights")
        print("3. Add Cargo")
        print("4. Show Cargo Schedule")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            airline_system.add_flight()
        elif choice == '2':
            airline_system.show_flights()
        elif choice == '3':
            cargo_system.add_cargo()
        elif choice == '4':
            cargo_system.show_cargo_schedule()
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()  

theory
How the System Works:
Add Flight: Users can input flight details such as Flight ID, Aircraft, Crew member, Departure time, and Arrival time. The system checks if the aircraft and crew are available and assigns them to the flight.

Show Scheduled Flights: Displays all the scheduled flights with relevant details such as the Flight ID, Aircraft, Crew member, Departure, and Arrival times.

Add Cargo: Users can input cargo details such as Cargo ID, associated Flight ID, Cargo weight, and Priority. The system will assign the cargo to the respective flight.

Show Cargo Schedule: Displays all the scheduled cargo along with the flight it is assigned to, weight, and priority.

Exit: Exit the system.

Theory:
This interactive expert system assists airline and cargo scheduling by managing flights, aircraft, crews, and cargo efficiently.
Airline Scheduling:
Ensures that flights are scheduled only if the aircraft and crew are available.

Assigns crew and aircraft to flights once availability is confirmed.
Shows scheduled flights in a clear format.

Cargo Scheduling:
Allows users to assign cargo to specific flights based on cargo weight and priority.
Displays the cargo schedule with relevant details like cargo ID, flight ID, weight, and priority.
This interactive system can be expanded further by adding features like:
Conflict Resolution: Resolving conflicts when an aircraft or crew member is already assigned to another flight.
Flight and Cargo Status: Providing status updates for flights and cargo.
Capacity Checks: Ensuring that cargo does not exceed the aircraft's weight limit.








