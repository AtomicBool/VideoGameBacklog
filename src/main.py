from structs.VideoGame import *

test = VideoGame(
    time_spent = 10.0,
    priority = 1,
    status = "STARTED",
    tags= ["ADVENTURE"]
)

print(test.get_status_text())
print(test.get_tags_text())