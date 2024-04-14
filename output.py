import os
import re
import sys

from matplotlib import pyplot as plt
from colored import *
import prettytable

class Output(object):

    @staticmethod
    def print(string, color=None, highlight=None, attrs=None):
        """Print string with styles"""
        print(Output.colored(string, color, highlight, attrs))


    @staticmethod
    def colored(string, color=None, highlight=None, attrs=None):
        """Apply styles to a given string"""
        # Colors list: https://pypi.org/project/colored/
        return colored.stylize(string, (colored.fg(color) if color else '') + \
                                       (colored.bg(highlight) if highlight else '') + \
                                       (colored.attr(attrs) if attrs else ''))
       
        
    @staticmethod
    def table(columns, data, hrules=True, borders=True):
        """
        Print a table. Supports multi-row cells.
        :param columns: An iterable of column names (strings)
        :param data: An iterable containing the data of the table
        :param hrules: Boolean for horizontal rules
        """
        columns = map(lambda x:Output.colored(x, attrs='bold'), columns)
        table = prettytable.PrettyTable(
            hrules=prettytable.ALL if hrules else prettytable.FRAME, 
            field_names=columns)
        for row in data:
            table.add_row(row)
        table.align = 'l'
        if not borders:
            table.border = False
        print(table)
        
        
    @staticmethod
    def print_title(title: str) -> None:
        title_len = len(title) + 2  # Adding 2 for the spaces around the title
        max_title_len = 63
        rest_len = (max_title_len - title_len) // 2 - 2  # Adjusted for the border characters
        
        title_color = '6'
        border_color = '10'

        print()
        # Top border
        top_border = ' ' * rest_len + '╔' + '═' * (title_len) + '╗'
        Output.print(top_border, color=border_color, attrs='bold')

        # Title row
        title_part = Output.colored(' ' + title + ' ', color=title_color)
        # For the title row, since it combines different colors, print parts separately
        left_border = Output.colored('═' * rest_len + '╣', color=border_color, attrs='bold')
        right_border = Output.colored('╠' + '═' * rest_len, color=border_color, attrs='bold')
        print(left_border + title_part + right_border)

        # Bottom border
        bottom_border = ' ' * rest_len + '╚' + '═' * (title_len) + '╝'
        Output.print(bottom_border, color=border_color, attrs='bold')
        # print()
        
        
    @staticmethod
    def print_scoreboard(player_1: str, player_1_score: str, player_2_score: str, player_2: str) -> None:
        scores_length = len(player_1) + len(player_1_score) + len(player_2_score) + len(player_2) + 11
        max_subtitle_len = 63
        rest_len = (max_subtitle_len - scores_length) // 2 - 2  # Adjusted for the border characters
        
        player_1_color = 'black'
        player_2_color = 'black'
        subtitle_highlight = '226'
        subtool_color = 'black'
        subtool_highlight = 'turquoise_2'
        border_color = '10'
        player_1_highlight = 'green'
        player_2_highlight = 'green'

        player_1_part = Output.colored(' ' + player_1 + ' ', color=player_1_color, highlight=player_1_highlight, attrs='bold')
        player_1_score_part = Output.colored(' ' + player_1_score + ' ', color=subtool_color, highlight=subtool_highlight, attrs='bold')
        player_2_score_part = Output.colored(' ' + player_2_score + ' ', color=subtool_color, highlight=subtool_highlight, attrs='bold')
        player_2_part = Output.colored(' ' + player_2 + ' ', color=player_2_color, highlight=player_2_highlight, attrs='bold')
        
        left_border = Output.colored('═' * rest_len, color=border_color, attrs='bold')
        right_border = Output.colored('═' * rest_len, color=border_color, attrs='bold')
        player_1_connector = Output.colored('▒', color=subtitle_highlight, attrs='bold')
        player_1_score_connector = Output.colored('▒', color=subtool_highlight, attrs='bold')
        player_2_connector = Output.colored('▒', color=subtitle_highlight, attrs='bold')
        player_2_score_connector = Output.colored('▒', color=subtool_highlight, attrs='bold')
        score_connector = Output.colored('░', color=border_color, attrs='bold')
        
        
        print(left_border + player_1_part + player_1_score_connector + player_1_score_part + player_1_score_connector + score_connector + player_2_score_connector + player_2_score_part + player_2_score_connector + player_2_part + right_border)
        
    @staticmethod
    def print_sub_scoreboard(total_game_played: str, total_game_count: str, subtitle_highlight="226") -> None:
        if len(total_game_count) == 1:
            total_game_count = "00" + total_game_count
        elif len(total_game_count) == 2:
            total_game_count = "0" + total_game_count
        
        game_count_length = len(total_game_count)
        max_score_board_len = 6
        score_board_rest_len = (max_score_board_len - game_count_length) // 2
        
        total_game_played_part_color = 'black'
        # subtitle_highlight = '226'
        subtool_color = 'black'
        border_color = '10'
        total_game_played_part_highlight = 'green'

        total_game_played_part = Output.colored(' ' + total_game_played + ' ', color=total_game_played_part_color, highlight=total_game_played_part_highlight, attrs='bold')

        left_border = Output.colored('═' * 15, color=border_color, attrs='bold')
        total_game_played_score_connector = Output.colored('▒', color=subtitle_highlight, attrs='bold')
        total_game_played_part_connector = Output.colored('▒', color=border_color, attrs='bold')
        score_connector = Output.colored('░', color=border_color, attrs='bold')
        
        left_highlight = Output.colored(' ' * score_board_rest_len, highlight=subtitle_highlight, attrs='bold')
        right_highlight = Output.colored(' ' * score_board_rest_len, highlight=subtitle_highlight, attrs='bold')
        score_count_part = Output.colored(total_game_count, color=subtool_color, highlight=subtitle_highlight, attrs='bold')
        final_score_count_part = left_highlight + score_count_part + right_highlight

        print(left_border + total_game_played_part + total_game_played_part_connector + score_connector + total_game_played_score_connector + final_score_count_part + total_game_played_score_connector)
        # print("")
        
    @staticmethod
    def print_mini_scoreboard(label: str, border_color="10", font_color="black") -> None:
        # font_color = 'black'
        # border_color = '10'

        label_part = Output.colored(' ' + label + ' ', color=font_color, highlight=border_color, attrs='bold')
        left_border = Output.colored('═' * 15, color=border_color, attrs='bold')
        
        print(left_border + label_part)
        # print("")
        
    @staticmethod
    def print_point_lable(label: str, border_color="10", font_color="black", attrs=None) -> None:
        # font_color = 'black'
        # border_color = '10'

        label_part = Output.colored(' ' + label + ' ', color=font_color, highlight=border_color)
        
        print(label_part)
        # print("")
        
        
    @staticmethod
    def print_full_point_lable(point_count: str, winner: str, score: dict) -> None:
        # font_color = 'black'
        # border_color = '10'
        
        if winner == "0":
            font_color = '197'
        else:
            font_color = '12'
            
        if len(point_count) == 1:
            point_count = "0" + str(point_count)
        else:
            point_count = str(point_count)
            
        for player, point in score.items():
            if point < 10:
                score[player] = "0" + str(point)
            else:
                score[player] = str(point)    
        

        point_part = Output.colored('Point ' + point_count + ': ', color="green")
        winner_part = Output.colored('Player ' + winner + ' wins the point ', color=font_color)
 
        # current_score_part = Output.colored("Current score - Player 0: ", color="white") + Output.colored(str(score['Player 0']), color="190"), Output.colored("Player 1: ", color="white") + Output.colored(str(score['Player 1']), color="190")
        
        print(point_part + winner_part + Output.colored("| Current score - Player 0: ", color="white") + Output.colored(score['Player 0'], color="190") + ", " + Output.colored("Player 1: ", color="white") + Output.colored(score['Player 1'], color="190"))
        # print("")
    
    @staticmethod
    def plot_serve_win_percentages(first_serve_win_pct, second_serve_win_pct):
        # Extract data for plotting
        categories = ['First Serve Win %', 'Second Serve Win %']
        player0_data = first_serve_win_pct['Player 0'], second_serve_win_pct['Player 0']
        player1_data = first_serve_win_pct['Player 1'], second_serve_win_pct['Player 1']
        
        bar_width = 0.35  # width of the bars
        index = range(len(categories))  # bar positions

        plt.figure(figsize=(8, 6))
        plt.bar(index, player0_data, bar_width, label='Player 0', color='#ABD200', alpha=0.9)
        plt.bar([p + bar_width for p in index], player1_data, bar_width, label='Player 1', color='#F4034D', alpha=0.9)

        plt.xlabel('Serve Type')
        plt.ylabel('Win Percentage')
        plt.title('Serve Win Percentages by Player')
        plt.xticks([p + bar_width / 2 for p in index], categories)
        plt.legend()
        plt.grid(True)
        
        # Set y-axis to have ticks every 10 percentage points
        plt.yticks(range(0, 101, 10))  # Generates ticks from 0 to 100 every 10 units
        
        plt.ylim(0, 100)  # Limit y-axis to 100% for clarity
        plt.show()
        
    @staticmethod
    def plot_point_growth(points_player_0, points_player_1):
        plt.figure(figsize=(13, 8))

        # Function to calculate cumulative points for the player
        def calculate_cumulative_points(points):
            cumulative_points = []
            current_total = 0
            for i, point in enumerate(points):
                if i == 0:
                    # Start with the first point score as the starting cumulative total
                    current_total = point
                else:
                    # Only increment cumulative total if the current point is greater than the last point
                    if point > points[i - 1]:
                        current_total += (point - points[i - 1])
                cumulative_points.append(current_total)
            return cumulative_points

        # Calculate cumulative points for each player
        cumulative_points_0 = calculate_cumulative_points(points_player_0)
        cumulative_points_1 = calculate_cumulative_points(points_player_1)

        # Generate x-axis values as the length of player 0's points or player 1's points
        x_axis_values = [i for i in range(len(cumulative_points_0))]

        # Plotting the data
        plt.plot(x_axis_values, cumulative_points_0, marker='o', linestyle='-', color='#ABD200', label='Player 0', markersize=4)
        plt.plot(x_axis_values, cumulative_points_1, marker='o', linestyle='-', color='#F4034D', label='Player 1', markersize=4)
        
        plt.title('Cumulative Point Growth Over Time')
        plt.xlabel('Total Points Played (Both Players)')
        plt.ylabel('Cumulative Points Scored')
        plt.legend()
        plt.grid(True)
        plt.show()
        