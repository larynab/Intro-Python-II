from room import Room

# Declare all the rooms
#fun
room = {
    'outside':  Room("Outside Cave Entrance",
                """North of you, the cave mount beckons"""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
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
#welcome message

#variable
starter_room = room['outside']
room = starter_room
def current_room():
   print("You are currently in Room: %s \n" % (room))

#main_loop
while True:
    if room == starter_room:
        print("Welcome, adventurer, you have travelled far and ended up near a cave. You stand outside waiting and looking where to go next\n")    
    #loop print
    print(f"You are in the: {room.name}. {room.description}. \n")
    #variable
    direction = input("please proceed with the directions north > n, south > s, east > e, west > w \n")

    if direction == 'n':
        print("going north \n")
        room = room.n_to
    if direction == 's':
        print("going south \n")
        room = room.s_to
    if direction == 'e':
        print("going east \n")
        room = room.e_to
    if direction == 'w':
        print("going west \n")
        room = room.w_to    
    elif direction == 'q':
        print("see you later \n")
        quit