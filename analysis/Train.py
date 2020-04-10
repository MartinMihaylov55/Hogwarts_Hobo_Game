class Train:
    def __init__(self, position, track, spendTime, nextSpendTime):
        self.position = position
        self.track = track
        self.spendTime = spendTime
        self.nextSpendTime = nextSpendTime
        
    def getPosition(self):
        return self.position

#next 
    def getNextTime(self):
        return self.nextSpendTime
    
    def updateTime(self):
        self.nextSpendTime -=1
