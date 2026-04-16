"""
Backlog.py
Authors: Matthew
Date: 2026-04-14
Description: Manages the in-memory backlog list of VideoGame objects.
             Supports adding (or replacing) and removing games by title.
"""

from structs.VideoGame import VideoGame

class Backlog():
    def __init__(self):
        self._game_list: list[VideoGame] = []  

    def load_games(self, games: list[VideoGame]):
        self._game_list.extend(games)

    def get_list(self):
        return self._game_list

    # This function prints all games in the list with numbers
    def print_games(self):  
        if len(self._game_list) == 0:
            print("backlog is empty")   
            return

        i = 1
        for game in self._game_list:
            print("[" + str(i) + "] " + str(game))
            i = i + 1

    def add_game(self, game: VideoGame):   # This function adds a game or replaces it if the title already exists
        for i in range(len(self._game_list)):
            existing = self._game_list[i]

            # Compare titles in lowercase so it ignores uppercase/lowercase differences
            if existing.get_title().lower() == game.get_title().lower():
                self._game_list[i] = game  
                print(game.get_title() + " updated")
                return
        # If no matching title was found, add the game to the list
        self._game_list.append(game)
        print(game.get_title() + " added")

    def remove_game(self, title):   # This function removes a game by its title
        for i in range(len(self._game_list)):
            game = self._game_list[i]

            # Check if the current game's title matches the given title
            if game.get_title().lower() == title.lower():
                self._game_list.pop(i)   
                print(game.get_title() + " removed")
                return
    
        print(title + " not found")
