import random

#Welcome message and default parameter values
print("SIMPLE MENS' SINGLES TENNIS SIMULATOR")
P0FS  = 0.76
P0FSW = 0.74
P0SS  = 0.94
P0SSW = 0.41
P1FS  = 0.70
P1FSW = 0.71
P1SS  = 0.92
P1SSW = 0.60

#Ask the user if they want to specify different parameter values
s = input("Use default input parameters? (y/n) >> ")
if s != "y" and s != "Y":
    print("Please input the following information for Player 0, then Player 1:")
    print("-Probability first serve legal")
    print("-Probability of winning point on first serve")
    print("-Probability of second serve legal")
    print("-Probability of winning point on second serve")
    P0FS  = float(input("P0 first serve            >> "))
    P0FSW = float(input("P0 wins with first serve  >> "))
    P0SS  = float(input("P0 second serve           >> "))
    P0SSW = float(input("P0 wins with second serve >> "))
    P1FS  = float(input("P1 first serve            >> "))
    P1FSW = float(input("P1 wins with first serve  >> "))
    P1SS  = float(input("P1 second serve           >> "))
    P1SSW = float(input("P1 wins with second serve >> "))
#Check that all the parameters are valid probabilites
assert min(P0FS,P0FSW,P0SS,P0SSW,P1FS,P1FSW,P1SS,P1SSW) >= 0 and max(P0FS,P0FSW,P0SS,P0SSW,P1FS,P1FSW,P1SS,P1SSW) <= 1, "Error: All probabilites must be between 0 and 1"

#Decide who is serving first (player 0 or 1)
serving = random.randint(0, 1)
print("Player", serving, "serving first")

#...Now progam the simulation

print("End of simulation.")

