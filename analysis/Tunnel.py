from RailTrack import RailTrack

class Tunnel:
    def __init__(self,length):
        self.length = length
        self.railtracks = []
        for i in range(length):
            self.railtracks.append(RailTrack(i))
            
    def __str__(self):
        return "Tunnel " + str(list(map(lambda s: str(s), self.railtracks)))