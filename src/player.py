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
        if len(self.items) > 0:
            for item in self.items:
                print(f"\n{item.name}: {item.description}")
        else:
            print(f"No items in inventory!")

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

    def acquire_item(self, item_to_acquire):
        for room_item in self.location.items:
            # uses lower() to account for input variations
            if room_item.name.lower() == item_to_acquire.lower():
                self.location.remove_item(room_item)
                self.items.append(room_item)
                return room_item.on_take(self.name, self.location.name)
        # will only fire if for loop returns nothing
        return print(f"This item does not exist in this room!")

    def leave_item(self, item_to_leave):
        for inventory_item in self.items:
            if inventory_item.name.lower() == item_to_leave.lower():
                self.items.remove(inventory_item)
                self.location.add_item(inventory_item)
                return inventory_item.on_drop(self.name, self.location.name)
        return print(f"You don't have this item in your inventory!")
