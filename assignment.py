'''Two people in a house sharing house
rent to be paid on how many days
one(one of the occupant) spent
staying at home
'''
class House:
    def __init__(self, name, rent):
        self.name = name
        self.rent = rent
# CORRECTION TO THIS ASSIGNMENT

# ASSIGNMENT 2:  ON API
'''
CALCULATE ALL THE PRICES IN THE JSON API URL
'''
# ASSIGNMENT 3: API BASED
'''
MORE ON API'S EXAMPLE; CRYPTO-CURRENCY API'S, BINANCE, COIN MARKET APP
'''

# ASSIGNMENT 4: REVISION ON CLASS
'''
Create a store that sells only wine, 
create a customer that buys only wine and 
collect the name of the wine and the quantity then amt in int.
Write a logic that if a customer buys certain amount of wine it substracts 
the amout from the quantity and print it out that we have ___ of amt of wine left
'''
# SOLUTION

class Store:
    def __init__(self, name, brand, quantity):
        self.name = name 
        self.brand = brand
        self.quantity = quantity

    def sell(self):
        print(F"We Sell {self.quantity} {self.brand} In {self.name}. ")
        
    def buy(self):
        amt = int(input("Please Input The Amount Of Drinks You Want To Buy: "))
        print(F"I Want To Buy {amt} {self.brand}")
        sum = self.quantity - amt
        print(F"We Have {sum} brands of {self.brand} remaining In {self.name}.")
x = Store("EverGreen Concepts", "Red Wines", 90)
x.sell()
x.buy()
print(x)