"""
TUI.py
Authors: Team
Date: 2026-04-14
Description: Handles all terminal screen rendering for the Video Game Backlog
             application. Each function clears the screen, prints a prompt,
             and returns the raw user input string.
"""

import os

def main_menu() -> str:
    """
    Display the main menu and return the user's input.

    Returns:
        str: The command entered by the user (e.g. 'p', 'o', 'r', 'q').
    """
    os.system("cls" if os.name == "nt" else "clear")
    print("GameBacklog Tool")
    print("[p] print | [q] save & quit | [o] add/modify a game | [r] remove a game | [ctrl + c] force quit")
    return input(">>> ").strip()

def add_game() -> str:
    """
    Display the add/modify game screen and return the user's input.

    Returns:
        str: The raw input string, or 'q' to return to the main menu.
    """
    os.system("cls" if os.name == "nt" else "clear")
    print("[q] return to main menu | [ctrl + c] force quit")
    print("Format: Title, Hours, Priority, Status, Tags...")
    print("Example: \"Minecraft, 3000.0, 1, STARTED, ADVENTURE, OPENWORLD\"")
    return input(">>> ").strip()

def remove_game() -> str:
    """
    Display the remove game screen and return the user's input.

    Returns:
        str: The game title to remove, or 'q' to return to the main menu.
    """
    os.system("cls" if os.name == "nt" else "clear")
    print("[q] return to main menu | [ctrl + c] force quit")
    print("Format: Title")
    print("Example: \"Minecraft\"")
    return input(">>> ").strip()