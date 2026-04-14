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
    pass

def print_games():
    pass

def add_game(game: VideoGame):
   pass


def remove_game(title: str):
    pass

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