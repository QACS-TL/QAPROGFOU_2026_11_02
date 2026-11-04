class Car:
    def __init__(self, make="Ford", model="Fiesta", year=2020, speed=0):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self, increment):
        self.speed += increment
        print(f"The car has accelerated to {self.speed} mph.")

    def brake(self, decrement):
        self.speed -= decrement
        print(f"The car has slowed down to {self.speed} mph.")