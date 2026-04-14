from structs.Enums import *

class VideoGame:

    def __init__(self, time_spent: float, priority: int, status: str, tags: list[str]):
        self._tags = []
        self.set_time_spent(time_spent)
        self.set_priority(priority)
        self.set_status(status)
        self.set_tags(tags)

    # region Regular Getter/Setter
    def set_time_spent(self, time_spent: float):
        self._time_spent = self._validate_time_spent(time_spent)

    def _validate_time_spent(self, time_spent: float) -> float:
        if time_spent < 0.0: 
            print("[!] Invalid Time Spent, fall back to 0 hrs")
            return 0.0
        return time_spent 

    def get_time_spent(self) -> float:
        return self._time_spent

    def set_priority(self, priority: int):
        self._priority = priority

    def get_priority(self) -> int:
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
        result = []
        for tag in self._tags:
            result.append(tag.name)
        return result