from room import Room
from player import Player
from item import Item, LightSource

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.",
                     True,
                     [Item("Pan", "A handy frying pan. Also a handy drying pan!"),
                      Item("Bread", "Looks moldy."),
                      LightSource()]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", False),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", False),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

name = input('What is your name?\n    ')
player = Player(str(name), room["outside"])


def action_handler(action):
    if len(action) > 1:  # support for two words
        if action[0] == 'take':
            player.acquire_item(action[1])
        elif action[0] == 'drop':
            player.leave_item(action[1])
        else:
            print("\nThis command isn't supported! Try another.")
    else:  # action only has one word
        if action[0] == 'items':
            if player.has_item('Lamp') or player.location.is_light:
                player.location.print_items()
            else:
                print(f"You can't see anything!")
        elif action[0] == 'inventory' or action[0] == 'i':
            if player.has_item('Lamp') or player.location.is_light:
                player.check_inventory()
            else:
                print(f"You can't see anything!")
        else:
            player.move_to(action[0])


while True:
    if player.has_item('Lamp') or player.location.is_light:
        print(
            f"\n---{player.name}'s progress---\nCurrent Location: {player.location.name}\n\n")
        player.location.print_description()
        print(f"\nRoom Items: {player.location.return_items_list()}")
    else:
        print(
            f"\n---{player.name}'s progress---\nCurrent Location: Unknown\n\n")
        print(f"It's pitch black! You should find a lamp!")
        player.location.locate_lamp()
        print(f"\nRoom Items: Unknown")
    action = input('What would you like to do?\n    ')
    if action == 'q' or action == 'quit':
        break
    else:
        action_handler(action.split())
