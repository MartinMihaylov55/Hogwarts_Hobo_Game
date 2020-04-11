from Tunnel import Tunnel
from RailTrack import RailTrack
from Train import Train
import random
class Hobo:
    def __init__(self, position, totalTracks):
        self.totalTracks = totalTracks
        self.position = random.randint(0,totalTracks)

    def getPosition(self):
        return self.position
    
    def hint(self, Train):
        return Train.getNextTime()
        
    #get the lowest pecentage
    #add return lowest