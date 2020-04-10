from Train import Train
import random
class RailTrack:
    #Add more objects
    def __init__(self, position):
        self.position = position
        self.train = Train(position,self,random.randint(1,3),random.randint(1,3))
        self.occupiedByTrain = False
        self.timer = 0
        self.deltaTime = 0

    def __str__(self):
        return "RailTrack: position " + str(self.position)
    
    def update(self):
        if(self.occupiedByTrain):
            if(self.deltaTime == (self.timer%4)):
                self.occupiedByTrain = False
            else:
                self.deltaTime+=1           
        else:
            if(self.deltaTime == (self.timer%4)):
                self.occupiedByTrain = True
            else:
                self.deltaTime+=1
        self.timer+=1
    