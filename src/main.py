from modules.ui import Command, TUI

try:
    while True:
        Command.handle_main_menu(TUI.main_menu())
except KeyboardInterrupt:
    exit(0)