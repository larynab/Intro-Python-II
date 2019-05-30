# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    """the enviroments where our characters will traverse and interact with"""
    def __init__(self, name, description, terrain = None, light = None, hazards = None):
        self.name = name
        self.description =description
        self.terrain = terrain
        self.light = light
        self.hazards = hazards
        self.n_to = None
    def ambience(self, music):
        if music >0 and hazards < 1:
            hazards += music