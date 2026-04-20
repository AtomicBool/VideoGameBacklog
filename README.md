# Video Game Backlog
a course Group Project

<p align="center">
  <a href="https://github.com/AtomicBool/ICS4U_TeamProject/releases"><img src="https://img.shields.io/github/v/release/atomicbool/ICS4U_TeamProject?include_prereleases&style=for-the-badge" alt="GitHub release"></a>
</p>

## Description
A command-line application to track your video game backlog.
It solves the problem that you cant compare your taste of games with STEAM/other platforms

**Features:**
- Add games to your backlog with a priority level (1st, 2nd, 3rd, etc.)
- Track play status for each game: `INTERESTED` / `STARTED` / `FINISHED`
- View your full backlog
- Mark games as started or completed
- Backlog is saved as a `JSON` file and reloaded each time you run the program

## How to Run
* Requires Python 3.10 or later
```bash
git clone https://github.com/AtomicBool/ICS4U_TeamProject.git
cd ICS4U_TeamProject/src
python main.py
```

## Example input/output

**Adding a game:**
```
> 2
Format : Title, Hours, Priority, Status, Tags...
> Minecraft, 3000.0, 1, STARTED, ADVENTURE, OPENWORLD
Minecraft added
```

**Viewing the backlog:**
```
> 1
=== Your Backlog ===
[1] Minecraft, 3000.0 Hours, 1, STARTED, Tags: ['ADVENTURE', 'OPENWORLD']
[2] Balatro, 50.0 Hours, 2, INTERESTED, Tags: ['ARCADE']
```

**Removing a game:**
```
> 3
Enter the title of the game to remove:
> Balatro
Balatro removed
```

Valid values:
- **Status:** `INTERESTED` / `STARTED` / `FINISHED`
- **Tags:** `ADVENTURE`, `ARCADE`, `COMBAT`, `ROGUELIKE`, `OPENWORLD`, `STRATEGY`

# Contributors:
<p align="center">
  <a href="https://github.com/atomicbool"><img src="https://avatars.githubusercontent.com/u/84610772?v=4&size=48" width="48" height="48" alt="atomicbool" title="atomicbool"/></a>
  <a href="https://github.com/liaoborui0-design"><img src="https://avatars.githubusercontent.com/u/231047472?s=400&v=4" width="48" height="48" alt="Steven L - Borui Liao" title="Steven L - Borui Liao"/></a>
  <a href="https://github.com/PeterHo125"><img src="https://avatars.githubusercontent.com/u/274590933?v=4" width="48" height="48" alt="PeterHo125" title="PeterHo125"/></a>
  <a href="https://github.com/wenxianzhong52-jpg"><img src="https://avatars.githubusercontent.com/u/234410479?v=4" width="48" height="48" alt="wenxianzhong52-jpg" title="wenxianzhong52-jpg"/></a>
</p>
