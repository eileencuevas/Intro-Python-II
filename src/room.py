# Implement a class to hold room information. This should have name and
# description attributes.

import textwrap


class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items

    def print_description(self):
        textwrapper = textwrap.TextWrapper(width=80)
        wrapped_description = textwrapper.wrap(text=self.description)
        for line in wrapped_description:
            print(f"{line}\n")

    def print_items_list(self):
        if self.items:
            for item in self.items:
                print(f"{item}")
