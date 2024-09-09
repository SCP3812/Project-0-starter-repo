class Item:
    def __init__(self, name, description, points, actions):
        self.name = name
        self.description = description
        self.points = points
        self.actions = actions
    
    def set_status(self, action, status):
        self.actions[action] = status

