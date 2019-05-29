# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    """the enviroments where our characters will traverse and interact with"""
    def __init__(self, terrain, light, hazards):
        self.terrain = terrain
        self.light = light
        self.hazards = hazards
    def ambience(self, music):
        if music >0 and hazards < 1:
            hazards += music