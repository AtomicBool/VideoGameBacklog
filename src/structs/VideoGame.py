"""
VideoGame.py
Authors: Team
Date: 2026-04-14
Description: Defines the VideoGame data class, which stores all information
             about a single game entry in the backlog (title, status,
             priority, time spent, and genre tags).
"""

from structs.Enums import *

class VideoGame:
    """Represents a single video game entry in the backlog."""
    def __init__(self, title: str, time_spent: float, priority: int, status: str, tags: list[str]):
        """
        Initialize a VideoGame instance.

        Args:
            title (str): The name of the game.
            time_spent (float): Hours spent playing (must be >= 0).
            priority (int): Priority rank in the backlog (1 = highest).
            status (str): Play status — 'INTERESTED', 'STARTED', or 'FINISHED'.
            tags (list[str]): List of genre tag strings (invalid tags are ignored).
        """
        self._tags = []
        self.set_title(title)
        self.set_time_spent(time_spent)
        self.set_priority(priority)
        self.set_status(status)
        self.set_tags(tags)

    # region Regular Getter/Setter
    def get_title(self) -> str:
        """Return the game's title."""
        return self._title

    def set_title(self, title: str):
        """Set the game's title."""
        self._title = title

    def set_time_spent(self, time_spent: float):
        """Set hours spent, falling back to 0 if the value is negative."""
        self._time_spent = self._validate_time_spent(time_spent)

    def _validate_time_spent(self, time_spent: float) -> float:
        """Return time_spent if valid (>= 0), otherwise print a warning and return 0.0."""
        if time_spent < 0.0:
            print("[!] Invalid Time Spent, fall back to 0 hrs")
            return 0.0
        return time_spent

    def get_time_spent(self) -> float:
        """Return hours spent playing."""
        return self._time_spent

    def set_priority(self, priority: int):
        """Set the priority rank in the backlog."""
        self._priority = priority

    def get_priority(self) -> int:
        """Return the priority rank in the backlog."""
        return self._priority

    # region ENUM Getter/Setter 
    # setter takes string, getter returns string
    def set_status(self, status: str):
        """
        Parse status (`INTERESTED/STARTED/FINISHED`),  
        fallback to `INTERESTED` if input is wrong
        
        Raises:
            None: THIS WILL NOT RAISE ANY ERROR
        """
        try: 
            self._status = GameStatus[status]
        except KeyError:
            print("[!] Status should be INTERESTED/STARTED/FINISHED, will fall back to \"INTERESTED\"")
            self._status = GameStatus.INTERESTED
    
    def get_status_text(self) -> str:
        """Return the play status as a string (e.g. 'STARTED')."""
        return self._status.name
    
    def set_tags(self, tags: list[str]):
        """
        parse valid tags, invalid tags will be ignored  
        
        Raises:
            None: THIS WILL NOT RAISE ANY ERROR
        """
        for tag in tags:
            try:
                self._tags.append(GameTag[tag])
            except KeyError:
                print(f"[!] Invalid Tag: {tag}")

    def get_tags_text(self) -> list[str]:
        """Return the list of genre tags as strings (e.g. ['ADVENTURE', 'OPENWORLD'])."""
        result = []
        for tag in self._tags:
            result.append(tag.name)
        return result
    
    def __str__(self):
        return (
            f"{self.get_title()}, "
            f"{self.get_time_spent()} Hours, "
            f"{self.get_priority()}, "
            f"{self.get_status_text()}, "
            f"Tags: {self.get_tags_text()}"
        )