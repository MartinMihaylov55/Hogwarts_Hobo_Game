from Tunnel import Tunnel
from RailTrack import RailTrack
from Train import Train

class Player:
    def __init__(self, position,length):
        self.position = position
        self.health = 10
        self.party = [] #The hobos in your party
        self.hints = {} #Any info you learn about the trains
        self.prevP = 0
        self.nextP = 0
        self.currP = 0
        self.length = length
        self.percentages = []
        
    def move(self,pos):
        self.position = pos       

    
    def setPrevP(self,percentage):
        self.prevP = percentage
    
    def addPercentage(self,percent):
        self.percentages.append(percent)

    def getHit(self, timeHit):
        self.health-=1
        self.recordInfo(self.position, timeHit)
        if not(self.position <= 0):
            self.move(self.position-1)
        else:
            self.move(self.position+1)

    #Any hints or mistakes to learn from are recorded here in pair tuples with the position of that object and an int to record when the player was hit
    def recordInfo(self, position, timeHit):
        if(position not in self.hints.keys()):
            self.hints[position] = []
        self.hints[position].append(timeHit)

    #Hint
    def getHint(self):
        return self.hints[self.position]
    
    #Helper function
    def getPosition(self):
        return self.position

    def getHealth(self):
        return self.health