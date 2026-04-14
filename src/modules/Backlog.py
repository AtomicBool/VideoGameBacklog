from structs.VideoGame import VideoGame

game_list = []

def add_game(game: VideoGame):
    for index, instance in enumerate(game_list):
        if instance.get_title() == game.get_title():
            game_list[index] = game
            return
    game_list.append(game)

    print("Game Added:")
    print("\t" + str(game))

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
            print(f"[+] game {title} has been removed")
            return
        
    print(f"[!] game {title} not found")