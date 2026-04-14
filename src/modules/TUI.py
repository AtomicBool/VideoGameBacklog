import os

def main_menu() -> str:
    os.system("cls" if os.name == "nt" else "clear")
    print("GameBacklog Tool")
    print("[p] print | [q] save & quit | [o] add/modify a game | [ctrl + c] force quit")
    return input(">>> ").strip()

def add_game() -> str:
    os.system("cls" if os.name == "nt" else "clear")
    print("[q] return to main menu | [ctrl + c] force quit")
    print("Format: Title, Hours, Priority, Status, Tags...")
    print("Example: \"Minecraft, 3000.0, 1, STARTED, ADVENTURE, OPENWORLD\"")
    return input(">>> ").strip()