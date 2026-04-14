# Video Game Backlog
a course Group Project

<p align="center">
  <a href="https://github.com/AtomicBool/ICS4U_TeamProject/releases"><img src="https://img.shields.io/github/v/release/atomicbool/ICS4U_TeamProject?include_prereleases&style=for-the-badge" alt="GitHub release"></a>
</p>

## Description
A command-line application to manage your video game backlog. You can add games, track their play status (Interested / Started / Finished), set a priority level, log hours spent, and assign genre tags. The backlog is saved to a file so your data is available the next time you run the program.

## How to Run
* Requires Python 3.10 or later
```bash
git clone https://github.com/AtomicBool/ICS4U_TeamProject.git
cd ICS4U_TeamProject/src
python main.py
```

## Example input/output
When the program starts, you will see the main menu:
```
GameBacklog Tool
[p] print | [q] save & quit | [o] add/modify a game | [ctrl + c] force quit
>>>
```

To add a game, press `o` and enter the game details in this format:
```
Format: Title, Hours, Priority, Status, Tags...
>>> Minecraft, 3000.0, 1, STARTED, ADVENTURE, OPENWORLD
```

Output after adding:
```
Minecraft, 3000.0 Hours, 1, STARTED, Tags: ['ADVENTURE', 'OPENWORLD']
```

Valid values:
- **Status:** `INTERESTED` / `STARTED` / `FINISHED`
- **Tags:** `ADVENTURE`, `ARCADE`, `COMBAT`, `ROGUELIKE`, `OPENWORLD`, `STRATEGY`

# Development schedule
see [schedule.docx](./docs/schedule.docx)

# Contribution
check [CONTRIBUTION.md](./docs/CONTRIBUTION.md)  
[TODO List](./docs/tasks.md)

## Contributors:
<p align="center">
  <a href="https://github.com/atomicbool"><img src="https://avatars.githubusercontent.com/u/84610772?v=4&size=48" width="48" height="48" alt="atomicbool" title="atomicbool"/></a>
  <a href="https://github.com/liaoborui0-design"><img src="https://avatars.githubusercontent.com/u/231047472?s=400&v=4" width="48" height="48" alt="Steven L - Borui Liao" title="Steven L - Borui Liao"/></a>
  <a href="https://github.com/PeterHo125"><img src="https://avatars.githubusercontent.com/u/274590933?v=4" width="48" height="48" alt="PeterHo125" title="PeterHo125"/></a>
  <a href="https://github.com/wenxianzhong52-jpg"><img src="https://avatars.githubusercontent.com/u/234410479?v=4" width="48" height="48" alt="wenxianzhong52-jpg" title="wenxianzhong52-jpg"/></a>
</p>
