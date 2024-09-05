class Character:
    def __init__(self, id, name, description, inventory, dialogue, combat, looking_for, stats):
        self.id = id
        self.name = name
        self.description = description
        self.inventory = inventory
        self.dialogue = dialogue
        self.looking_for = looking_for
        self.stats = stats
        
    def get_requests(self):
        return self.dialogue

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_combat(self):
        return self.combat

    def get_stat(self, stat):
        return self.stats[stat]

    def set_stat(self, stat, value):
        self.stats[stat] = value

    