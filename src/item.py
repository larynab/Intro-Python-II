class Item:
    """Objects to pick up and use in the world"""
    def __init__(self, name, room = None, player = None):
        self.name = name
        self.room = room
        self.player = player