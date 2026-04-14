"""
Enums.py
Authors: Team
Date: 2026-04-14
Description: Defines shared enumerations used across the Video Game Backlog
             application, including play status and genre tags.
"""

from enum import Enum

class GameStatus(Enum):
    """Represents the play status of a video game in the backlog."""
    INTERESTED = 0
    STARTED = 1
    FINISHED = 2

class GameTag(Enum):
    """Represents genre tags that can be assigned to a video game."""
    ADVENTURE = 0   # It Takes Two, Cyberpunk 2077, Portal
    ARCADE = 1      # Brotato, Balatro
    COMBAT = 2      # CS2, Apex Legends
    ROGUELIKE = 3   # Dead Cells, Brotato
    OPENWORLD = 4   # Minecraft, Astroneer, Kerbal Space Program
    STRATEGY = 5    # Red Alert, CIVILIZATION VII