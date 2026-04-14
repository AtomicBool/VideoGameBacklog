"""
Backlog.py
Authors: Matthew
Date: 2026-04-14
Description: Manages the in-memory backlog list of VideoGame objects.
             Supports adding (or replacing) and removing games by title.
"""

from structs.VideoGame import VideoGame

game_list: list[VideoGame] = []

def _print_game(add_info: str, game: VideoGame):
    """
    Print a single game entry with a leading label.

    Args:
        add_info (str): Label prepended to the line (e.g. an index like "[1]").
        game (VideoGame): The game to display.
    """
    print(f"{add_info} {game}")


def print_games():
    """Print every game in game_list, numbered from 1. Prints a placeholder if empty."""
    if not game_list:
        print("  (backlog is empty)")
        return
    for i, game in enumerate(game_list, start=1):
        _print_game(f"[{i}]", game)


def add_game(game: VideoGame):
    """
    Add game to game_list, replacing any existing entry with the same title.

    Args:
        game (VideoGame): The game to add or replace.
    """
    for i, existing in enumerate(game_list):
        if existing.get_title().lower() == game.get_title().lower():
            game_list[i] = game
            print(f'[*] "{game.get_title()}" updated in backlog.')
            return
    game_list.append(game)
    print(f'[+] "{game.get_title()}" added to backlog.')


def remove_game(title: str):
    """
    Remove the first game whose title matches (case-insensitive).

    Args:
        title (str): Title of the game to remove.
    """
    for i, game in enumerate(game_list):
        if game.get_title().lower() == title.lower():
            game_list.pop(i)
            print(f'[-] "{game.get_title()}" removed from backlog.')
            return
    print(f'[!] "{title}" not found in backlog.')

def generate_taste() -> list[int]:
    taste: list[int] = [0, 0, 0, 0, 0, 0]

    for game in game_list:
        hours_spent = game.get_time_spent()
        tags = game.get_tags()
        for tag in tags:
            taste[tag.value] += hours_spent / len(tags)

    max_val = max(taste)

    # Divede by Zero Case
    if max_val == 0:
        return [0] * 6

    normalized = [
        round(x / max_val * 255)
        for x in taste
    ]

    return normalized