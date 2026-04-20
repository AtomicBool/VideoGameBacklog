import json, os
from structs.VideoGame import VideoGame

def save(games_list: list[VideoGame], save_destination = os.path.join(os.path.expanduser("~"), "backlog.json")):
    """
    Load game data from a Json file

    Parameters:
        save_destination (string): Location of the file
    
    Returns:
        None
    
    Raises:
        IOError: if the file cannot be read

    Example:
        >>> game = load("backlog.json")
    """
    data = []
    for game in games_list:
        data.append({
            "title": game.get_title(),
            "time_spent": game.get_time_spent(),
            "priority": game.get_priority(),
            "status": game.get_status_text(),
            "tags": game.get_tags_text()
        })
    with open(save_destination, "w") as f:
        json.dump(data, f, indent=2)

def load(save_destination = os.path.join(os.path.expanduser("~"), "backlog.json")):
    """
    Save the game data to a Json file

    Parameters:
        game_list (list[VideoGame]): The list of video game objects
        save_destination (string): Location to save the file
    Returns: 
        None
    
    Raises: 
        IoError: if the file cannot be written or lacking of permissions

    Example:
        >>> save(game, "backlog.json")
    """
    if not os.path.exists(save_destination):
        return []
    with open(save_destination, "r") as f:
        data = json.load(f)
    result = []
    for item in data:
        result.append(VideoGame(
            title=item["title"],
            time_spent=item["time_spent"],
            priority=item["priority"],
            status=item["status"],
            tags=item["tags"]
        ))
    return result
