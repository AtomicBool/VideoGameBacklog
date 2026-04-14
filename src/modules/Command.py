from modules import InputParser, TUI, Backlog

def handle_main_menu(cmd: str):
    if cmd == "p":
        print("list of games")
    elif cmd == "q":
        print("save & quit")
        exit(0)
    elif cmd == "o":
        handle_add_game()
    elif cmd == "r":
        handle_remove_game()
    else:
        print("[!] Invalid Input")

    input("Press any key to continue...")
            
def handle_add_game():
    while True:
        cmd_add_game = TUI.add_game()

        if cmd_add_game == "q":
            break

        #try:
        Backlog.add_game(InputParser.parse_game(cmd_add_game))
        #except:
        #    print("[!] Invalid Input")
                    
        input("Press any key to continue...")

def handle_remove_game():
    while True:
        cmd_remove_game = TUI.remove_game()
        if cmd_remove_game == "q":
            break

        try:
            Backlog.remove_game(cmd_remove_game)
        except:
            print("[!] Invalid Input")
                    
        input("Press any key to continue...")