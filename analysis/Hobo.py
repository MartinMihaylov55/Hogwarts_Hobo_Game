from Tunnel import Tunnel
from RailTrack import RailTrack
from Train import Train
class Hobo:
    def __init__(self, position):
        self.position = position
        self.hint = []

    def addInfo(self, position):
        self.paperPlanes[self.position] = position

    def getPosition(self):
        return self.position
    
    def hint(self, Train):
        return Train.getNextTime()
        
    #get the lowest pecentage
    #add return lowest