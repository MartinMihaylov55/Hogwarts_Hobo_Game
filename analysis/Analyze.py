from RailTrack import RailTrack
from Tunnel import Tunnel
from Train import Train
from Player import Player



import random
#This is the amount of time in seconds since the game started. If the player performs an action (ex. waits, hops), time is advanced by 1 second
elapsedTime = 0


# Take parameter as intput from stdin
tracks = int(input("Enter the number of tracks: "))

p = Player(0)
t = Tunnel(tracks) # Railtracks and trains are in here


print("Generated RailTrack object successfully, " + str(t))

fcount = 0 # count failiures
mcount = 1 # count for every actions to get the percentage
# Game Loop run for n iterations
#for i in range(tracks):
while True:   
    #player on track at that time and there is a train coming up
    # This might be redundant

    # In each step:
    # We ask our player if they want to move (potential algorithm: move to random track)
    decision = input("Move to new track? (Y/N)")
    if decision.lower() == "y":
        p.move(1)
    elif decision.lower() == "n":
        print("staying")
    else:
        print("Undefined command")
    # We ask benchmark player if they want to move
    


    # Move trains, check for collisions
    # Move train randomly

    #get current time

    #Check for colision
    
    # Sum the failiures
     # percentage
    # After all iterations are done return return the percentage of successes for each player and other data of the game
    print("#---------------------------------------------------------#")
    railT = t.getRailTracks()
    for i in railT:
        print("Coming in: 3")# replace it with actual time
        print("Player current position: ",p.getPosition())
        if t.railtracks[p.position].occupiedByTrain:
            p.getHit(elapsedTime)
            print("You got hit!")
            fcount +=1
        pc = (fcount/mcount)*100
        print("Safety percentage: ",pc," %")
        elapsedTime += 1
    print("#---------------------------------------------------------#")
    # Then update the game
    t.update()
# Give schedule to arriving trains
def timeGenerator(start):
    return random.randint(start,60)




#Display time
