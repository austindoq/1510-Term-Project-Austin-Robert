import random, time
from constants import BOLD, COLOUR_END, STORY, ENEMIES, ENV_DESCRIPTIONS, UNDERLINE
import ascii_art


def make_board(rows: int, columns: int) -> dict[tuple[int, int], str]:
    """
    Create the grid containing the game's accessible points and environment information.

    :param rows: a positive non-zero integer
    :param columns: a positive non-zero integer
    :precondition: rows must be a positive non-zero integer
    :precondition: columns must be a positive non-zero integer
    :return: a dictionary containing all board locations as tuples
    """
    if str(rows).isalpha():
        print(f"Row value must be a number, '{rows}' is not a number.")
        raise ValueError
    elif int(rows) < 1:
        print(f"Row value must be greater than 0, '{rows}' is not greater than 0.")
        raise ValueError

    if str(columns).isalpha():
        print(f"Column value must be a number, '{columns}' is not a number.")
        raise ValueError
    elif int(columns) < 1:
        print(f"Column value must be greater than 0, '{columns}' is not greater than 0.")
        raise ValueError

    board = {}

    rows = list(range(rows))
    columns = list(range(columns))



    for row in rows:
        for column in columns:
            board[(row, column)] = ENV_DESCRIPTIONS[random.randint(0, 5)]

    return board


def make_character() -> dict[str, str | int ]:
    """
    Initialize the character stats and info in a dictionary.

    :postcondition: create a dictionary containing character information
    :return: a dictionary containing character stats and information
    """
    name = input(f"\n{BOLD["BLUE"]}Player: What was my name again?\nName: {COLOUR_END}")
    print("\n")
    char_info = {
        "X-coordinate": 0,
        "Y-coordinate": 0,
        "Current HP": 10,
        "Name": name,
        "Rank Title": "Soldado",
        "Rank": 1,
        "XP": 0,
        "inventory" : {}
    }

    return char_info


def describe_current_location(board: dict[tuple[int,int], str], character: dict[str, str | int], rows: int,
                              columns: int) -> None:
    """
    Print the information associated with the character's current location.

    :param board: a dictionary containing the game board information
    :param character: a dictionary containing the character information
    :param rows: a positive non-zero integer
    :param columns: a positive non-zero integer
    :precondition: board must be a dictionary containing the environment info about each valid game board coordinate
    :precondition: character must be a dictionary containing the character's current X/Y coordinate
    :precondition: rows must be a positive non-zero integer
    :precondition: columns must be a positive non-zero integer
    :postcondition: print the environment info about character's current location
    """
    x_pos, y_pos = character["X-coordinate"], character["Y-coordinate"]
    status = f"{board[(x_pos,y_pos)]}\nGame board:\n"
    for column in range(columns):
        for row in range(rows):
            status += f" {BOLD["BLUE"]}*{COLOUR_END}" if row == x_pos and column == y_pos else " _"
        status += "\n"
    print(status)


def get_user_choice() -> int:
    """
    Take and process user's choice of direction they wish to travel.

    :postcondition: process user's input against list of acceptable direction inputs
    :return: user's direction choice as an integer
    """
    user_move = ""
    valid_selection = {1,2,3,4}

    while not user_move:
        user_move =  input(f"{UNDERLINE["WHITE"]}Please choose which direction you wish to move:"
                           f"{COLOUR_END}\n(1)North\n(2)East\n(3)South\n(4)West\n>> ")
        try:
            user_move = int(user_move)
        except ValueError:
            print(f"You must input 1, 2, 3, or 4 to move in the direction associated with the number. '{user_move}' is "
                  f"not one of these options.")
            user_move = ""
        else:
            if int(user_move) in valid_selection:
                break
            else:
                print(f"You must choose a number from the listed options, you chose '{user_move}' which is not "
                      f"included in the list of options. Please choose again.")
                user_move = ""

    return user_move


def validate_move(board: dict[tuple[int, int], str], character: dict[str, str | int], direction: int) -> bool:
    """
    Validate the user's desired direction to move.

    :param board: a dictionary containing the coordinates of the game
    :param character: a dictionary containing character information
    :param direction: an integer associated with a desired direction of movement
    :precondition: board must be a dictionary containing all valid game coordinates
    :precondition: character must be a dictionary containing the character's current X/Y coordinate
    :precondition: direction must be an integer in the range [1,4]
    :postcondition: decide if user's desired direction of movement is valid
    :return: True if desired_coord is a valid game board coordinate otherwise False
    >>> doc_board = make_board(rows=5,columns=5)
    >>> doc_character = {"X-coordinate": 0,"Y-coordinate": 0,"Current HP": 5,"Name": "Doris"}
    >>> doc_direction = 2
    >>> validate_move(doc_board, doc_character, doc_direction)
    True
    >>> doc_board = make_board(rows=5,columns=5)
    >>> doc_character = {"X-coordinate": 0,"Y-coordinate": 0,"Current HP": 5,"Name": "Doris"}
    >>> doc_direction = 1
    >>> validate_move(doc_board, doc_character, doc_direction)
    False
    """
    north = (character["X-coordinate"],character["Y-coordinate"] - 1)
    east = (character["X-coordinate"] + 1,character["Y-coordinate"])
    south = (character["X-coordinate"],character["Y-coordinate"] + 1)
    west = (character["X-coordinate"] -1,character["Y-coordinate"])

    if direction == 1:
        desired_coord = north
    elif direction == 2:
        desired_coord = east
    elif direction == 3:
        desired_coord = south
    else:
        desired_coord = west

    for location in board.keys():
        if location == desired_coord:
            return True
        else:
            continue
    return False


def move_character(character: dict[str, str | int], direction: int):
    """
    Apply the desired direction of movement to the character's current position.

    :param character: a dictionary containing the character information
    :param direction: an integer associated with a desired direction of movement
    :precondition: character must be a dictionary containing the character's current X/Y coordinate
    :precondition: direction must be an integer in the range [1,4]
    :postcondition: update the character's x or y coordinates to correspond with the user's choice of direction
    >>> doc_character = {"X-coordinate": 0,"Y-coordinate": 0,"Current HP": 5,"Name": "Doris"}
    >>> doc_direction = 2
    >>> move_character(doc_character, doc_direction)
    >>> doc_character["X-coordinate"]
    1
    >>> doc_character["Y-coordinate"]
    0
    >>> doc_character = {"X-coordinate": 0,"Y-coordinate": 0,"Current HP": 5,"Name": "Doris"}
    >>> doc_direction = 3
    >>> move_character(doc_character, doc_direction)
    >>> doc_character["X-coordinate"]
    0
    >>> doc_character["Y-coordinate"]
    1
    """
    if direction == 1:
        character["Y-coordinate"] = character["Y-coordinate"] - 1
    elif direction == 2:
        character["X-coordinate"] = character["X-coordinate"] + 1
    elif direction == 3:
        character["Y-coordinate"] = character["Y-coordinate"] + 1
    else:
        character["X-coordinate"] = character["X-coordinate"] - 1


def check_for_foes() -> bool:
    """
    Check for a %25 chance of an enemy encounter.

    :postcondition: randomly select a number in the range [1,4] inclusive
    :return: True if number rolled is 4 otherwise False
    """
    foe_check = random.randint(1,4)
    if foe_check == 4:
        return True
    else:
        return False


def print_battle_stats(character: dict[str, str | int]):
    """
    Print the battle stats to the console.

    :param character: a dictionary containing character information
    :precondition: character must be a dictionary containing character information
    :postcondition: the relevant stats to the current battle are printed to console
    """
    health = character["Current HP"]
    name = character["Name"]
    rank_title = character["Rank Title"]
    xp = character["XP"]
    print(f"\n│ {BOLD["RED"]}[IN BATTLE]{COLOUR_END} | {BOLD["BLUE"]
    }{name}{COLOUR_END} the {BOLD["BLUE"]}"
    f"{rank_title.title()}{COLOUR_END} | HP:{BOLD["RED"]}{health}{COLOUR_END} | XP:{BOLD["YELLOW"]}{xp}{COLOUR_END} │"
          f"\n| {ENEMIES[character["Rank"]]["Name"]} | HP:{BOLD["RED"]}{ENEMIES[character["Rank"]]["Current HP"]}"
          f"{COLOUR_END} | \n")


def check_if_goal_attained(character: dict[str, str | int], rows: int, columns: int) -> bool:
    """
    Decide if game goal has been achieved.

    :param character: a dictionary containing character information
    :param rows: a positive non-zero integer
    :param columns: a positive non-zero integer
    :precondition: rows must be a positive non-zero integer
    :precondition: columns must be a positive non-zero integer
    :precondition: character must be a dictionary containing character's current x and y coordinates
    :postcondition: correctly decide if the character's current position is in (14, 14)
    :return: True if character is currently in (4,4) otherwise False
    >>> doc_character = {"X-coordinate": 0,"Y-coordinate": 1,"Current HP": 5,"Name": "Doris"}
    >>> check_if_goal_attained(doc_character)
    False
    >>> doc_character = {"X-coordinate": 4,"Y-coordinate": 4,"Current HP": 5,"Name": "Doris"}
    >>> check_if_goal_attained(doc_character)
    True
    """
    if (character["X-coordinate"], character["Y-coordinate"]) == (rows-1, columns-1):
        return True
    else:
        return False


def begin_narration(story_chapter: int) -> None:
    """
    Begin the narration of storyline in the console.

    :param story_chapter: an integer associated with a text file containing story storyline
    :precondition: story_chapter must be an integer associated with a text file containing the storyline
    :postcondition: a specific chapter's storyline is printed to the console
    """
    if story_chapter == 0:
        print(f"{BOLD["GREEN"]}{ascii_art.ascii_start[0]}\n{COLOUR_END}")
        skip = False
        while not skip:
            acceptable = ["y","n"]
            skip_choice = input("Skip intro?(Y/N)\n").lower()
            if skip_choice not in acceptable:
                continue
            elif skip_choice == "y":
                skip = True
            else:
                try:
                    file_object = open("./storyline/start.txt", "r")
                except FileNotFoundError:
                    print("Storyline file missing, please reinstall file.")
                else:
                    for line in file_object.readlines():
                        print(f"{STORY["UL_IT_GREEN"]}{line}{COLOUR_END}")
                        time.sleep(2)
                    file_object.close()
                break

    if story_chapter == 1:
        try:
            file_object = open("./storyline/end.txt", "r")
        except FileNotFoundError:
            print("Storyline file missing, please reinstall file.")
        else:
            for line in file_object.readlines():
                print(f"{STORY["UL_IT_GREEN"]}{line}{COLOUR_END}")
                time.sleep(2)
            file_object.close()


def guessing_game(character:dict[str, str | int]):
    """
    Initiate an integer guessing game with an enemy.

    :param character: a dictionary containing character information
    :precondition: character must be a dictionary containing the character's current HP`
    :postcondition: user will engage in a riveting integer guessing game
    """
    acceptable_guesses = [1,2,3,4,5]
    answer = random.randint(1, 5)

    print(f"{BOLD["YELLOW"]}LOOK! An enemy has decided to challenge you!{COLOUR_END}")
    print(f"{BOLD["RED"]}Enemy: 'Muahaha, looks like you've sauntered right into my trap! The only way to "
          f"escape now is to do the impossible! You must guess an integer from 1 - 5...'{COLOUR_END}")

    while character["Current HP"] > 0 and (character["X-coordinate"], character["Y-coordinate"]) != (14, 14):
        print_battle_stats(character)
        guess = input("Pick an integer from 1 - 5: ")

        try:
            guess = int(guess)
        except ValueError:
            print(f"You must enter a number! '{guess}' is not an integer. Try again.")
        else:
            if guess not in acceptable_guesses or guess != answer:
                character["Current HP"] = character["Current HP"] - 1
                print(f"{BOLD["RED"]}Enemy: Just as I expected, WRONG!{COLOUR_END}\n")
                print(f"{BOLD["BLUE"]}Player: 'ACK!' {COLOUR_END}{BOLD["RED"]}(-1hp){COLOUR_END}")
            else:
                print(f"══════════════════════════════")
                print(f"{BOLD["PURPLE"]}*Enemy explodes in defeat!*{COLOUR_END}")
                apply_reward(character)
                print(f"══════════════════════════════\n")

                break


def apply_reward(character: dict[str, str | int]) -> None:
    """
    Apply gained XP and HP from winning a battle to the player and award level up buffs if certain conditions are met.

    :param character: a dictionary containing character information
    :precondition: character must be a dictionary containing the character's information
    :postcondition: the correct enemy dropped XP reward is applied to the character
    """
    character["XP"] += ENEMIES[character["Rank"]]["XP Dropped"]
    character["Current HP"] += 1
    print(f"{BOLD["GREEN"]}+1 HP{COLOUR_END}")
    print(f"XP Gained: {BOLD["YELLOW"]}{ENEMIES[character["Rank"]]["XP Dropped"]}{COLOUR_END}")
    check_if_level_up(character)


def check_if_level_up(character: dict[str, str | int]) -> None:
    """
    Check if the character has reached an XP level up threshold and reward them accordingly.

    :param character: a dictionary containing character information
    :precondition: character must be a dictionary containing the character's information
    :postcondition: the character dictionary is modified with rewards if the XP level up threshold is met
    """
    if character["XP"] > 5 and character["Rank"] == 1:
        character["Rank"] += 1
        character["Current HP"] += 10
        character["Rank Title"] = "Cabo"
        print(f"\n{BOLD["BLUE"]}{character["Name"]}{COLOUR_END} has levelled up to {BOLD["BLUE"]
        }{character["Rank Title"]}{COLOUR_END}")
        print(f"{BOLD["GREEN"]}+10 HP{COLOUR_END}")
    elif character["XP"] > 15 and character["Rank"] == 2:
        character["Rank"] += 1
        character["Current HP"] += 10
        character["Rank Title"] = "Capitán"
        print(f"\n{BOLD["BLUE"]}{character["Name"]}{COLOUR_END} has levelled up to {BOLD["BLUE"]
        }{character["Rank Title"]}{COLOUR_END}")
        print(f"{BOLD["GREEN"]}+10 HP{COLOUR_END}")


def decide_enemy(character:dict[str, str | int]):
    progress = character["X-coordinate"] + character["Y-coordinate"]
    dangerous = character["X-coordinate"] * character["Y-coordinate"]
    meet_hard = dangerous / 300
    meet_medium = progress / 30
    if random.random() < meet_hard:
        return ENEMIES[random.randint(7,8)]
    elif random.random() < meet_medium:
        return ENEMIES[random.randint(4,6)]
    else:
        return ENEMIES[random.randint(0,3)]


def guessing_game(character:dict[str, str | int]):
    """
    Initiate an integer guessing game with an enemy.

    :param character: a dictionary containing character information
    :precondition: character must be a dictionary containing the character's current HP`
    :postcondition: user will engage in a riveting integer guessing game
    """
    enemy = decide_enemy(character).copy()

    print(f"{BOLD["YELLOW"]}LOOK! An enemy has decided to challenge you!{COLOUR_END}")
    print(f"It is {enemy["Name"]}!")
    print(f"{BOLD["RED"]}Enemy: 'Muahaha, looks like you've sauntered right into my trap! The only way to "
          f"escape now is to do the impossible! Try defend or counter my attack'{COLOUR_END}")

    while (character["Current HP"] > 0 and
           (character["X-coordinate"], character["Y-coordinate"]) != (14, 14)):
        print(f"Enemy HP left:{enemy["Current HP"]}")
        print_battle_stats(character)

        player_choice = input(f"Enemy is trying to attack you!:\n(1) to defense this attack\n(2) to counterattack ")
        try:
            player_choice = int(player_choice)
        except ValueError:
            print(f"You must enter a number! '{player_choice}' is not an integer. Try again.")
        else:
            if player_choice == 2:
                print(f"You make a counter attack and hit the enemy in the first place")
                if enemy["Current HP"] == 1:
                    print(f"{BOLD["PURPLE"]}*Enemy explodes in defeat!*{COLOUR_END}")
                    break
                else: enemy["Current HP"] -= 1
            if random.random() < enemy["Hit chance"]:
                print(f"Enemy's attack head towards you.")
                if player_choice == 1:
                    if random.random() < 0.8:
                        print(f"You successfully defended against the attack.")
                    else:
                        print(f"Enemy break through your defense.")
                        character["Current HP"] -= 1
                else:
                    print(f"You get hit from the expected damage.")
                    character["Current HP"] -= 1
            else:
                print("Enemy's attack miss you.")
    return character


def game():
    """
    Initialize and start playing the game.
    """
    rows = 15
    columns = 15
    board = make_board(rows, columns)
    begin_narration(0)

    character = make_character()
    describe_current_location(board, character, rows, columns)
    achieved_goal = False
    while not achieved_goal and character["Current HP"] > 0:
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            describe_current_location(board, character, rows, columns)
            # ask_user_to_see_stats(character)
            there_is_a_challenger = check_for_foes()
            if there_is_a_challenger:
                guessing_game(character)

            achieved_goal = check_if_goal_attained(character, rows, columns)
        else:
            print("Alas, you cannot go that way! Try again.")

    if achieved_goal:
        begin_narration(1)

    else:
        print(f"{BOLD["RED"]}Game over! You ran out of HP.{COLOUR_END}", end="")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
