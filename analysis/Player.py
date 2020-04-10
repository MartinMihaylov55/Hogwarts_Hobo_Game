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
        
    def move(self):
        if(self.currP > self.nextP) and ((self.position + 1) < self.length):
            self.position += 1
        elif (self.currP < self.nextP) and ((self.position - 1) > 1):
            self.position -= 1 
        else:
            print("illegal move")

    def setNextP(self,percentage):
        self.nextP = percentage

    def setCurrP(self,percentage):
        self.currP = percentage
    
    def setPrevP(self,percentage):
        self.prevP = percentage
    
    def addPercentage(self,percent):
        self.percentages.append(percent)

    def getHit(self, timeHit):
        self.health-=1
        self.recordInfo(self.position, timeHit)
        self.position-=1

    #Any hints or mistakes to learn from are recorded here in pair tuples with the position of that object and an int to record when the player was hit
    def recordInfo(self, position, description):
        if(position not in self.hints.keys()):
            self.hints[position] = []
        self.hints[position].append(description)

    #Hint
    def getHint(self):
        return self.hints[self.position]
    
    #Helper function
    def getPosition(self):
        return self.position

    def getHealth(self):
        return self.health