class Train:
    def __init__(self, position, track, speed,time):
        self.position = position
        self.track = track
    def move(self):
        self.position += 1
    def getPosition(self):
        return self.postion
    def getTrack(self):
        return self.track

#Do we need the time?
#We could've just use the speed and the distance to get the time
