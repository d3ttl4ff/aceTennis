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

""" A men’s singles tennis match is played between two players. In each game, one player is designated as a
 server and one as a receiver. Service alternates game by game. A single game consists of a sequence of points
 played with the same player serving. A game is won by a player only when (a) he scores four or more points
 and (b) he has two or more points than his opponent.
 In this simulation, the winner of the tennis match is the first player to win three sets in total (i.e. best of
 f
 ive sets). Unlike grand slam tournaments such as Wimbledon, a player wins a set when (a) he has won six
 or more games and (b) he has won two or more games than his opponent in the set (i.e., we do not consider
 “tie breaks”). If you are unfamiliar with the scoring system of tennis, further information can be found at
 http://en.wikipedia.org/wiki/Tennis.
 For each point in tennis, the server has two opportunities to serve. Typically, his first serve will be fast but
 less accurate. This means that if his first serve is deemed legal, he has a slightly higher chance of winning
 the point compared to his second serve. If his first serve is illegal then his second serve will generally be hit
 with less power but more accuracy, giving it a greater chance of being legal. However, due to this slower
 pace, the server also has a slightly lower chance of winning the point. In this simulation, a tennis player’s
 abilities can therefore be described using four performance statistics
 
 Probability of his first serve being legal
 Probability of winning the point on his first serve
 Probability of his second serve being legal
 Probability of winning the point on his second serve
 
  The supplied code tennis.py gives a basic program for reading in the user-defined parameters. Once these
 values have been read in, the program also randomly decides which of the two players is to serve first (50:50
 chance). Players are identified by the integers 0 and 1.
 Write a function called PointWinner. This should take the current server as a parameter (plus any other
 parameters deemed useful) and should return the winner of a particular point, calculated according to the
 performance statistics defined above. (Note that only the server’s performance statistics determine the winner
 of a particular point, not his opponent’s).
 """
     
def PointWinner(serving, P0FS, P0FSW, P0SS, P0SSW, P1FS, P1FSW, P1SS, P1SSW):
    """The function takes the current server as a parameter and returns the winner of the point.
    [Parameters]:
    serving (int): The player who is serving (0 or 1).
    P0FS (float): Probability of Player 0's first serve being legal.
    P0FSW (float): Probability of Player 0 winning the point on his first serve.
    P0SS (float): Probability of Player 0's second serve being legal.
    P0SSW (float): Probability of Player 0 winning the point on his second serve.
    P1FS (float): Probability of Player 1's first serve being legal.
    P1FSW (float): Probability of Player 1 winning the point on his first serve.
    P1SS (float): Probability of Player 1's second serve being legal.
    P1SSW (float): Probability of Player 1 winning the point on his second serve.
    """
    # If Player 0 is serving
    if serving == 0:
        # First serve successful
        if random.random() < P0FS: 
            # First serve winner if the random possibility is less than the probability of winning the point on first serve
            return 0 if random.random() < P0FSW else 1 
        # First serve fault and Second serve successful
        elif random.random() < P0SS:
            # Second serve winner if the random possibility is less than the probability of winning the point on second serve
            return 0 if random.random() < P0SSW else 1
        # Both first and second serve faults so the point goes to the opponent (Player 1)
        else:
            return 1
        
    # If Player 1 is serving
    else:
        # First serve successful
        if random.random() < P1FS:
            # First serve winner if the random possibility is less than the probability of winning the point on first serve
            return 1 if random.random() < P1FSW else 0
        # First serve fault and Second serve successful
        elif random.random() < P1SS:
            # Second serve winner if the random possibility is less than the probability of winning the point on second serve
            return 1 if random.random() < P1SSW else 0
        # Both first and second serve faults so the point goes to the opponent (Player 0)
        else:
            return 0


print("End of simulation.")

