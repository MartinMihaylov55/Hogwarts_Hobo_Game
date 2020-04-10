from RailTrack import RailTrack
from Tunnel import Tunnel
from Train import Train
from Player import Player

import random

#This is the amount of time in seconds since the game started. If the player performs an action (ex. waits, hops), time is advanced by 1 second
elapsedTime = 0


# Take parameter as intput from stdin
tracks = int(input("Enter the number of tracks: "))

p = Player(0,tracks)
t = Tunnel(tracks) # Railtracks and trains are in here


print("Generated RailTrack object successfully, " + str(t))

mcount = 1 # count for every actions to get the percentage
# Game Loop run for n iterations
#for i in range(tracks):
while True:   
    #player on track at that time and there is a train coming up
    # This might be redundant

    # In each step:
    # We ask our player if they want to move (potential algorithm: move to random track)
    decision = input("Move to new track? (Y/N)")
    if (decision.lower() == "y"):
        if (p.position <= t.length):
            p.move()
        else:
            print("Unable to advance")
    elif decision.lower() == "n":
        print("staying")
    else:
        print("Undefined command")
        break
        
    # We ask benchmark player if they want to move
    


    # Move trains, check for collisions
    # Move train randomly

    #get current time

    #Check for colision
    
    # Sum the failiures
     # percentage
    # After all iterations are done return return the percentage of successes for each player and other data of the game
    
    currPos = p.getPosition()
    
    print("#---------------------------------------------------------#")
    railT = t.getRailTracks()
    for i in railT:
        print(i)
        currTrain = i.getTrain()
        if p.getHealth() == 0:
            print("Game over!")
            exit(0)
        print("Player current position: ",currPos)
        print("Player's current health: ",p.getHealth())
        print("Coming in: ",currTrain.getNextTime())# replace it with actual time
        if currTrain.getNextTime() != 0:
            currTrain.updateTime()
        else:
            if currPos == currTrain.getPosition():
                p.getHit(elapsedTime)
                print("You got hit!")
                i.updateFail()
            i.setNewTrain()        
        pc = (i.getFails()/mcount)*100
        p.addPercentage(pc)
        print("Unsafe percentage: ",pc," %")
        elapsedTime += 1
        mcount += 1
    print("#---------------------------------------------------------#")

    p.setCurrP(p.percentages[currPos])
    p.setNextP(p.percentages[currPos + 1])
    p.setPrevP(p.percentages[currPos - 1])

    # Then update the game
    t.update()



