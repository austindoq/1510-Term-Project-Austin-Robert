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

COLOUR_END =  f"\033[0m"

UNDERLINE = {
    "RED" : f"\033[4;31m",
    "GREEN": f"\033[4;32m",
    "YELLOW": f"\033[4;33m",
    "BLUE": f"\033[4;34m",
    "PURPLE": f"\033[4;35m",
    "CYAN": f"\033[4;36m",
    "WHITE": f"\033[4;37m",
}

STORY = {
    "UL_IT_GREEN" : f"\033[1;3;32m"
}

ENEMIES = {
    "Easy" : {
        "Current HP" : 1,
        "XP Dropped" : 2,
        "Name" : f"{UNDERLINE["GREEN"]}Swarm of Mosquitoes{COLOUR_END}"
    },
    "Medium" : {
        "Current HP" : 2,
        "XP Dropped" : 5,
        "Name" : f"{UNDERLINE["PURPLE"]}Jungle Panther{COLOUR_END}"
    },
    "Hard" : {
        "Current HP" : 3,
        "XP Dropped" : 10,
        "Name" : f"{UNDERLINE["YELLOW"]}Omagua Warrior{COLOUR_END}"
    }
}