import colored
import os

from output import Output

#----------------------------------------------------------------------------------------
subtitle = Output.colored(" SIMPLE MENS' SINGLES TENNIS SIMULATOR ", color='black', highlight='green', attrs='bold')
left_connector = Output.colored('░░░░░░░░░░░░░░░▒▒▒▒▒▓▓▓▓███', color='10', attrs='bold')
right_connector = Output.colored('███▓▓▓▓▒▒▒▒▒░░░░░░░░░░░░░░░', color='10', attrs='bold')

BANNER = colored.stylize("""
   _____ _____ _   _ _   _ _____ _____   _____ ________  ____   _ _      ___ _____ ___________ 
  |_   _|  ___| \ | | \ | |_   _/  ___| /  ___|_   _|  \/  | | | | |    / _ |_   _|  _  | ___ \\
    | | | |__ |  \| |  \| | | | \ `--.  \ `--.  | | | .  . | | | | |   / /_\ \| | | | | | |_/ /
    | | |  __|| . ` | . ` | | |  `--. \  `--. \ | | | |\/| | | | | |   |  _  || | | | | |    / 
    | | | |___| |\  | |\  |_| |_/\__/ / /\__/ /_| |_| |  | | |_| | |___| | | || | \ \_/ | |\ \ 
    \_/ \____/\_| \_\_| \_/\___/\____/  \____/ \___/\_|  |_/\___/\_____\_| |_/\_/  \___/\_| \_|
    
  {left_connector}{subtitle}{right_connector}                                                     
""".format(left_connector=left_connector, subtitle=subtitle, right_connector=right_connector), colored.fg('green') + colored.attr('bold'))