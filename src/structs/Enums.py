from enum import Enum

class GameStatus(Enum):
    INTERESTED = 0
    STARTED = 1
    FINISHED = 2

class GameTag(Enum):
    ADVENTURE = 0   # It Takes Two, Cyberpunk 2077, Portal
    ARCADE = 1      # Brotato, Balatro
    COMBAT = 2      # CS2, Apex Legends
    ROGUELIKE = 3   # Dead Cells, Brotato
    OPENWORLD = 4   # Minecraft, Astroneer, Kerbal Space Program
    STRATEGY = 5    # Red Alert, CIVILIZATION VII 