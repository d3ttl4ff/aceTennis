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