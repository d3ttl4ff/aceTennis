import random
import matplotlib.pyplot as plt

from Config import *
from output import Output

#Welcome message and default parameter values
# print("SIMPLE MENS' SINGLES TENNIS SIMULATOR")
print(BANNER)
P0FS  = 0.76
P0FSW = 0.74
P0SS  = 0.94
P0SSW = 0.41
P1FS  = 0.70
P1FSW = 0.71
P1SS  = 0.92
P1SSW = 0.60

#Ask the user if they want to specify different parameter values
s = input("[~] Use default input parameters? (y/n) >> ")
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
print("")
     
def PointWinner(serving, P0FS, P0FSW, P0SS, P0SSW, P1FS, P1FSW, P1SS, P1SSW):
    """The function takes the current server as a parameter and returns the winner of the point."""
    # If Player 0 is serving
    if serving == 0:
        if random.random() < P0FS:
            # First serve is in, determine if it wins the point
            return 0 if random.random() < P0FSW else 1
        else:
            # First serve was a fault, check second serve
            if random.random() < P0SS:
                # Second serve is in, determine if it wins the point
                return 0 if random.random() < P0SSW else 1
            else:
                # Both serves are faults, opponent wins the point
                return 1
            
    # If Player 1 is serving
    else:
        if random.random() < P1FS:
            # First serve is in, determine if it wins the point
            return 1 if random.random() < P1FSW else 0
        else:
            # First serve was a fault, check second serve
            if random.random() < P1SS:
                # Second serve is in, determine if it wins the point
                return 1 if random.random() < P1SSW else 0
            else:
                # Both serves are faults, opponent wins the point
                return 0

def PlayGame(serving, P0FS, P0FSW, P0SS, P0SSW, P1FS, P1FSW, P1SS, P1SSW):
    """The function simulates a game (with the same player serving throughout) and determines the winner.
    """
    # Initialize the scores for both players in a dictionary with the names of the players as keys
    score = {"Player 0": 0, "Player 1": 0}
    
    # Initialize a counter for the number of points played
    point_count = 0
    
    print(f"Player {serving} serving.")
    # Continue playing the game until one player wins
    while True:
        # Determine the winner of the point
        winner = PointWinner(serving, P0FS, P0FSW, P0SS, P0SSW, P1FS, P1FSW, P1SS, P1SSW)
        
        # Increment the score of the winner
        score["Player " + str(winner)] += 1
        
        # Increment the point count
        point_count += 1
        
        # Print the outcome of the current point
        print(f"Point {point_count}: Player {winner} wins the point. Current score - Player 0: {score['Player 0']}, Player 1: {score['Player 1']}")
        
        # If the winner has won 4 or more points and has 2 more points than the opponent, the game is over
        if score["Player " + str(winner)] >= 4 and score["Player " + str(winner)] - score["Player " + str(1-winner)] >= 2:
            # # Print the game winner and final scores
            # print(f"\nGame Winner: Player {winner}. Final score - Player 0: {score['Player 0']}, Player 1: {score['Player 1']}")
            return winner

def PlaySet(serving, P0FS, P0FSW, P0SS, P0SSW, P1FS, P1FSW, P1SS, P1SSW):
    """The function simulates an entire set and determines the winner.
    [Parameters]:
    P0FS (float): Probability of Player 0's first serve being legal.
    P0FSW (float): Probability of Player 0 winning the point on his first serve.
    P0SS (float): Probability of Player 0's second serve being legal.
    P0SSW (float): Probability of Player 0 winning the point on his second serve.
    P1FS (float): Probability of Player 1's first serve being legal.
    P1FSW (float): Probability of Player 1 winning the point on his first serve.
    P1SS (float): Probability of Player 1's second serve being legal.
    P1SSW (float): Probability of Player 1 winning the point on his second serve.
    """
    # Initialize the scores for both players in a dictionary with the names of the players as keys
    score = {"Player 0": 0, "Player 1": 0}
    
    # Initialize a counter for the number of games played
    game_count = 0
    
    # Track game wins over time for plotting
    game_wins = {"Player 0": [], "Player 1": []}
    
    # Continue playing the set until one player wins 6 or more games and has 2 more games than the opponent
    while True:
        # Determine the winner of the game
        game_winner = PlayGame(serving, P0FS, P0FSW, P0SS, P0SSW, P1FS, P1FSW, P1SS, P1SSW)
        
        # Increment the score of the game_winner
        score["Player " + str(game_winner)] += 1
        
        # Increment the game count
        game_count += 1
        
        # Print the outcome of the current game
        print(f"+{'-'*75}+")
        print(f"Game {game_count}: Player {game_winner} wins the game. Current game wins - Player 0: {score['Player 0']}, Player 1: {score['Player 1']}")
        print("")
        game_wins["Player 0"].append(score["Player 0"])
        game_wins["Player 1"].append(score["Player 1"])
        
        # If the game_winner has won 6 or more games and has 2 more games than the opponent, the set is over
        if score["Player " + str(game_winner)] >= 6 and score["Player " + str(game_winner)] - score["Player " + str(1-game_winner)] >= 2:
            # # Print the set winner and final scores
            # print(f"Set Winner: Player {game_winner}. Final score - Player 0: {score['Player 0']}, Player 1: {score['Player 1']}")
            # Output.PlotGameWins(game_wins)
            return game_winner, game_wins
        
        # Switch the server for the next game
        serving = 1 - serving
 
def PlayMatch():
    """The function simulates an entire match and determines the winner.
    """
    # Initialize the scores for both players in a dictionary with the names of the players as keys
    score = {"Player 0": 0, "Player 1": 0}
    
    # Initialize a counter for the number of sets played
    set_count = 0
    
    # Track set wins over time for plotting
    set_wins = {"Player 0": [], "Player 1": []}
    
    # Continue playing the match until one player wins 3 sets
    while True:
        # Determine the winner of the set
        set_winner, game_wins = PlaySet(serving, P0FS, P0FSW, P0SS, P0SSW, P1FS, P1FSW, P1SS, P1SSW)
        
        # Increment the score of the set_winner
        score["Player " + str(set_winner)] += 1
        
        # Increment the set count
        set_count += 1
        
        # Print the outcome of the current set
        print(f"+{'-'*75}+")
        print(f"Set {set_count}: Player {set_winner} wins the set. Current set wins - Player 0: {score['Player 0']}, Player 1: {score['Player 1']}")
        print("")
        set_wins["Player 0"].append(score["Player 0"])
        set_wins["Player 1"].append(score["Player 1"])
        
        # Prepare data for the table output
        data = []
            
        for i in range(2):
            data.append([f"Player {i}", set_wins["Player " + str(i)][-1], game_wins["Player " + str(i)][-1]])    
        
        # Print the table output       
        columns = ["Player", "Current Set Wins", "No of games won in this set"]
        # Output.print(f"[+] Player {set_winner} WON!", color='green', attrs='bold')
        Output.print_title(f"Set {set_count} Winner : Player {set_winner}")
        Output.table(columns, data)
        
        # Output.PlotGameWins(set_wins)
        
        # If the set_winner has won 3 sets, the match is over
        if score["Player " + str(set_winner)] >= 3:
            # Print the match winner and final scores
            print(f"\nMatch Winner: Player {set_winner}. Final score - Player 0: {score['Player 0']}, Player 1: {score['Player 1']}")
            
            Output.print_subtitle(str(set_winner), str(score['Player 0']), str(score['Player 1']))
            
            return set_winner
        
PlayMatch()

print("\nEnd of simulation.")


