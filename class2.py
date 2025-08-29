class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement the move() method")


class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")


class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")


class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing on the water...")


# Function to demonstrate polymorphism
def start_journey(vehicle):
    print(f"Starting journey with a {vehicle.__class__.__name__}:")
    vehicle.move()
    print()


# Main program
if __name__ == "__main__":
    my_car = Car()
    my_plane = Plane()
    my_boat = Boat()

    start_journey(my_car)
    start_journey(my_plane)
    start_journey(my_boat)
