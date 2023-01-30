import random
from colorama import init as colorama_init
from colorama import Fore, Back, Style

STYLES = {
        "narrative":{"fore": Fore.LIGHTGREEN_EX,"back":Back.BLACK},
        "pos_result": {"fore": Fore.GREEN, "back":""},
        "neg_result": {"fore": Fore.YELLOW, "back":""},
        "player_hit": {"fore": Fore.LIGHTBLUE_EX, "back":""},
        "enemy_hit": {"fore": Fore.RED, "back": ""},
        "program": {"fore": Fore.LIGHTBLUE_EX, "back":""},
        "misc": {"fore": Fore.LIGHTYELLOW_EX, "back":""},
        "help": {"fore": Fore.YELLOW, "back": ""},
}

colorama_init()


def say(text, style, start_lb=False, end_lb=False):
    if style in STYLES:
        colors = STYLES.get(style)
        # Capitalizing the sentence
        text = text.capitalize()
        # Constructing the string with colors.
        phrase = f"{colors.get('back')}{colors.get('fore')}{text}{Style.RESET_ALL}"
        # If linebreaks need to be printed, then it's printed before the actual phrase.
        if start_lb:
            print("\n")
        print(phrase)
        if end_lb:
            print("\n")
    else:
        print(f"{Fore.RED} Invalid text color style. {Style.RESET_ALL}")


def get_random_key(dictionary) -> str:
    """Select random key from a passed dictionary."""
    keys = list(dictionary)
    rand_key = random.choice(keys)
    return rand_key

def get_random_array_item(array) -> str:
    """ Select random item from array. """
    rand_item = array[random.randint(0, len(array) - 1)]
    return rand_item

# GF categories
enemies = {
    "Minotaur": {"health": 20, "power": 30},
    "Orc": {"health": 15, "power": 8},
    "Goblin": {"health": 5, "power": 5},
    "Dragon": {"health": 60, "power": 25},
    "Bandit": {"health": 12, "powr": 15},
    "Mouse": {"health": 3, "power": 1},
    "Tiger": {"health": 10, "power": 20},
}
enemy_attributes = ["Weak", "Strong"]
room_attributes = ["Damp", "Bright", "Dark", "Creepy", "Scary", "Peaceful"]
enemy_modifiers = ["Angry", "Happy", "Furious", "Old"]
objects = {
    "Boulder": {"lootable": False, "passable": False, "locked": False},
    "Chest": {"lootable": True, "passable": True, "locked": True},
    "Bag": {"lootable": True, "passable": True, "locked": False},
    "Exit": {"lootable": False, "passable": True, "locked": False},
    "Gate": {"lootable": False, "passable": False, "locked": True},
    "Wall": {"lootable": False, "passable": False, "locked": False},
    "Door": {"lootable": False, "passable": True, "locked": False},
}
items = {
    "Sword": {"power": 10, "fits": ["Backpack"]},
    "Axe": {"power": 10, "fits": ["Backpack"]},
    "Hammer": {"power": 10, "fits": ["Backpack"]},
    "WizardStaff": {"power": 10, "fits": ["Backpack"]},
    "Key": {"power": 10, "fits": ["Backpack"]},
    "ScottishKilt": {"power": 10, "fits": ["Backpack", "Legs"]},
    "LeatherSkirt": {"power": 10, "fits": ["Backpack", "Legs"]},
    "VikingHelmet": {"power": 10, "fits": ["Backpack", "Head"]},
    "BaseballCap": {"power": 10, "fits": ["Backpack", "Head"]},
}
item_modifiers = {
    "Sharp": lambda power : 10 + power,
    "Dull": lambda power : power - 8,
    "Broken": lambda power : power - 15,
    "Legendary": lambda power : power * 4,
    "Magical": lambda power : power * 2,
    "Shiny": lambda power : power + 15 ,
    "Fiery": lambda power : power + 20,
    "Mysterious": lambda power : power * 3,
    "Frozen": lambda power : power + 25,
}
locations = ["Backpack", "Head", "Legs"]
room_modifiers = ["Damp", "Bright", "Dark", "Creepy", "Scary", "Peaceful"]
# Used in help command by linearizing these to show what can be said.
command_tree_examples = {
    "Descriptive": ["DescribeEnemy Mouse", "DescribeEnemy (EnemyMod Old Goblin)"],
    "Drop": ["Drop (ItemMod Mysterious ScottishKilt)", "Drop WizardStaff"],
    "Put": ["Put (ItemMod Mysterious ScottishKilt) Legs", "Put ScottishKilt Legs"],
    "Attack": [
        "Attack Minotaur Hammer",
        "Attack (EnemyMod Happy Orc) (ItemMod Mysterious Sword)",
        "Attack (EnemyMod Happy Orc) Hammer",
        "Attack Orc (ItemMod Mysterious Axe)",
    ],
    "Loot": ["Loot Chest"],
    "Move": ["Move Backward", "Move Forward", "Move Left", "Move Right"],
    "Item Query": ["QItemQuery Backpack", "QItemQuery Legs", "QItemQuery Head"],
    "Direction Query": ["QDirectionQuery Infront"],
}
