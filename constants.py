import random

BOLD = {
    "BLACK" : f"\033[1;90m",
    "RED": f"\033[1;91m",
    "GREEN": f"\033[1;92m",
    "YELLOW": f"\033[1;93m",
    "BLUE": f"\033[1;94m",
    "PURPLE": f"\033[1;95m",
    "CYAN": f"\033[1;96m",
}

BG = {
    "RED": f"\033[0;101m",
    "GREEN": f"\033[0;102m",
    "YELLOW": f"\033[0;103m",
    "BLUE": f"\033[0;104m",
    "PURPLE": f"\033[0;105m",
    "CYAN": f"\033[0;106m",
}

STORY = {
    "UL_IT_GREEN" : f"\033[1;3;32m"
}

COLOUR_END =  f"\033[0m"

UNDERLINE = {
    "RED" : f"\033[4;31m",
    "GREEN": f"\033[4;32m",
    "YELLOW": f"\033[4;33m",
    "BLUE": f"\033[4;34m",
    "PURPLE": f"\033[4;35m",
    "CYAN": f"\033[4;36m",
    "WHITE": f"\033[1;4;38m",
}

ENEMIES = [

    # Easy
    {
        "Current HP": 1,
        "XP Dropped": 1,
        "Hit chance": 0.3,
        "Name": f"{UNDERLINE['GREEN']}Swarm of Mosquitoes{COLOUR_END}"
    },
    {
        "Current HP": 2,
        "XP Dropped": 3,
        "Hit chance": 0.25,
        "Name": f"{UNDERLINE['GREEN']}Poison Dart Frog{COLOUR_END}"
    },
    {
        "Current HP": 2,
        "XP Dropped": 3,
        "Hit chance": 0.3,
        "Name": f"{UNDERLINE['GREEN']}Jungle Snake{COLOUR_END}"
    },
    {
        "Current HP": 2,
        "XP Dropped": 4,
        "Hit chance": 0.3,
        "Name": f"{UNDERLINE['GREEN']}Piranha Swarm{COLOUR_END}"
    },

    # Medium
    {
        "Current HP": 4,
        "XP Dropped": 7,
        "Hit chance": 0.3,
        "Name": f"{UNDERLINE['PURPLE']}Jungle Panther{COLOUR_END}"
    },
    {
        "Current HP": 3,
        "XP Dropped": 6,
        "Hit chance": 0.35,
        "Name": f"{UNDERLINE['PURPLE']}Giant Anaconda{COLOUR_END}"
    },
    {
        "Current HP": 3,
        "XP Dropped": 7,
        "Hit chance": 0.4,
        "Name": f"{UNDERLINE['PURPLE']}Tribal Hunter{COLOUR_END}"
    },

    # Hard
    {
        "Current HP": 5,
        "XP Dropped": 12,
        "Hit chance": 0.7,
        "Name": f"{UNDERLINE['YELLOW']}Omagua Warrior{COLOUR_END}"
    },
    {
        "Current HP": 6,
        "XP Dropped": 10,
        "Hit chance": 0.5,
        "Name": f"{UNDERLINE['YELLOW']}Giant Caiman{COLOUR_END}"
    },

    #Boss
    # {
    #     "Current HP": 10,
    #     "XP Dropped": 100,
    #     "Hit chance": 0.9,
    #     "Name": f"{UNDERLINE['Red']}Amazon Spirit Guardian{COLOUR_END}"
    # }

]


ENV_DESCRIPTIONS = [
        f"{BOLD["GREEN"]}The dense jungle opens up a little, you can see sun rays trickle in from above.{COLOUR_END}",
        f"{BOLD["GREEN"]}You climb over fallen Ceibo tree and step into shin high mud. {COLOUR_END}",
        f"{BOLD["GREEN"]}This area seems to be quiet. Only an ant eater stumbles through the foliage.{COLOUR_END}",
        f"{BOLD["GREEN"]}You are under a thick jungle canopy, light struggles to reach the forest floor.{COLOUR_END}",
        f"{BOLD["GREEN"]}You push forward through chest high brambles into a small clearing{COLOUR_END}",
        f"{BOLD["GREEN"]}You are standing on a high ridge yet can't see far.{COLOUR_END}"
    ]

