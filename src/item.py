class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, player_name):
        print(
            f"{player_name} has taken {self.name}! What a find!")

    def on_drop(self, player_name):
        print(
            f"{player_name} has dropped {self.name} onto the floor. Oh well.")


class LightSource(Item):
    def __init__(self):
        self.name = 'Lamp'
        self.description = 'A bright lamp.'

    def on_drop(self, player_name):
        print(
            f"{player_name} dropped the Lamp, but it's not wise to drop your source of light!")
