from RailTrack import RailTrack
from Tunnel import Tunnel

#This is the amount of time in seconds since the game started. If the player performs an action (ex. waits, hops), time is advanced by 1 second
elapsedTime = 0

t = Tunnel(5)
print("Generated RailTrack object successfully, " + str(t))