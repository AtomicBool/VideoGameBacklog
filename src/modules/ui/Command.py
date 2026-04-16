"""
Command.py
Authors: Steven
Date: 2026-04-14
Description: Handles all user input logic for the Video Game Backlog application.
             Routes main menu commands to the appropriate sub-handlers.
"""

import sys

from modules import Backlog
from modules.ui import TUI
from modules.parser import InputParser
from modules.save import Save
from modules.algorithm import Taste

def handle_main_menu(cmd: str):
    """
    Route the main-menu selection to the appropriate handler.

    Args:
        cmd (str): The raw string the user entered at the main menu.
    """
    if cmd == "1":
        handle_print_game()
    elif cmd == "2":
        handle_add_game()
    elif cmd == "3":
        handle_remove_game()
    elif cmd == "4":
        handle_save_quit()
    else:
        print(f'[!] Unknown command: "{cmd}". Enter 1-4.')
        input("Press Enter to continue...")


def handle_print_game():
    """Display the full backlog and wait for the user to press Enter."""
    print()
    print("=== Your Backlog ===")
    Backlog.print_games()
    input("Press Enter to return to menu...")

def handle_add_game():
    """
    Prompt the user for game details, parse them, and add the game to the backlog.
    Loops until valid input is given or the user cancels.
    """
    raw = TUI.add_game()
    if not raw:
        return
    try:
        game = InputParser.parse_game(raw)
        Backlog.add_game(game)
    except (ValueError, IndexError) as e:
        print(f"[!] Could not parse input: {e}")
    input("Press Enter to continue...")


def handle_remove_game():
    """Prompt the user for a title and remove the matching game from the backlog."""
    title = TUI.remove_game()
    if not title:
        return
    Backlog.remove_game(title)
    input("Press Enter to continue...")

def handle_save_quit():
    """Save the backlog to disk and exit the application."""
    Save.save(Backlog.game_list)
    print("[*] Backlog saved. Goodbye!")
    sys.exit(0)

