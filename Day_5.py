"""
Assignment: Modify Or Update This Code To Be On A Loop

"""
class WiFi:
    def __init__(self, name, network, password, type):
        self.name = name
        self.network = network
        self.password = password
        self.type = type
        
    def create_wifi(self):
        print(f"Wifi {self.name} has been created")

    def connect(self):
        print("Do You Want To Connect\n(a.) Yes\n(b.) No")
        response = str(input(">> "))
        if response == "a" or response == "Yes":
            password = str(input("Enter Password\n>> "))
            if password == self.password:
                print("Connection Successful")
            else:
                print("Incorrect Password!!! Try Again 🙁")
        elif response == "a" or response == "No":
            print("Ok... Enjoy The Rest Of Our Service")
        else:
            print("Invalid Request!")

        return "Connection Mode!!!"
    
print("You Can Now Create Your Own Wifi")
name = str(input("Enter Name\n>> "))
network = str(input("Enter Network\n>> "))
password = str(input("Enter Password\n>> "))
type = str(input("Enter Type\n>> "))
print("What Would You Like To Do?\n1. Create Wifi\n2. Connect To Wifi")
request = str(input(">> "))
if request == "1" or request == "Create Wifi":
    device = WiFi(name, network, password, type)
    device.create_wifi()
elif request == "2" or request == "Connect To Wifi":
    device = WiFi(name, network, password, type)
    device.connect()
else:
    print("Invalid Request")
# onazi = WiFi("Onazi", "Airtel", "wertyut4", "MiFi")
# onazi.connect()