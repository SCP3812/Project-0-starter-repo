class Item:
    def __init__(self, name, description, actions, points):
        self.name = name
        self.description = description
        self.actions = actions
    
    def set_status(self, action, status):
        self.actions[action] = status

