- struct/VideoGame.py: data-class like class for video game, contains its status/name/priority...

- module/Backlog.py: a class contains `list[VideoGame]` and prints/add/remove/modify elements

- module/Save.py: read+parse/write+save stuff into a JSON file  

- main.py: the main loop, read `games.json` when start  
    [p] to print  
    [o] to add/modify (name, status, prority)  
    [q] to save & quit  