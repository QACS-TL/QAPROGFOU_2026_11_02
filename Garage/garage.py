from car import Car
red_car = Car("Audi", "A4", 2023, 15)
print(f"Make: {red_car.make}, Model: {red_car.model}, Year: {red_car.year}, Speed: {red_car.speed} mph")

blue_car = Car()
print(f"Make: {blue_car.make}, Model: {blue_car.model}, Year: {blue_car.year}, Speed: {blue_car.speed} mph")

red_car.accelerate(10)
blue_car.brake(5)

print(f"Make: {red_car.make}, Model: {red_car.model}, Year: {red_car.year}, Speed: {red_car.speed} mph")
print(f"Make: {blue_car.make}, Model: {blue_car.model}, Year: {blue_car.year}, Speed: {blue_car.speed} mph")