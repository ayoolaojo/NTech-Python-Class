# Create a class for Car, boat, and plane . To have 2 attributes, brand amd year, have move() as method.

class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    def move(self):
        print("Drive")
        
class Boat:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
        
    def move(self):
        print("Sail")        
        
class Plane:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def move(self) :
        print("fly")  
        
        


car1 = Car("Toyota", 2025) 
boat1 = Boat("Mercury", 2024)
plane1 = Plane("Boeing-jet", 747)
    
for x in (car1,boat1,plane1):
    x.move()