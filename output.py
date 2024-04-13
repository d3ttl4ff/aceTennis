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
        subcommand_color = 'turquoise_2'
        subcommand_highlight = '234'
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
    def print_sub_scoreboard(total_game_played: str, total_game_count: str) -> None:
        scores_length = len(total_game_played) + len(total_game_count) + 11
        max_subtitle_len = 63
        rest_len = (max_subtitle_len - scores_length) // 2 - 2  # Adjusted for the border characters
        
        player_1_color = 'black'
        player_2_color = 'black'
        subtitle_highlight = '226'
        subtool_color = 'black'
        subtool_highlight = 'turquoise_2'
        subcommand_color = 'turquoise_2'
        subcommand_highlight = '234'
        border_color = '10'
        total_game_played_part = 'green'
        player_2_highlight = 'green'

        total_game_played_part = Output.colored(' ' + total_game_played + ' ', color=player_1_color, highlight=total_game_played_part, attrs='bold')
        total_game_count_part = Output.colored(' ' + total_game_count + ' ', color=subtool_color, highlight=subtitle_highlight, attrs='bold')

        left_border = Output.colored('═' * 15, color=border_color, attrs='bold')
        # right_border = Output.colored('═' * rest_len, color=border_color, attrs='bold')
        total_game_played_score_connector = Output.colored('▒', color=subtitle_highlight, attrs='bold')
        total_game_played_part_connector = Output.colored('▒', color=border_color, attrs='bold')
        score_connector = Output.colored('░', color=border_color, attrs='bold')

        print(left_border + total_game_played_part + total_game_played_part_connector + score_connector + total_game_played_score_connector + total_game_count_part + total_game_played_score_connector)
        # print("")
      
        
    @staticmethod
    def PlotGameWins(game_wins):
        plt.figure(figsize=(10, 5))
        plt.plot(game_wins["Player 0"], label='Player 0 Game Wins', marker='o')
        plt.plot(game_wins["Player 1"], label='Player 1 Game Wins', marker='o')
        plt.title('Game Wins Over Time')
        plt.xlabel('Game Number')
        plt.ylabel('Total Games Won')
        plt.legend()
        plt.grid(True)
        plt.show() 
        
        