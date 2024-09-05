class Location:
    def __init__(self, id, name, description, items, characters, exits)
        self.id = id
        self.name = name
        self.description = description
        self.items = items
        self.characters = characters
        self.exits = exits

        def add_item(self, item):
            self.items.append(item)

        def remove_item(self, item):
            self.items.remove(item)

        def add_character(self, character):
            self.characters.append(character)

        def remove_character(self, character):
            self.characters.remove(character)