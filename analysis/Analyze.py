from RailTrack import RailTrack
from Tunnel import Tunnel

#This is the amount of time in seconds since the game started. If the player performs an action (ex. waits, hops), time is advanced by 1 second
elapsedTime = 0

t = Tunnel(5)
print("Generated RailTrack object successfully, " + str(t))

# Take parameter as intput from stdin
# Game Loop run for n iterations
# In each step:
# We ask our player if they want to move (potential algorithm: move to random track)
# We ask benchmark player if they want to move
# Move trains, check for collisions
# Sum the failiures
# After all iterations are done return return the percentage of successes for each player