from Tunnel import Tunnel
from RailTrack import RailTrack
from Train import Train

class Player:
    def __init__(self, position):
        self.position = position
        self.health = 10
        self.party = [] #The hobos in your party
        self.hints = {} #Any info you learn about the trains
        
    def move(self, steps):
        if((self.position + steps) > 0):
            self.position += steps       
        else:
            print("You can't go any further back!")
    
    def getHit(self, timeHit):
        self.health-=1
        self.recordInfo(self.position, timeHit)
        self.move(-1)

    def gameOver(self):
        result = ""
        if self.health == 0:
            result = "Game over!"
        return result

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

    def findRoute(self):
        return True