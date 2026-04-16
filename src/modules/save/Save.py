import json, os
from structs.VideoGame import VideoGame

# convert and save dictionary in the json file
def save(games_list: list[VideoGame], save_destination = os.path.join(os.path.dirname(os.path.dirname(__file__)), "../backlog.json")):
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

# load data from the json file
def load(save_destination = os.path.join(os.path.dirname(os.path.dirname(__file__)), "../../backlog.json")):
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
