from room import Room
from player import Player
from item import Item
#Room List
room = {
    'outside':  Room("Outside Cave Entrance",
                """North of you, the cave mount beckons"""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}
#player list
player = {'user1': Player("Azhin")}
#item List
item = {'apple': Item("apple")}
#Room Operations
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['outside'].addItem(item['apple'])
#--------------------------------------------------------------------------------
# Main
# Make a new player object that is currently in the 'outside' room.
# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
# If the user enters "q", quit the game.
#--------------------------------------------------------------------------------
#variable
starter_room = room['outside']
room = starter_room
player = player['user1']
#main_loop
while True:
    #welcome message
    if room == starter_room:
        print(f"Welcome, {player.name}, you have travelled far and ended up near a cave. You stand outside waiting and looking where to go next\n")    
    #loop print
    print(f"You are at the: {room.name}. {room.description}. \n")
    print(f"This room contains {room}\n")
    print(f"Your inventory: {player.inventory}\n")
    #item input
    #really important
    cmd = ' '.join(input("please proceed with the directions north > 'n', south > 's', east > 'e', west > 'w' \n, or 'get itemname'\n Enter command: ").lower().split()).split(" ")
    get_item = cmd[0]
    # drop_item = input("drop item to room with > drop itemname\n")
    if get_item == 'get':
        #dont put print inside object, related to MVC
        room.transferItem(cmd[1], player)   

    #direction 
    if cmd[0] == 'n':
        print("going north \n")
        room = room.n_to
    if cmd[0] == 's':
        print("going south \n")
        room = room.s_to
    if cmd[0] == 'e':
        print("going east \n")
        room = room.e_to
    if cmd[0] == 'w':
        print("going west \n")
        room = room.w_to    
    elif cmd[0] == 'q':
        print("see you later \n")
        quit