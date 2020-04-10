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
for i in range(tracks):
    
    print(i)
    #player on track at that time and there is a train coming up
    if p.getPosition() == t.getTrainPos(i):
        p.getHit(elapsedTime)
        elapsedTime+=1


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

    # Sum the failiures
    pc = (fcount/mcount)*100 # percentage
    # After all iterations are done return return the percentage of successes for each player
    print(pc)
    # Then update the game
    t.update()
# Give schedule to arriving trains
def timeGenerator(start):
    return random.randint(start,60)



#Display time