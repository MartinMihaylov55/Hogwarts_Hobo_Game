import random

print("""
Welcome to Hobo Hogwarts!
For this deliverable there are some missing features or features that dont match the specifications:
# Must enter number of iterations to simulate
# No hobos
# No possion distribution, just random
# No random train duration, every train lasts for 1 step
# No random train arrial duration, train arrive randomly at each step
# Player does not stay on average for S second
Features that match the specification:
# Player can move to any track
# Benchmark algorithm moves when hit by train to random track
Algorithm Description
# Player alogrithm: player moves every step to random track
# Benchmark alogrithm: player moves to random track every time it collides
Note there is no exception handling in this version
""")

# Get input params
tn = int(input("Enter the number of tracks: "))
trackNum = tn - 1
if(tn < 1):
    print("Must have more than 0 tracks")
    exit(1)
stepNum = int(input("Enter the number of iterations to simulate: "))

# Init to random
playerPos = random.randint(0, trackNum)
benchMarkPos = random.randint(0, trackNum)

playerCollisionsCount = 0
benchCollisionsCount = 0

tracks = [0 for i in range(tn)] 

for x in range(stepNum):
    # Move player and benchmark
    playerPos = random.randint(0, trackNum)
    # Only move benchmark if hit by train
    if(tracks[benchMarkPos] == 1):
        benchMarkPos = random.randint(0, trackNum)

    # Move trains
    for i in range(tn):
        #  track 0 no train, 1 train
        tracks[i] = random.randint(0, 1)

    # Check for collisions
    # print(playerPos, benchMarkPos, tracks[playerPos], tracks[benchMarkPos])
    if(tracks[playerPos] == 1):
        playerCollisionsCount += 1
    if(tracks[benchMarkPos] == 1):
        benchCollisionsCount += 1

print("Results: ")
print("Simulated: ", stepNum)
print("Player collisions: ", playerCollisionsCount)
print("Benchmark collisions: ", benchCollisionsCount)
print("Player success percentage: %.2f" % (100 - playerCollisionsCount/float(stepNum)* 100) + "%")
print("Benchmark algorithm success percentage: %.2f" % (100 - benchCollisionsCount/float(stepNum)* 100) + "%")