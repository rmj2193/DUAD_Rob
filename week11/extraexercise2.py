class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed = max(0, self.speed - amount)

    def __str__(self):
        return f"{self.brand} {self.model} - Speed: {self.speed} km/h"


# Example 
if __name__ == "__main__":
    car = Car("Toyota", "Corolla")

    car.accelerate(50)
    print(car)

    car.brake(20)
    print(car)

    car.brake(50)  # shouldn't go below 0
    print(car)