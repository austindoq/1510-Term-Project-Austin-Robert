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
        "XP Dropped": 2,
        "Hit chance": 0.7,
        "stamina": 1,
        "Name": f"{UNDERLINE['GREEN']}Swarm of Mosquitoes{COLOUR_END}"
    },
    {
        "Current HP": 1,
        "XP Dropped": 2,
        "Hit chance": 0.5,
        "stamina": 2,
        "Name": f"{UNDERLINE['GREEN']}Poison Dart Frog{COLOUR_END}"
    },
    {
        "Current HP": 2,
        "XP Dropped": 2,
        "Hit chance": 0.55,
        "stamina": 2,
        "Name": f"{UNDERLINE['GREEN']}Jungle Snake{COLOUR_END}"
    },
    {
        "Current HP": 2,
        "XP Dropped": 2,
        "Hit chance": 0.6,
        "stamina": 3,
        "Name": f"{UNDERLINE['GREEN']}Piranha Swarm{COLOUR_END}"
    },

    # Medium
    {
        "Current HP": 4,
        "XP Dropped": 5,
        "Hit chance": 0.7,
        "stamina": 5,
        "Name": f"{UNDERLINE['PURPLE']}Jungle Panther{COLOUR_END}"
    },
    {
        "Current HP": 3,
        "XP Dropped": 5,
        "Hit chance": 0.65,
        "stamina": 4,
        "Name": f"{UNDERLINE['PURPLE']}Giant Anaconda{COLOUR_END}"
    },
    {
        "Current HP": 3,
        "XP Dropped": 5,
        "Hit chance": 0.8,
        "stamina": 6,
        "Name": f"{UNDERLINE['PURPLE']}Tribal Hunter{COLOUR_END}"
    },

    # Hard
    {
        "Current HP": 7,
        "XP Dropped": 10,
        "Hit chance": 1.0,
        "stamina": 7,
        "Name": f"{UNDERLINE['YELLOW']}Omagua War Chief{COLOUR_END}"
    },
    {
        "Current HP": 8,
        "XP Dropped": 10,
        "Hit chance": 0.9,
        "stamina": 8,
        "Name": f"{UNDERLINE['YELLOW']}Omagua Warrior{COLOUR_END}"
    },
    {
        "Current HP": 10,
        "XP Dropped": 10,
        "Hit chance": 0.6,
        "stamina": 5,
        "Name": f"{UNDERLINE['YELLOW']}Giant Caiman{COLOUR_END}"
    },

    #Boss
    {
        "Current HP": 20,
        "XP Dropped": 100,
        "Hit chance": 2.0,
        "stamina": 15,
        "Name": f"{UNDERLINE['RED']}Amazon Spirit Guardian{COLOUR_END}"
    }

]


ENV_DESCRIPTIONS = [
        f"{BOLD["GREEN"]}The dense jungle opens up a little, you can see sun rays trickle in from above.{COLOUR_END}",
        f"{BOLD["GREEN"]}You climb over fallen Ceibo tree and step into shin high mud. {COLOUR_END}",
        f"{BOLD["GREEN"]}This area seems to be quiet. Only an ant eater stumbles through the foliage.{COLOUR_END}",
        f"{BOLD["GREEN"]}You are under a thick jungle canopy, light struggles to reach the forest floor.{COLOUR_END}",
        f"{BOLD["GREEN"]}You push forward through chest high brambles into a small clearing{COLOUR_END}",
        f"{BOLD["GREEN"]}You are standing on a high ridge yet can't see far.{COLOUR_END}"
    ]

