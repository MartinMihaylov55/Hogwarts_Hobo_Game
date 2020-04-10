from RailTrack import RailTrack
from Tunnel import Tunnel
from Train import Train
from Player import Player



import random
#This is the amount of time in seconds since the game started. If the player performs an action (ex. waits, hops), time is advanced by 1 second
elapsedTime = 0


# Take parameter as intput from stdin
tracks = int(input("Enter the number of tracks: "))
p = Player()
t = Tunnel(tracks)
print("Generated RailTrack object successfully, " + str(t))

fcount = 0 # count failiures
clock = 0 # keep track of time (per hour)
# Game Loop run for n iterations
for i in range(tracks):
    #train = Train(position,random.randint(t.getLength()),speed,time)
    print(i)

    # In each step:
    # We ask our player if they want to move (potential algorithm: move to random track)
    # We ask benchmark player if they want to move
    # Move trains, check for collisions
    # Sum the failiures
    # After all iterations are done return return the percentage of successes for each player

# Give schedule to arriving trains
def timeGenerator(start):
    return random.randint(start,23)
