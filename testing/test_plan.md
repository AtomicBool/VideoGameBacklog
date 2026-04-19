# Test Plan

## TestInputParser — Ray

| ID | Function | Type | Input | Expected Output |
|----|----------|------|-------|-----------------|
| IP-1 | `parse_game` | Normal | `"Minecraft, 3000.0, 1, STARTED, ADVENTURE, OPENWORLD"` | title=Minecraft, time=3000.0, priority=1, status=STARTED, tags=[ADVENTURE, OPENWORLD] |
| IP-2 | `parse_game` | Normal | `"Cyberpunk, 100.5, 2, INTERESTED"` (no tags) | tags=[] |
| IP-3 | `parse_game` | Error | status=`"BADSTATUS"` | falls back to INTERESTED |
| IP-4 | `parse_game` | Edge | time=`-5.0` | falls back to 0.0 |
| IP-5 | `parse_game` | Normal | `"Balatro, 50.0, 3, FINISHED, ARCADE"` (one tag) | tags=[ARCADE] |

## TestSave — Peter

| ID | Function | Type | Input | Expected Output |
|----|----------|------|-------|-----------------|
| SV-1 | `save` + `load` | Normal | 2 VideoGame objects | loaded list has 2 items with all fields preserved |
| SV-2 | `load` | Error | path to nonexistent file | returns `[]` |
| SV-3 | `save` + `load` | Edge | empty list | returns `[]` |
| SV-4 | `save` + `load` + `Backlog.load_games` | Normal | 2 games saved then loaded into Backlog | backlog has 2 correct items |
| SV-5 | `parse_game` + `save` + `load` + `Backlog.load_games` | Normal | 3 raw input strings | backlog has 3 items with correct titles and status |

## TestBacklog — Matthew and Steven

| ID | Function | Type | Input | Expected Output |
|----|----------|------|-------|-----------------|
| BL-1 | `add_game` | Normal | add one new game to empty backlog | list length = 1, title matches |
| BL-2 | `add_game` | Normal | add game with same title twice | list length stays 1, entry is updated to new values |
| BL-3 | `remove_game` | Normal | add a game then remove it by title | list length = 0 |
| BL-4 | `remove_game` | Error | remove a title that does not exist | no exception raised, list unchanged |
