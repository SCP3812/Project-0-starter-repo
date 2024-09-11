class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []

    def add_item(self, item):
        print(f"You picked up {item.name}.")
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def move_location(self, location, input_dir, available_rooms):

        if input_dir in self.location.exits:
            if input_dir == "L":
                input_dir = "R"
            elif input_dir == "R":
                input_dir = "L"
            elif input_dir == "F":
                input_dir = "B"
            elif input_dir == "B":
                input_dir = "F"
        #inverts input direction to exit direction, makes checking location exits easier
            for room in available_rooms:
                    if input_dir in room.exits:
                        self.location = room
        #checks if input direction is in the closest rooms exit list, and if it is, moves player to that room
        else:
            print("You cannot move anywhere at this current moment.")
            return

                        

                    
                        

    #both functions AI-generated by Claude-3.5