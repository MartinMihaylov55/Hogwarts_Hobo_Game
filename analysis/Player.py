from Tunnel import Tunnel
from RailTrack import RailTrack

class Player:
    def __init__(self, position):
        self.position = position
        self.health = 10
        self.party = [] #The hobos in your party
        self.hints = [] #Any info you learn about the trains
        
    def move(self, steps):
        self.position += steps
    
    #Any hints or mistakes to learn from are recorded here in 3-long tuples with what object it relates to, the position of that object, and a string with what info is stored (ex. Time until next train)
    def recordInfo(self, relatedObject, position, description):
        self.hints.append((relatedObject, position, description))