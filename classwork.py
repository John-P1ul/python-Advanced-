class Car:
    def __init__(self):
        self.name = "Toyota"
        self.colour = "Red"

My_Car = Car()
print(f"{My_Car.name} Is A Company Which Produces Cars Of Different Colour And Sizes Especially {My_Car.colour} Cars")

class Phone:
    def __init__(self, os, name, colour):
        self.os = os
        self.name = name
        self.colour = colour

    def call(self):
        print(f"{self.name} can make local and international calls ")

    def camera(self):
        print(f"{self.name} has perfect image capturing")

iphone = Phone("IOS", "iPhone 15 pro", "cyan Black")
samsung = Phone("Android", "Samsung s24 ultra", "Silver")
iphone.call()
iphone.camera()
samsung.call()
samsung.camera()
# print(iphone.name, iphone.os)

# x = Phone()
# print(f"{x.device} is a device which have been given a name called {x.name} and its {x.colour} in colour")


# # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class House:
    def __init__(self, rooms, windows, doors, flats, cupboard, bed, wardrobe, dinning_table, garage, cooking_utensils):
        self.rooms = rooms
        self.windows = windows 
        self.doors = doors
        self.flats = flats
        self.cupboard = cupboard
        self.bed = bed
        self.wardrobe = wardrobe
        self.dinning_table = dinning_table
        self.garage = garage
        self.cooking_utensils = cooking_utensils
        
    def purpose(self):
        pass
        
class Duplex(House):
    def purpose(self):
        return"For Personal And Family Usage"
    
class Church(House):
    def purpose(self):
        return"A Place Of Worship For Christians"

class Home(House):
    def purpose(self):
        return"For Shelter"
    
class Hotel(House):
    def purpose(self):
        return"For Lodging(Shelter) Incase If One Is Far Away From Home"
class School(House):
    def purpose(self):
        return"A Place For Learning And Creativity"

duplex = Duplex("4-5 rooms", "7-10 windows", "4-8 doors", "No Flats Just Rooms", "2-3 cupboards", "4-5 beds", "4-5 wardrobe", "0-1 dinning table", "Yes, Enough For Two Cars", "Yes")
church = Church("1-2 rooms", "10-14 windows", "4-9 doors", "None", "1 cupboard", "None", "at_least 1 wardrobe", "Non", "Yes, Enough For Many Cars", "None")
home = Home("2-3 rooms", "5-6 windows", "3-6 doors", "1-19 flats", "1-3 cupboards", "2-3 beds", "2-3 wardrobe", "0-1 dinning table", "Yes, Enough For At Least 1-2 Cars", "Yes")
hotel = Hotel("Many rooms", "Many windows", "Many doors", "None", "Many cupboards", "Many beds", "Many wardrobe", "Non", "Yes, Enough For Many Cars", "Yes")
school = School("Many rooms", "Many windows", "Many doors", "None", "1-10 cupboards", "1-2 beds", "None", "None", "Yes, Enough For At Least 1-4 Cars", "None")

print(duplex.rooms, duplex.windows, duplex.doors)