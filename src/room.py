# Implement a class to hold room information. This should have name and
# description attributes.

import textwrap


class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
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
            for item in self.items:
                return item
        else:
            return "No items"
