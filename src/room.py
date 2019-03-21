# Implement a class to hold room information. This should have name and
# description attributes.

import textwrap


class Room:
    def __init__(self, name, description, is_light, items=None):
        self.name = name
        self.description = description
        self.is_light = is_light
        if items is not None:
            self.items = items
        else:
            self.items = []

    def print_description(self):
        textwrapper = textwrap.TextWrapper(width=80)
        wrapped_description = textwrapper.wrap(text=self.description)
        for line in wrapped_description:
            print(f"{line}")

    def return_items_list(self):
        if len(self.items) > 0:
            room_items = []
            for item in self.items:
                room_items.append(item.name)
            return room_items
        else:
            return "No items"

    def print_items(self):
        if len(self.items) > 0:
            for item in self.items:
                print(f"\n{item.name}: {item.description}")
        else:
            print("No items")

    def remove_item(self, item):
        self.items.remove(item)

    def add_item(self, item):
        self.items.append(item)

    def locate_lamp(self):
        for item in self.items:
            if item.name == 'Lamp':
                return print(f"You feel as if there is a Lamp nearby...")
        return print(f"You don't think that there's a Lamp nearby...")
