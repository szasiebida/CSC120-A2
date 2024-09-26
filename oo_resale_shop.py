from computer import *

class ResaleShop:

    # attribute inventory
    inventory:list


    #constructor 
    def __init__(self, inventory:list, ):
        self.inventory=inventory

    #function to buy a computer and add to the inventory 
    def buyComputer(self, computer:Computer):
        self.inventory.append(computer)
    
    #function to sell  a computer and remove to the inventory 
    def sellComputer(self, computer:Computer):
        if computer in self.inventory:
            self.inventory.remove(computer)
        else: 
            print('computer doesnt exist')
        
    #function to update the price 
    def updatePrice(self,computer:Computer, new_price:int):
        if computer in self.inventory:
            computer.price=new_price
        else:
            print('computer doesnt exist')

    #function to update the computer operating system 
    def updateComputer(self,computer:Computer, new_operating_system:str):
        if computer in self.inventory:
            computer.operating_system=new_operating_system
        else:
            print('computer doesnt exist')
   
    #function to print the inventory 
    def printInventory(self, computer:Computer):
        for computer in self.inventory:
            print(computer.description)
    
    #function to refurbish the computer and change the price and the operating system 
    def refurbish(self, computer:Computer, new_operating_system:str):
        if computer in self.inventory:
            if computer.year_made < 2000:
                computer.price=0
            elif computer.year_made < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif computer.year_made < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

            computer.operating_system = new_operating_system # update details after installing new OS
        else:
            print("Item", computer.description, "not found. Please select another item to refurbish.")

def main():
    computer =Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    computers=[]
    # computers.append(computer)
    computer2 =Computer(
        "Mac (Late 2005)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2005, 100
    )
    # computers.append(computer2)

    myshop=ResaleShop(computers)
    print(myshop.inventory)
    myshop.buyComputer(computer2)
    print(myshop.inventory[0].description)
    print('hello')
    print(computer2.price)
    myshop.updatePrice(computer2,20)
    print(computer2.price)
    #variable.method(parmater)
    print(computer2.operating_system)
    myshop.updateComputer(computer2,'idk')
    print(computer2.operating_system)
    myshop.refurbish(computer2,'meow')
    print(computer2.operating_system)
    myshop.printInventory(myshop.inventory)



main()