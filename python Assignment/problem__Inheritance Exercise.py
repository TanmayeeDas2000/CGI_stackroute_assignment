(''' INHERITANCE

1- Create a base class 'vehicle' with attributes 'make' and 'model'. Create derived classes 'car' and 
    'motorcycle' with their own attribute and method.
2- Implement a class hierarchy for different types of employees in an organization using inheritance 
''')


class vehicle:
    def __init__(self,make):
        self.make = make

    def model(self):
        pass

class car(vehicle):
    def model(self):
        return "ferrari"

class bike( vehicle):
    def model(self):
        return "bmw"

car1 = car("sports")
bike1 = bike("crusher")

print(f"Car make is {car1.make} and model {car1.model()}")
print(f"Bike make is {bike1.make} and model {bike1.model()}")