from structs.VideoGameStatus import VideoGameStatus

class VideoGame:
    def __init__(self, status: VideoGameStatus):
        self.setStatus(status)

    def setStatus(self, status):
        self._status = self._validateStatus(status)

    def _validateStatus(self, status: VideoGameStatus) -> VideoGameStatus:
        if status.value >= 0 and status.value <= 2:
            return status
        else:
            raise ValueError("[!] Invalid Status, should be [0, 2]")
        
    def getStatus(self) -> str:
        if self._status == VideoGameStatus.INTERESTED: 
            return "INTERESTED"
        elif self._status == VideoGameStatus.STARTED:
            return "STARTED"
        else:
            return "FINISHED"