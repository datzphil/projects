# Crafting Game

# Commands
commands = {
    "i": "see inventory",
    "c": "see crafting options",
    "craft [item]": "craft something from inventory",
}

# inventory
items = {
    "flint": 50,

    "grass": 100,
    "hay": 0,

    "tree": 100,
    "log": 0,

    "boulder": 30,
    "rock": 0,
    "pickaxe": 0,
}

# Rules to make new objects
craft = {
    "hay": {"grass": 1},
    "twig": {"sapling": 1}
}
