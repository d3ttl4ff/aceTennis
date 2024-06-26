import random
import matplotlib.pyplot as plt

from Config import *
from output import Output
from logger import logger

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

probability_data = []
probability_data.append(["Player 0", P0FS, P0FSW, P0SS, P0SSW])
probability_data.append(["Player 1", P1FS, P1FSW, P1SS, P1SSW])

columns = ["Player", "First Serve Legal", "Win Pt First Serve", "Second Serve Legal", "Win Pt Second Serve"]

Output.table(columns, probability_data)
print("")

#Ask the user if they want to specify different parameter values
# s = input("[~] Use default input parameters? (y/n) > ")
s = input(Output.colored("[~] Use default input parameters? (y/n) > ", color='white', attrs='bold'))
print("")
if s != "y" and s != "Y":
    Output.print("[~] Please input the following information for Player 0, then Player 1:", color='white', attrs='bold')
    logger.warning("Probability of first serve legal (ex: 0.76)")
    logger.warning("Probability of winning point on first serve (ex: 0.74)")
    logger.warning("Probability of second serve legal (ex: 0.94)")
    logger.warning("Probability of winning point on second serve (ex: 0.41)")
    
    print("")
    P0FS   = float(input(Output.colored("[+] P0 first serve            > ", color='197', attrs='bold')))
    P0FSW  = float(input(Output.colored("[+] P0 wins with first serve  > ", color='197', attrs='bold')))
    P0SS   = float(input(Output.colored("[+] P0 second serve           > ", color='197', attrs='bold')))
    P0SSW  = float(input(Output.colored("[+] P0 wins with second serve > ", color='197', attrs='bold')))
    P1FS   = float(input(Output.colored("[+] P1 first serve            > ", color='12', attrs='bold')))
    P1FSW  = float(input(Output.colored("[+] P1 wins with first serve  > ", color='12', attrs='bold')))
    P1SS   = float(input(Output.colored("[+] P1 second serve           > ", color='12', attrs='bold')))
    P1SSW  = float(input(Output.colored("[+] P1 wins with second serve > ", color='12', attrs='bold')))

   
#Check that all the parameters are valid probabilites
assert min(P0FS,P0FSW,P0SS,P0SSW,P1FS,P1FSW,P1SS,P1SSW) >= 0 and max(P0FS,P0FSW,P0SS,P0SSW,P1FS,P1FSW,P1SS,P1SSW) <= 1, "Error: All probabilites must be between 0 and 1"

livematch = False
matchchoice = input(Output.colored("[~] Do you want to see the live output? (y/n) > ", color='white', attrs='bold')).lower()
# print("")

if matchchoice == "y":
    livematch = True
    
serve_win_choice = input(Output.colored("[~] Do you want to see the serve win percentage graph upon completion? (y/n) > ", color='white', attrs='bold')).lower()
point_growth_choice = input(Output.colored("[~] Do you want to see the point growth graph upon completion? (y/n) > ", color='white', attrs='bold')).lower()
print("")

#Decide who is serving first (player 0 or 1)
serving = random.randint(0, 1)
# print("Player", serving, "serving first")
Output.print("[*] Player " + str(serving) + " wins the toss", color='blue', attrs='bold')
Output.print(f"[+] Player {serving} will serve first", color='green', attrs='bold')
     
def PointWinner(serving, P0FS, P0FSW, P0SS, P0SSW, P1FS, P1FSW, P1SS, P1SSW):
    """The function takes the current server as a parameter and returns the winner of the point."""
    # Initialize counts for first and second serve attempts and wins
    serve_stats = {
        'Player 0': {'first': {'attempts': 0, 'wins': 0}, 
                     'second': {'attempts': 0, 'wins': 0}, 
                     'faults': 0},
        'Player 1': {'first': {'attempts': 0, 'wins': 0}, 
                     'second': {'attempts': 0, 'wins': 0}, 
                     'faults': 0}
    }
    
    if serving == 0:
        if random.random() < P0FS:
            serve_stats['Player 0']['first']['attempts'] += 1 # Increment first serve count for Player 0
            if random.random() < P0FSW:
                serve_stats['Player 0']['first']['wins'] += 1 # Increment first serve win count for Player 0
                return 0, 'first', serve_stats  # Player 0 wins on first serve
            else:
                return 1, 'opponent', serve_stats  # Player 1 wins, but not on their serve
        else:
            if random.random() < P0SS:
                serve_stats['Player 0']['second']['attempts'] += 1  # Increment second serve count for Player 0
                if random.random() < P0SSW:
                    serve_stats['Player 0']['second']['wins'] += 1 # Increment second serve win count for Player 0
                    return 0, 'second', serve_stats  # Player 0 wins on second serve
                else:
                    return 1, 'opponent', serve_stats  # Player 1 wins, but not on their serve
            else:
                serve_stats['Player 0']['faults'] += 1
                return 1, 'fault', serve_stats  # Player 0 double faults
    else:
        if random.random() < P1FS:
            serve_stats['Player 1']['first']['attempts'] += 1  # Increment first serve count for Player 1
            if random.random() < P1FSW:
                serve_stats['Player 1']['first']['wins'] += 1 # Increment first serve win count for Player 1
                return 1, 'first', serve_stats  # Player 1 wins on first serve
            else:
                return 0, 'opponent', serve_stats  # Player 0 wins, but not on their serve
        else:
            if random.random() < P1SS:
                serve_stats['Player 1']['second']['attempts'] += 1  # Increment second serve count for Player 1
                if random.random() < P1SSW:
                    serve_stats['Player 1']['second']['wins'] += 1 # Increment second serve win count for Player 1
                    return 1, 'second', serve_stats  # Player 1 wins on second serve
                else:
                    return 0, 'opponent', serve_stats  # Player 0 wins, but not on their serve
            else:
                serve_stats['Player 1']['faults'] += 1 # Increment double fault count for Player 1
                return 0, 'fault', serve_stats  # Player 1 double faults

def PlayGame(serving, P0FS, P0FSW, P0SS, P0SSW, P1FS, P1FSW, P1SS, P1SSW, livematch):
    """The function simulates a game (with the same player serving throughout) and determines the winner.
    """
    # Initialize the scores for both players in a dictionary with the names of the players as keys
    score = {"Player 0": 0, "Player 1": 0}
    
    # List to track scores per point for both players
    point_scores = {"Player 0": [], "Player 1": []}
    
    # Initialize a counter for the number of points played
    point_count = 0
    
    # Initialize serve count tracking
    serve_counts = {
        'Player 0': {'first': {'attempts': 0, 'wins': 0}, 'second': {'attempts': 0, 'wins': 0}, 'faults': 0},
        'Player 1': {'first': {'attempts': 0, 'wins': 0}, 'second': {'attempts': 0, 'wins': 0}, 'faults': 0}
    }
    
    if livematch:
        print(f"")
        if serving == 0:
            Output.print(f"[+] Player {serving} serving.", color='197', attrs='bold')
        else:
            Output.print(f"[+] Player {serving} serving.", color='12', attrs='bold')
        
    # Continue playing the game until one player wins
    while True:
        # Determine the winner of the point
        winner, serve_type, new_serve_counts = PointWinner(serving, P0FS, P0FSW, P0SS, P0SSW, P1FS, P1FSW, P1SS, P1SSW)
        
        # Increment the score of the winner
        score["Player " + str(winner)] += 1
        
        # Increment the point count
        point_count += 1
        
        # Aggregate serve count updates
        for player in ['Player 0', 'Player 1']:
            for serve in ['first', 'second']:
                serve_counts[player][serve]['attempts'] += new_serve_counts[player][serve]['attempts']
                serve_counts[player][serve]['wins'] += new_serve_counts[player][serve]['wins']    
            serve_counts[player]['faults'] += new_serve_counts[player]['faults']
            
        point_scores['Player 0'].append(score['Player 0'])
        point_scores['Player 1'].append(score['Player 1'])
        
        # Print the outcome of the current point
        if livematch:
            Output.print_full_point_lable(str(point_count), str(winner), dict(score))
        
        # If the winner has won 4 or more points and has 2 more points than the opponent, the game is over
        if score["Player " + str(winner)] >= 4 and score["Player " + str(winner)] - score["Player " + str(1-winner)] >= 2:
            service_game_win = 1 if winner == serving else 0
            return winner, service_game_win, point_count, score, serve_counts, point_scores

def PlaySet(serving, P0FS, P0FSW, P0SS, P0SSW, P1FS, P1FSW, P1SS, P1SSW, livematch):
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
    
    # Track point scores for each player
    all_point_scores = {"Player 0": [], "Player 1": []}
    
    # Initialize a counter for the number of games played
    game_count = 0
    
    # Track game wins over time for plotting
    game_wins = {"Player 0": 0, "Player 1": 0}
    
    # Track service game wins over time for plotting
    service_games_won = {"Player 0": 0, "Player 1": 0}
    
    # Track total points played in the set
    set_total_points = 0
    
    # Track total player points
    set_player_points = {"Player 0": 0, "Player 1": 0}
    
    # Track serve counts for each player
    set_serve_counts = {'Player 0': {'first': {'attempts': 0, 'wins': 0}, 'second': {'attempts': 0, 'wins': 0}, 'faults': 0},
                        'Player 1': {'first': {'attempts': 0, 'wins': 0}, 'second': {'attempts': 0, 'wins': 0}, 'faults': 0}}
    
    # Continue playing the set until one player wins 6 or more games and has 2 more games than the opponent
    while True:
        # Determine the winner of the game
        game_winner, service_game_win, point_count, player_point_score, game_serve_counts, game_point_scores = PlayGame(serving, P0FS, P0FSW, P0SS, P0SSW, P1FS, P1FSW, P1SS, P1SSW, livematch)
        
        # Increment the score of the game_winner
        score["Player " + str(game_winner)] += 1
        
        # Increment the service game count for the game_winner
        service_games_won["Player " + str(serving)] += service_game_win
        
        # Increment the game count
        game_count += 1
        
        # Print the outcome of the current game
        if livematch:
            print(f"+{'-'*76}+")
            print(f"Game {game_count}: Player {game_winner} wins the game. Current game wins - Player 0: {score['Player 0']}, Player 1: {score['Player 1']}")
            # print("")

        # Accumulate game wins over time
        game_wins["Player " + str(game_winner)] += 1
        
        # Accumulate total points played in the set
        set_total_points += point_count
        
        # Accumulate total player points in the set
        for player in ['Player 0', 'Player 1']:
            set_player_points[player] += player_point_score[player]
            all_point_scores[player].extend(game_point_scores[player])
 
        # Update aggregate serve counts
        for player in ['Player 0', 'Player 1']:
            for serve in ['first', 'second']:
                set_serve_counts[player][serve]['attempts'] += game_serve_counts[player][serve]['attempts']
                set_serve_counts[player][serve]['wins'] += game_serve_counts[player][serve]['wins']
            set_serve_counts[player]['faults'] += game_serve_counts[player]['faults']
        
        # If the game_winner has won 6 or more games and has 2 more games than the opponent, the set is over
        if score["Player " + str(game_winner)] >= 6 and score["Player " + str(game_winner)] - score["Player " + str(1-game_winner)] >= 2:
            return game_winner, game_wins, service_games_won, game_count, set_total_points, set_player_points, set_serve_counts, all_point_scores
        
        # Switch the server for the next game
        serving = 1 - serving
 
def PlayMatch():
    """The function simulates an entire match and determines the winner.
    """
    # Initialize the scores for both players in a dictionary with the names of the players as keys
    score = {"Player 0": 0, "Player 1": 0}
    
    # Initialize a counter for the number of sets played
    set_count = 0
    
    # Track total points scored by each player
    total_tracked_points = {"Player 0": [], "Player 1": []}
    
    # Track set wins over time 
    set_wins = {"Player 0": [], "Player 1": []}
    
    # Track total service games wins over time 
    total_service_games_won = {"Player 0": 0, "Player 1": 0}
    
    # Track total game wins over time
    total_game_wins = {"Player 0": 0, "Player 1": 0}
    
    # Track total games played
    total_game_count = 0
    
    # Track total points played in the match
    total_point_count = 0
    
    # Track total player points
    total_player_points = {"Player 0": 0, "Player 1": 0}
    
    # Track total serve counts
    total_serve_counts = {'Player 0': {'first': {'attempts': 0, 'wins': 0}, 'second': {'attempts': 0, 'wins': 0}, 'faults': 0},
                        'Player 1': {'first': {'attempts': 0, 'wins': 0}, 'second': {'attempts': 0, 'wins': 0}, 'faults': 0}}
    
    # Continue playing the match until one player wins 3 sets
    while True:
        # Determine the winner of the set
        set_winner, game_wins, service_games_won, game_count, set_total_points, set_player_points, set_serve_counts, match_point_scores = PlaySet(serving, P0FS, P0FSW, P0SS, P0SSW, P1FS, P1FSW, P1SS, P1SSW, livematch)
        
        # Increment the score of the set_winner
        score["Player " + str(set_winner)] += 1
        
        # Increment the set count
        set_count += 1

        # Accumulate total game wins, service games won, game count, total points played and player points  
        for player in ['Player 0', 'Player 1']:
            set_wins[player].append(score[player])
            total_game_wins[player] += game_wins[player]
            total_service_games_won[player] += service_games_won[player]
            total_player_points[player] += set_player_points[player]
            total_tracked_points[player].extend(match_point_scores[player])
        
        total_game_count += game_count
        total_point_count += set_total_points

        # Update aggregate serve counts
        for player in ['Player 0', 'Player 1']:
            for serve_type in ['first', 'second']:
                total_serve_counts[player][serve_type]['attempts'] += set_serve_counts[player][serve_type]['attempts']
                total_serve_counts[player][serve_type]['wins'] += set_serve_counts[player][serve_type]['wins']
            total_serve_counts[player]['faults'] += set_serve_counts[player]['faults']

        # Prepare data for the table output
        data = []
            
        for i in range(2):
            data.append([f"Player {i}", 
                         set_wins["Player " + str(i)][-1], 
                         game_wins["Player " + str(i)],
                         set_player_points["Player " + str(i)]
                         ])    
        
        # Print the table output       
        columns = ["Player", "Current Set Wins", "Set Game Wins", "Set Points Scored"]
        Output.print_title(f"Set {set_count} Winner : Player {set_winner}")
        Output.table(columns, data)
        print("\n")
        
        # If the set_winner has won 3 sets, the match is over
        if score["Player " + str(set_winner)] >= 3:
            # Print the match winner and final scores
            print(f"\nMatch Winner: Player {set_winner}. Final Scored Sets - Player 0: {score['Player 0']}, Player 1: {score['Player 1']}")
            
            Output.print_title(f"Match Winner : Player {set_winner}")
            Output.print_scoreboard(str("Player 0"), str(score['Player 0']), str(score['Player 1']), str("Player 1"))
            print("")
            Output.print_sub_scoreboard(str("Total Points"), str(total_point_count))
            Output.print_sub_scoreboard(str("Total Games "), str(total_game_count))
            Output.print_sub_scoreboard(str("Total Sets  "), str(set_count))
            
            final_data = []
            
            for i in range(2):
                final_data.append([f"Player {i}", 
                                   set_wins["Player " + str(i)][-1], 
                                   total_game_wins["Player " + str(i)], 
                                   total_service_games_won["Player " + str(i)],
                                   total_player_points["Player " + str(i)]])
                
            final_columns = ["Player", "Total Sets Won", "Total Games Won", "Service Games Won", "Total Points Scored"]
            Output.table(final_columns, final_data)
            
            #-----------------------------------------------------------------------------------------------------
            
            # Calculate serve win percentages
            first_serve_win_pct = {}
            second_serve_win_pct = {}
            first_serve_in_pct = {}
            second_serve_in_pct = {}
            serve_win_pct = {}
            
            for player in ['Player 0', 'Player 1']:
                first_attempts = total_serve_counts[player]['first']['attempts']
                first_wins = total_serve_counts[player]['first']['wins']
                second_attempts = total_serve_counts[player]['second']['attempts']
                second_wins = total_serve_counts[player]['second']['wins']
                
                first_serve_win_pct[player] = (first_wins / first_attempts * 100) if first_attempts > 0 else 0
                second_serve_win_pct[player] = (second_wins / second_attempts * 100) if second_attempts > 0 else 0
                
                first_serve_in_pct[player] = (first_attempts / (first_attempts + total_serve_counts[player]['faults']) * 100) if (first_attempts + total_serve_counts[player]['faults']) > 0 else 0
                second_serve_in_pct[player] = (second_attempts / (second_attempts + total_serve_counts[player]['faults']) * 100) if (second_attempts + total_serve_counts[player]['faults']) > 0 else 0

            print("")
            for player in ['Player 0', 'Player 1']:
                if player == 'Player 0':
                    body_color = "197"
                elif player == 'Player 1':
                    body_color = "12"
                
                Output.print_mini_scoreboard(str(player) + (" " * 19) , border_color=body_color, font_color="white")
                Output.print_sub_scoreboard(str("1st Serve Pt Win Percentage"), str(f"{int(first_serve_win_pct[player])}%"), subtitle_highlight="105")
                Output.print_sub_scoreboard(str("2nd Serve Pt Win Percentage"), str(f"{int(second_serve_win_pct[player])}%"), subtitle_highlight="105")
                
                if player == 'Player 0':
                    print("")
                 
            serve_data = []
            
            for i in range(2):
                serve_data.append([f"Player {i}", 
                                total_serve_counts["Player " + str(i)]['first']['attempts'],
                                total_serve_counts["Player " + str(i)]['second']['attempts'],
                                total_serve_counts["Player " + str(i)]['faults']])
                
            serve_columns = ["Player", "Total First Serve Count", "Total Second Serve Count", "Total Double Faults"]
            Output.table(serve_columns, serve_data)
            
            # Output.plot_serve_win_percentages(first_serve_win_pct, second_serve_win_pct)
            # Output.plot_point_growth(total_tracked_points['Player 0'], total_tracked_points['Player 1'])
            
            if serve_win_choice == "y":
                Output.plot_serve_win_percentages(first_serve_win_pct, second_serve_win_pct)
            if point_growth_choice == "y":
                Output.plot_point_growth(total_tracked_points['Player 0'], total_tracked_points['Player 1'])
            
            return set_winner
          
PlayMatch()

print("\nEnd of simulation.")


