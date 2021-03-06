"""
SNAKES AND LADDERS
Code Institute PP3
StevenWeir038
December 2021
"""
# Imports

from rules import game_instructions
import random
import os
import time
import colorama
from pyfiglet import Figlet
from termcolor import colored
from colorama import Fore, Style
colorama.init(autoreset=True)


# Classes

class Board():
    """
    Board class
    """
    def __init__(self):
        self.board = board = []
        row = []
        for square in range(100, 0, -1):
            row.append(str(square).zfill(3))
            if (square-1) % 10 == 0:
                board.append(row)
                row = []
        for column in range(10):
            if column % 2:
                board[column].reverse()

    def turn_board(self, position):
        """
        if value player position integer > 100, format square 100
        convert player position from integer to string
        evaluate player position string by looping through board list items
        format the matching list value
        return: None
        """
        str_pos = str(position).zfill(3)
        if position >= 100:
            self.board[0][0] = " 🏁 "

        for x, row in enumerate(self.board):
            for y, col in enumerate(row):
                if col == str_pos:
                    self.board[x][y] = " 📌 "

    def print_board(self):
        for square in self.board:
            print(" | ".join(square))


class Player:
    """
    Player class
    """
    def __init__(self, pawn_color, curr_position=0):
        self.pawn_color = pawn_color
        self.curr_square = curr_position
        self.num_turns = 0


# Snake and Ladder dictionaries to be used in game

SNAKE_HEAD = {
    98: 78, 97: 76, 95: 24, 93: 68, 64: 60, 48: 30, 16: 6
}

LADDER_FOOT = {
    1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100
}


# Menu behaviors

def clear_terminal():
    """
    clear the terminal.
    return: None
    """
    os.system("cls" if os.name == "nt" else "clear")


def sleep(secs):
    '''
    display returned input for defined number of seconds for information to
    be useful to user
    return: None
    '''
    time.sleep(secs)


def menu_return():
    """
    back to main menu
    """
    input(f"\nPress{Fore.BLUE} Enter{Fore.WHITE} to return to menu\n")
    clear_terminal()
    menu_screen()


def print_center(msg):
    """
    center content on console
    """
    print(' ' * ((os.get_terminal_size().columns - len(msg))//2) + msg)


# Menus

def menu_screen():
    """
    Menu
    """
    print(" MENU\n")
    print(f"{Fore.RED}{Style.BRIGHT} 1 "
          f"{Fore.WHITE}{Style.NORMAL}View Rules\n")
    print(f"{Fore.GREEN}{Style.BRIGHT} 2 "
          f"{Fore.WHITE}{Style.NORMAL}View Board\n")
    print(f"{Fore.BLUE}{Style.BRIGHT} 3 {Fore.WHITE}{Style.NORMAL}Play Game\n")
    print(f"{Fore.YELLOW}{Style.BRIGHT} 4 "
          f"{Fore.WHITE}{Style.NORMAL}Quit Application\n")

    try:
        pre_game_choice = int(input(
            f"Select from options "
            f"{Fore.RED}{Style.BRIGHT}1{Fore.WHITE}{Style.NORMAL}, "
            f"{Fore.GREEN}{Style.BRIGHT}2{Fore.WHITE}{Style.NORMAL}, "
            f"{Fore.BLUE}{Style.BRIGHT}3{Fore.WHITE}{Style.NORMAL} or "
            f"{Fore.YELLOW}{Style.BRIGHT}4{Fore.WHITE}{Style.NORMAL}\n"))

        if not input:
            raise ValueError
        elif pre_game_choice == 1:
            view_rules()
        elif pre_game_choice == 2:
            view_board()
        elif pre_game_choice == 3:
            game_setup()
        elif pre_game_choice == 4:
            quit_application()

        else:
            incorrect_value()

    except ValueError:
        print(f'{Fore.RED}Incorrect value submitted.')
        sleep(2)
        clear_terminal()
        menu_screen()


def validate_player_count(player_count):
    """
    parameters: number of players (integer) from game_setup()
    check the players list passed from game_setup()
    is an integer >= 2 and <= 4
    return: True / False to game_setup()
    """
    try:
        if player_count < 2 or player_count > 4:
            raise ValueError
    except ValueError:
        print(
            f"{Fore.RED}You entered {player_count} player(s). Try again...\n")
        return False

    return True


def view_rules():
    '''
    clear terminal
    view Rules (import from rules.py)
    Back to welcome screen
    '''
    clear_terminal()
    print(game_instructions())
    menu_return()


def view_board():
    """
    for use in the menu to show player the board output
    clear terminal
    draw board using Board class
    menu option to go back to welcome screen
    """
    clear_terminal()
    print("\nYour position at the end of each turn is shown by a 📌\n")
    Board().print_board()
    menu_return()


def game_setup():
    """
    clear terminal
    ask user for number of players between 2 - 4 (with error handling)
    call function to validate user input
    apply pawn color to each player,
    P1 = red, P2 = green, P3 = blue, P4 = yellow
    return: 'players' dictionary to snl_game()
    """
    clear_terminal()

    while True:

        try:
            player_count = int(
                input("\nEnter number of players between 2 and 4:\n"))
            if not input:
                raise ValueError

            if validate_player_count(player_count):
                print(f"{Fore.GREEN}\nValid input. Building game for "
                      f"{Fore.WHITE}{player_count}{Fore.GREEN} players...")
                sleep(4)
                clear_terminal()
                player_list = []
                for p in range(1, player_count + 1):
                    if p == 1:
                        player_list.append("Red")
                    elif p == 2:
                        player_list.append("Green")
                    elif p == 3:
                        player_list.append("Blue")
                    else:
                        player_list.append("Yellow")

                players = {pawn_color: Player(
                    pawn_color=pawn_color) for pawn_color in player_list}
                break

        except ValueError:
            print(f"{Fore.RED}\nNo value or text value submitted...\n")

    return snl_game(players)


def incorrect_value():
    '''
    If value entered isn't a number from 1 to 4 throw an error
    '''
    print(f'{Fore.RED}\nIncorrect value submitted.')
    sleep(2)
    clear_terminal()
    menu_screen()


def quit_application():
    """
    confirm if user still wants to quit application
    display message and exit app after a short time
    """
    clear_terminal()
    ans = input("\nAre you sure you want to quit? Y/N\n")
    if ans.lower() in ["y", "yes"]:
        clear_terminal()
        print("\n\n\n\n\n\n\n\n\n")
        print_center("Thanks for playing!")
        sleep(3)
        clear_terminal()
        exit()

    elif ans.lower() in ["n", "no"]:
        clear_terminal()
        menu_screen()

    else:
        quit_application()


# Game

def turn_prompt():
    """
    breakpoint to stop game autorunning
    """
    input(f"\n{Fore.BLUE}ROLL DICE{Fore.WHITE} for next player?\n")


def snl_game(players):
    """
    parameters: 'players' dictionary from game_setup()
    iterate player
    loop through each until win condition met
    return: None
    """
    while True:

        for player_id, player_inst in players.items():
            turn_prompt()

            clear_terminal()

            player_inst.num_turns += 1

            turns = player_inst.num_turns
            turn_msg = f"\n{player_id} TURN {turns}\n"
            print(turn_msg.upper())

            curr_position = player_inst.curr_square
            print(f"You start the turn on square {curr_position}.\n")
            new_position = move(player_id, curr_position)
            player_inst.curr_square = new_position
            print(f"You end the turn on square {new_position}.\n")

            b = Board()
            b.turn_board(new_position)
            b.print_board()
            check_win(player_id, player_inst)


def check_win(player_id, player_inst):
    '''
    evaluate if player has reached or passed 100 to terminate program
    '''
    if player_inst.curr_square >= 100:
        print(f"\n🎈 {player_id} wins! 🎈\n")
        print("GAME OVER...")
        menu_return()


def roll_dice():
    """
    generate number 1-6 using imported randint function and save to variable
    return: roll_num in move()
    """
    roll = random.randint(1, 6)
    return roll


def move(player_id, curr_position):
    """
    parameters: 'player_ID' and 'curr_position' from snl_game()
    For each player move:
    1. get roll value from roll_dice()
    2. move x squares based on roll value.
    3. evaluate if pawn landed on snake, read dict key move to dict value
    4. evaluate if pawn landed on ladder, read dict key move to dict value
    return: None
    """
    roll_num = roll_dice()
    new_position = curr_position + roll_num
    print(f"You rolled a {roll_num}.\n")
    if new_position in SNAKE_HEAD:
        new_position = SNAKE_HEAD[new_position]
        print("Meh, you landed on a 🐍\n")
    elif new_position in LADDER_FOOT:
        new_position = LADDER_FOOT[new_position]
        print("Yay, you landed on a 🖇️\n")
    return new_position


def pre_game():
    """
    Start of the program
    display title
    ask user if they want to view menu screen
    return: None
    """
    clear_terminal()
    title = Figlet(font='small')
    print(colored(title.renderText("     Snakes  & Ladders"), 'yellow'))
    print("\n\n\n\n")
    print_center("PRESS ENTER TO PLAY")
    input("")
    clear_terminal()
    menu_screen()


pre_game()
