from modules import Backlog
from modules.save import Save
from modules.ui import Command, TUI

# Load any previously saved backlog
backlog = Backlog()
backlog.load_games(Save.load())

try:
    while True:
        Command.handle_main_menu(TUI.main_menu())
except KeyboardInterrupt:
    exit(0)