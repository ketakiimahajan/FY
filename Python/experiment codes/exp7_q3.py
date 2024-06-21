from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def speed(self):
        pass
    
class FourWheeler(Vehicle):
    def __init__(self, name, speed):
        self.name = name
        self.speed_val = speed

    def speed(self):
        print(f"Name: {self.name}")
        print(f"Speed: {self.speed_val} km/h")

class TwoWheeler(Vehicle):
    def __init__(self, name, speed):
        self.name = name
        self.speed_val = speed

    def speed(self):
        print(f"Name: {self.name}")
        print(f"Speed: {self.speed_val} km/h")

name = input("Enter vehicle name: ")
four_wheeler_speed = float(input("Enter speed of four-wheeler: "))
two_wheeler_speed = float(input("Enter speed of two-wheeler: "))

four_wheeler = FourWheeler(name, four_wheeler_speed)
two_wheeler = TwoWheeler(name, two_wheeler_speed)

four_wheeler.speed()
two_wheeler.speed()