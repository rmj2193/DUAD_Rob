class Person:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person: Person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} boarded the bus.")
        else:
            print("The bus is full. Can't add more passengers.")

    def remove_passenger(self):
        if self.passengers:
            removed = self.passengers.pop(0)   # remove first
            print(f"{removed.name} got off the bus.")
        else:
            print("There are no passengers left to remove.")


# Example 
if __name__ == "__main__":
    bus = Bus(2)

    p1 = Person("Rob")
    p2 = Person("Carlos")
    p3 = Person("Juan")

    bus.add_passenger(p1)
    bus.add_passenger(p2)
    bus.add_passenger(p3)  # should say bus is full

    bus.remove_passenger()
    bus.remove_passenger()
    bus.remove_passenger()