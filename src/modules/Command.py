from modules import InputParser, TUI

def handle_main_menu(cmd: str):
    if cmd == "p":
        print("list of games")
    elif cmd == "q":
        print("save & quit")
        exit(0)
    elif cmd == "o":
        handle_add_game()

    input("Press any key to continue...")
            
def handle_add_game():
    while True:
        cmd_add_game = TUI.add_game()

        if cmd_add_game == "q":
            break

        try:
            game = InputParser.parse_game(cmd_add_game)
            print(game)
        except:
            print("[!] Invalid Input")
                    
        input("Press any key to continue...")