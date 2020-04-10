class Train:
    def __init__(self, position, track, spendTime, nextSpendTime):
        self.position = position
        self.track = track
        self.spendTime = spendTime
        self.nextSpendTime = nextSpendTime
        
    def getPostion(self):
        return self.position

