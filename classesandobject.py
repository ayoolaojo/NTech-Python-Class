# class Car :
#     name = "Toyota"
#     brand = "Corolla"
#     transmission = "manual"
#     year = 1999
#     wheel = 4
#     color = "red"
# Car1 = Car()
# print(Car1.wheel)
# print(Car1.name)


# Car2 = Car()
# print(Car2.year)



# class Animal:
#     def __init__(self, name , classification):
#         self.name = name
#         self.classification = classification

# Animal1 = Animal("dog", "carnivore")
# Animal2 = Animal("goat", "herbivore")
# Animal3 = Animal("tiger" , "carnivore")


# print(Animal3.name   +  ":"  +  Animal3.classification)
    
class Player:
    def __init__(self, name, position, number, club ):
        self.name = name
        self.position = position
        self.number = number
        self.club = club
        
    def Passing(self):
        print(f"{self.name} passes the ball")
        
    def Dribbling(self):
        print(f"{self.name} dribbles")
        
    def Shooting(self):
        print(f"{self.name} shoots")
        
    def PlayerInfo(self):
        print(f"{self.name} is {self.position}  wears {self.number } at {self.club}")
        
Player1 = Player("Ronaldo", "forward", 7 , "Al-nasri")
Player2 = Player("Messi", "forward", 10 , "InterMiami")

Player1.PlayerInfo()

Player2.Passing()

Player1.Shooting()



# Inheritance

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def make_sound(self):
        print(f"{self.name} makes sound")
        
class Dog(Animal):
    def make_sound(self):
        return f"{self.name}  barks"
        
dog1 = Dog("Buddy" , 18 )
print(dog1.name)

goat1 = Animal("Messi" , 37)

goat1.make_sound()
dog1.make_sound()



        
        
        
        