"""
Save.py
Authors: Team
Date: 2026-04-14
Description: Handles saving and loading the backlog to/from a JSON file.
"""

import json
import os

from structs.VideoGame import VideoGame

SAVE_FILE = os.path.join(os.path.dirname(__file__), "../../../../backlog.json")


def save(game_list: list):
    """
    Serialize game_list to JSON and write it to SAVE_FILE.

    Args:
        game_list (list): List of VideoGame objects to persist.
    """
    data = []
    for game in game_list:
        data.append({
            "title": game.get_title(),
            "time_spent": game.get_time_spent(),
            "priority": game.get_priority(),
            "status": game.get_status_text(),
            "tags": game.get_tags_text()
        })
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=2)


def load() -> list:
    """
    Read SAVE_FILE and deserialize it into a list of VideoGame objects.

    Returns:
        list: Loaded VideoGame objects, or an empty list if no save file exists.
    """
    if not os.path.exists(SAVE_FILE):
        return []
    with open(SAVE_FILE, "r") as f:
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
