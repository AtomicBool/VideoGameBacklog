"""
Backlog.py
Authors: Matthew
Date: 2026-04-14
Description: Manages the in-memory backlog list of VideoGame objects.
             Supports adding (or replacing) and removing games by title.
"""

from structs.VideoGame import VideoGame

game_list = []   

def print_games():   # This function prints all games in the list with numbers
    if len(game_list) == 0:
        print("backlog is empty")   
        return

    i = 1
    for game in game_list:
        # Print each game with its position number
        print("[" + str(i) + "] " + str(game))
        i = i + 1



def add_game(game):   # This function adds a game or replaces it if the title already exists
    for i in range(len(game_list)):
        existing = game_list[i]

        # Compare titles in lowercase so it ignores uppercase/lowercase differences
        if existing.get_title().lower() == game.get_title().lower():
            game_list[i] = game  
            print(game.get_title() + " updated")
            return
    # If no matching title was found, add the game to the list
    game_list.append(game)
    print(game.get_title() + " added")
def remove_game(title):   # This function removes a game by its title
    for i in range(len(game_list)):
        game = game_list[i]

        # Check if the current game's title matches the given title
        if game.get_title().lower() == title.lower():
            game_list.pop(i)   
            print(game.get_title() + " removed")
            return
        
 
    print(title + " not found")