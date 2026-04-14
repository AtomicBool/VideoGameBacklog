import os

from modules import InputParser

input_buffer = ""

try:
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("GameBacklog Tool")
        print("[p] print | [q] save & quit | [o] add/modify a game | [ctrl + c] force quit")
        input_buffer = input(">>> ")

        if input_buffer == "p":
            print("list of games")
        elif input_buffer == "q":
            print("save & quit")
            exit(0)
        elif input_buffer == "o":
            print("Format: Title, Hours, Priority, Status, Tags...")
            print("Example: \"Minecraft, 3000.0, 1, STARTED, ADVENTURE, OPENWORLD\"")
            input_buffer = input(">>> ")
            game = InputParser.parse_game(input_buffer)
            print(game)
        else:
            print("[!] Invalid Input")
        
        input("Press any key to continue...")
except KeyboardInterrupt:
    exit(0)