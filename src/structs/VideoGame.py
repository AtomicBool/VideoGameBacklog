from structs.Enums import VideoGameStatus

class VideoGame:
    def __init__(self, status: str, priority: float = 2000):
        self.setStatus(status)
        self.setPriority(priority)

    def setStatus(self, status: str):
        try: 
            self._status = VideoGameStatus[status]
        except KeyError:
            print("[!] Status should be INTERESTED/STARTED/FINISHED, will fall back to \"INTERESTED\"")
            self._status = VideoGameStatus.STARTED
    
    def getStatusText(self) -> str:
        return self._status.name
    
    def setPriority(self, priority: float):
        self._priority = priority

    def getPriority(self) -> float:
        return self._priority