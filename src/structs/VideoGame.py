from structs.Enums import *

class VideoGame:
    _tags = []

    def __init__(self, timeSpent: float, priority: int, status: str, tags: list[str]):
        self.setStatus(status)
        self.setPriority(priority)
        self.setTag(tags)

    # region Regular Getter/Setter
    def setTimeSpent(self, timeSpent: float):
        self._timeSpent = self.validateTimeSpent(timeSpent)

    def validateTimeSpent(self, timeSpent: float) -> float:
        if timeSpent < 0.0: 
            print("[!] Invalid Time Spent, fall back to 0 hrs")
            return 0.0
        return timeSpent 

    def getTimeSpent(self) -> float:
        return self._timeSpent

    def setPriority(self, priority: int):
        self._priority = priority

    def getPriority(self) -> int:
        return self._priority

    # region ENUM Getter/Setter 
    # setter takes string, getter returns string
    def setStatus(self, status: str):
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
    
    def getStatusText(self) -> str:     
        return self._status.name
    
    def setTag(self, tags: list[str]):
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

    def getTagsText(self) -> list[str]:
        result = []
        for tag in self._tags:
            result.append(tag.name)
        return result