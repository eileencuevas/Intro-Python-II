# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, items=None):
        self.name = name
        self.location = location
        if items is not None:
            self.items = items
        else:
            self.items = []

    def check_inventory(self):
        if len(self.items) == 0:
            print(f"No items in inventory!")
        else:
            for item in self.items:
                print(f"\n{item.name}: {item.description}")

    def move_to(self, direction):
        if direction in ["n", "s", "e", "w"]:
            if direction == "n" and hasattr(self.location, 'n_to'):
                self.location = self.location.n_to
            elif direction == "s" and hasattr(self.location, 's_to'):
                self.location = self.location.s_to
            elif direction == "e" and hasattr(self.location, 'e_to'):
                self.location = self.location.e_to
            elif direction == "w" and hasattr(self.location, 'w_to'):
                self.location = self.location.w_to
            else:
                print(f"\n{self.name} walks into a wall! Try another direction.")
        else:
            print('\nNot a valid direction! Try n, s, e, or w!')
