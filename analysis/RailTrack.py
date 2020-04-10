from Train import Train
import random
class RailTrack:
    #Add more objects
    def __init__(self, position,total):
        self.position = position
        self.total = total
        self.train = Train(position,self,random.randint(1,self.total),random.randint(1,self.total))
        #adjust the time
        self.occupiedByTrain = False
        self.timer = 0
        self.deltaTime = 0
        self.fails = 0

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
    
    def getTrain(self):
        return self.train

    def setNewTrain(self):
        if self.train.getNextTime() == 0:
            self.train = Train(self.position,self,random.randint(1,self.total),random.randint(1,self.total))
        
    def updateFail(self):
        self.fails += 1
    
    def getFails(self):
        return self.fails