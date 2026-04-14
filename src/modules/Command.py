"""
Command.py
Authors: Team
Date: 2026-04-14
Description: Handles all user input logic for the Video Game Backlog application.
             Routes main menu commands to the appropriate sub-handlers.
"""

from modules import InputParser, TUI, Backlog

def handle_main_menu(cmd: str):
    """
    Route a main menu command to the appropriate handler.

    Args:
        cmd (str): Command string from the user ('p', 'o', 'r', or 'q').
    """
    if cmd == "p":
        print("list of games")
    elif cmd == "q":
        print("save & quit")
        exit(0)
    elif cmd == "o":
        handle_add_game()
    elif cmd == "r":
        handle_remove_game()
    else:
        print("[!] Invalid Input")

    input("Press any key to continue...")
            
def handle_add_game():
    """
    Show the add/modify game screen in a loop until the user presses 'q'.
    Parses input and adds the game to the backlog.
    """
    while True:
        cmd_add_game = TUI.add_game()

        if cmd_add_game == "q":
            break

        try:
            Backlog.add_game(InputParser.parse_game(cmd_add_game))
        except IndexError:
            print("[!] Invalid Input: Parameters out of Range")
        except ValueError as err:
            print("[!] Invalid Input: " + err)
                    
        input("Press any key to continue...")

def handle_remove_game():
    """
    Show the remove game screen in a loop until the user presses 'q'.
    Removes the matching game from the backlog by title.
    """
    while True:
        cmd_remove_game = TUI.remove_game()
        if cmd_remove_game == "q":
            break

        Backlog.remove_game(cmd_remove_game)
                    
        input("Press any key to continue...")