# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    """The avatar the user will be controlling through the world"""
    def __init__(self, name, room = None, inventory = []):
        self.name = name
        self.room = room
        self.inventory = inventory
    def addItem(self, item):
        self.inventory.append(item) 