from Tunnel import Tunnel
from RailTrack import RailTrack
from Train import Train
class Hobo:
    def __init__(self, position):
        self.position = position
        self.paperPlanes = [] 
            
    def getHint(self):
        return self.paperPlanes.pop(self.position)

    def addInfo(self, position):
        self.paperPlanes[self.position] = position

    def getPosition(self):
        return self.position
    
    #get the lowest pecentage
    #add return lowest