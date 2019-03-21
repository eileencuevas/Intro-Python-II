class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, player_name, room_name):
        print(
            f"{player_name} has taken {self.name} from its home in {room_name}! What a find!")

    def on_drop(self, player_name, room_name):
        print(
            f"{player_name} has dropped {self.name} onto the floor of the {room_name}. Oh well.")
