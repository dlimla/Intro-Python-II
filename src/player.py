# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []


    def __str__(self):
        return f'name: {self.name}, room:{self.current_room}'

    def get_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                return item
        return None

    def move(self, direction):
        nextRoom = self.current_room.get_room(direction)
        if nextRoom is not None:
            self.current_room = nextRoom
            print("you are currently " + self.current_room.name + " and " + self.current_room.description)
        else:
            print("Cannot go that way choose another")

# new_player = Player("Dan", "outside")

# print(new_player)