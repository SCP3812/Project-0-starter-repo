class Character:
    def __init__(self, name, description, inventory, dialogue):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.dialogue = dialogue
        
    def get_requests(self):
        return self.dialogue

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
    