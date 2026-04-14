import random, time
from constants import BOLD, COLOUR_END, STORY, ENEMIES
from ascii_art import ascii_library


def make_board(rows: int, columns: int) -> dict[tuple[int, int], str]:
    """
    Create the grid containing the game's accessible points and environment information.

    :param rows: a non-zero integer
    :param columns: a non-zero integer
    :precondition: rows must be a non-zero integer
    :precondition: columns must be a non-zero integer
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

    environment_descriptions = [
        f"{BOLD["GREEN"]}You are in an open field filled with long grass and small boulders.{COLOUR_END}",
        f"{BOLD["GREEN"]}You enter a sparsely wooded area, the trees are thin and bushes surround the trail.{COLOUR_END}",
        f"{BOLD["GREEN"]}You are in a arid plane, little vegetation grows here and the wind blows strong.{COLOUR_END}",
        f"{BOLD["GREEN"]}You are under a thick forest canopy, light struggles to reach the forest floor.{COLOUR_END}"
    ]

    for row in rows:
        for column in columns:
            board[(row, column)] = environment_descriptions[random.randint(0, 3)]

    return board


def make_character() -> dict[str, str | int ]:
    """
    Initialize the character stats and info in a dictionary.

    :postcondition: create a dictionary containing character information
    :return: a dictionary containing character stats and information
    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5, 'Name': 'Doris'}
    """
    name = input(f"{BOLD["BLUE"]}Player: What was my name again?\nName: {COLOUR_END}")
    char_info = {
        "X-coordinate": 0,
        "Y-coordinate": 0,
        "Current HP": 5,
        "Name": name,
        "Rank Title": "Soldado",
        "Rank": 1,
        "Experience": 0
    }

    return char_info


def describe_current_location(board: dict[tuple[int,int], str], character: dict[str, str | int]):
    """
    Print the information associated with the character's current location.

    :param board: a dictionary containing the game board information
    :param character: a dictionary containing the character information
    :precondition: board must be a dictionary containing the environment info about each valid game board coordinate
    :precondition: character must be a dictionary containing the character's current X/Y coordinate
    :postcondition: print the environment info about character's current location
    """
    current_character_location = (character["X-coordinate"], character["Y-coordinate"])
    try:
        for location_key in  board:
            if current_character_location == location_key:
                print(board[location_key])
    except KeyError:
        print("Somehow, someway, you've accessed an out of bounds location. Trace your steps back to safety.")


def get_user_choice() -> int:
    """
    Take and process user's choice of direction they wish to travel.

    :postcondition: process user's input against list of acceptable direction inputs
    :return: user's direction choice as an integer
    """
    user_move = ""
    valid_selection = {1,2,3,4}

    while not user_move:
        user_move =  input("Please choose which direction you wish to move:\n(1)North\n(2)East\n(3)South\n(4)West\n"
                           "Move: ")
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
    rank = character["Rank"]
    print(f"{BOLD["RED"]}[IN BATTLE]{COLOUR_END} | {BOLD["BLUE"]}{name} the level {rank} {rank_title}{COLOUR_END} |"
          f" {BOLD["BLUE"]}HP:{health}{COLOUR_END}")


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
                print(f"{BOLD["RED"]}Enemy: Just as I expected, WRONG!{COLOUR_END}")
                print(f"{BOLD["BLUE"]}Player: 'ACK!' {COLOUR_END}{BOLD["RED"]}(-1hp){COLOUR_END}")
            else:
                print(f"{BOLD["PURPLE"]}*Enemy explodes in defeat!*{COLOUR_END}")
                break


def check_if_goal_attained(character: dict[str, str | int]) -> bool:
    """
    Decide if game goal has been achieved.

    :param character: a dictionary containing character information
    :precondition: character must be a dictionary containing character's current x and y coordinates
    :postcondition: correctly decide if the character's current position is in (4, 4)
    :return: True if character is currently in (4,4) otherwise False
    >>> doc_character = {"X-coordinate": 0,"Y-coordinate": 1,"Current HP": 5,"Name": "Doris"}
    >>> check_if_goal_attained(doc_character)
    False
    >>> doc_character = {"X-coordinate": 4,"Y-coordinate": 4,"Current HP": 5,"Name": "Doris"}
    >>> check_if_goal_attained(doc_character)
    True
    """
    if (character["X-coordinate"], character["Y-coordinate"]) == (4, 4):
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
    print(f"{BOLD["GREEN"]}{ascii_library["WELCOME"]}\n{COLOUR_END}")
    if story_chapter == 0:
        skip = False
        while not skip:
            acceptable = ["y","n"]
            skip_choice = input("Skip intro?(Y/N)\n").lower()
            if skip_choice not in acceptable:
                continue
            elif skip_choice == "y":
                skip = True
            else:
                with open("./storyline/start.txt") as file_object:
                    print("")
                    for line in file_object.readlines():
                        print(f"{STORY["UL_IT_GREEN"]}{line}{COLOUR_END}")
                        time.sleep(2)
                skip = True


def game():
    """
    Initialize and start playing the game.
    """
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    begin_narration(0)

    character = make_character()
    achieved_goal = False

    while not achieved_goal and character["Current HP"] > 0:
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            describe_current_location(board, character)
            there_is_a_challenger = check_for_foes()
            if there_is_a_challenger:
                guessing_game(character)
            achieved_goal = check_if_goal_attained(character)
        else:
            print("Alas, you cannot go that way! Try again.")

    if achieved_goal:
        begin_narration(1)
        print(f"{BOLD["GREEN"]}{ascii_library["THE_END"]}")
    else:
        print(f"{BOLD["RED"]}Game over! You ran out of HP.{COLOUR_END}", end="")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
