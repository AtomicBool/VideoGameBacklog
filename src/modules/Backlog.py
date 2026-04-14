"""
Backlog.py
Authors: Team
Date: 2026-04-14
Description: Manages the in-memory backlog list of VideoGame objects.
             Supports adding (or replacing) and removing games by title.
"""

from structs.VideoGame import VideoGame

game_list = []

def _print_game(add_info: str, game: VideoGame):
    print(add_info)
    print("\t" + str(game))

def print_games():
    # We need to print in both A-Z order and priority based 
    pass

def add_game(game: VideoGame):
    """
    Add a game to the backlog, or replace it if a game with the same title exists.

    Args:
        game (VideoGame): The game to add or update.
    """
    for index, instance in enumerate(game_list):
        if instance.get_title() == game.get_title():
            game_list[index] = game
            _print_game("[Modified]", game)
            return
    game_list.append(game)
    _print_game("[Added]", game)

def remove_game(title: str):
    """
    Delete a game from the list with given title
    
    Notice that this is not the right way to   
    delete elements from list,  
    but it works because title is unique in this case
    """
    for index, instance in enumerate(game_list):
        if instance.get_title() == title:
            del game_list[index]
            print(f"[Removed] {title}")
            return
        
    print(f"[!] {title} not found")