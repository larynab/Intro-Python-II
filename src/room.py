# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    """the enviroments where our characters will traverse and interact with"""
    def __init__(self, name, description, terrain = None, light = None, hazards = None, inventory = []):
        self.name = name
        self.description =description
        self.terrain = terrain
        self.light = light
        self.hazards = hazards
        self.n_to = None
        self.inventory = inventory
    def ambience(self, music):
        if music >0 and hazards < 1:
            hazards += music
    def addItem(self, item):
        self.inventory.append(item) 
    def transferItem(self, itemname, player):
        for index, item in enumerate(self.inventory):
            print(index)
            print(itemname)
            print(self.inventory)
            if  item.name == itemname:
                print(f"picked up {itemname}, and added to your inventory")
                founditem = item 
                del self.inventory[index]
                player.addItem(founditem)
                return
        print("item not found")
        return None  
    def __str__(self):
        #empty space
        inv_str = ""
        for item in self.inventory:
            inv_str += item.name + " "
        return inv_str    