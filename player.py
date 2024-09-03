class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []

    def pick_up_item(self, item):
        print(f"You picked up {item.name}.")
        self.inventory.append(item)

    #both functions AI-generated