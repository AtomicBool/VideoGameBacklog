"""
InputParser.py
Authors: Team
Date: 2026-04-14
Description: Parses raw comma-separated user input into VideoGame objects.
"""

from structs.VideoGame import VideoGame

def parse_game(text: str) -> VideoGame:
    """
    Parse a comma-separated string into a VideoGame object.

    Expected format: Title, Hours, Priority, Status, Tags...
    Example: "Minecraft, 3000.0, 1, STARTED, ADVENTURE, OPENWORLD"

    Args:
        text (str): Raw input string from the user.

    Returns:
        VideoGame: A new VideoGame instance populated with the parsed values.
    """
    parts = [x.strip() for x in text.split(",")]
    
    return VideoGame(
        title = parts[0],
        time_spent = float(parts[1]),
        priority = int(parts[2]),
        status = parts[3],
        tags = parts[4:]
    )