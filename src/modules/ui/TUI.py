"""
TUI.py
Authors: Steven
Date: 2026-04-14
Description: Handles all terminal screen rendering for the Video Game Backlog
             application. Each function clears the screen, prints a prompt,
             and returns the raw user input string.
"""

def main_menu() -> str:
    """
    Render the main menu and return the user's choice.

    Returns:
        str: The raw input string entered by the user.
    """
    print("╔══════════════════════════╗")
    print("║   Video Game Backlog     ║")
    print("╠══════════════════════════╣")
    print("║  1. View Backlog         ║")
    print("║  2. Add Game             ║")
    print("║  3. Remove Game          ║")
    print("║  4. Save & Quit          ║")
    print("╚══════════════════════════╝")
    return input("> ").strip()


def add_game() -> str:
    """
    Render the add-game screen and return the user's raw input line.

    Expected format: Title, Hours, Priority, Status, Tags...
    Example: Minecraft, 3000.0, 1, STARTED, ADVENTURE, OPENWORLD

    Returns:
        str: The raw comma-separated input string entered by the user.
    """
    print("=== Add Game ===")
    print("Format : Title, Hours, Priority, Status, Tags...")
    print("Example: Minecraft, 3000.0, 1, STARTED, ADVENTURE, OPENWORLD")
    print()
    print("Status options : INTERESTED | STARTED | FINISHED")
    print("Tag options    : ADVENTURE | ARCADE | COMBAT | ROGUELIKE | OPENWORLD | STRATEGY")
    print()
    return input("> ").strip()


def remove_game() -> str:
    """
    Render the remove-game screen and return the title entered by the user.

    Returns:
        str: The game title string entered by the user.
    """
    print("=== Remove Game ===")
    print("Enter the title of the game to remove:")
    print()
    return input("> ").strip()

