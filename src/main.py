from structs.VideoGame import *

test = VideoGame(
    timeSpent = 10.0,
    priority = 1,
    status = "STARTED",
    tags= ["ADVENTURE"]
)

print(test.getStatusText())
print(test.getTagsText())