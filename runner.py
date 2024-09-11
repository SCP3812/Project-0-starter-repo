import json
from location import Location
from item import Item
from character import Character
from player import Player
from puzzle import playPuzzle
from action import Action

with open ('Dialogue.json', 'r') as file:
    dialogue = json.load(file)

therapist = Character("Dr. Soychild", "Your very worst nightmare, the WOKE Therapist, Dr. Soychild. He hates every singular fibre of your being. His entire life has been dedicated to keeping you weak and demoralized, so that the Establishment may remain strong and powerful.", [], dialogue["soychild"])
gamer = Character("Epic Gamer", "An epic gamer, one that has not yet fallen to the WOKE MIND VIRUS. He is like you in many ways, yet, he unfortunately has become infirmed.", [], dialogue["gamer"])
gamer_life = Item("your gamer life", "This is the only thing you have left that hasn't been tainted by the Matrix. It is your lifeblood, your will-to-power, your gamer life; to give it away would be like selling your soul to Woke Satan.", 500)
scene1 = Location("Therapy", "You awake in a bleak white lounging room. Walking corpses of men stand all around you. The windows to the outside world, meatspace, have all been shuttered. Welcome to your new personal gamer Hell.", [], [], ['F'])
#L, R, F, B
scene1.add_item(gamer_life)
scene1.add_character(therapist)
scene1.add_character(gamer)
johnkler = Character("Johnkler", "A man cowers in the corner, holding himself in the fetal position. On his face he wears a cruel farce of clown makeup, a smile painted over his scowling lips. His silently laughs to himself.", [], dialogue["jonkler"])
normal_pills = Item("normal pills", "These pills will make you normal. These pills will make you conform. These pills WILL make you live in a society, and you WILL BE HAPPY.", 1000)
receptionist = Character("Receptionist", "It's a devil wearing the skin of a woman wearing a blindingly white labcoat. She stares into your soul with eyes of pure sadism and wanton contempt. Her smile is slightly too wide for her face. She speaks in a condescending, infantilizing tone. She does not have your best intentions in mind.", [], dialogue["reception"])
scene2 = Location("Pharmacy", "This room is a room of darkness, where liberty and freedom go to die. The gamer's worst nightmare is here - being nerfed - taking normal pills. The workers stand in their red, white, and blue scrubs, staring you down with garish, soulless grins. It is a sterile white, with a counter where the receptionist stands.", [], [], ['B','L'])
scene2.add_item(normal_pills)
scene2.add_character(receptionist)
puzzlebox = Item("puzzlebox", "A small brass cube with differently-shaped holes all over its surface, and a set of various shaped brass fittings to match. Something within it calls to you, as if it can provide freedom.", 900)
scene3 = Location("Backroom", "A crampt, dark, dank room you've managed to get into somehow. It's cold in here. You've gotten the sense that this room was once used as a storage closet... for something.", [], [], ['R'])
scene3.add_item(puzzlebox)
locales = [scene1, scene2]

def gameloop(locations):
    print("Welcome to MonkeyTime PlayFun Time Monkey Game by Games Incorporated")
    player_name =  input("What is your name? ")
    #autocompleted by Claude-3.5
    player = Player(player_name, locations[0])
    print(f"Introduction: You are {player.name}. You are a gamer, and you believe your life is literally a video game. Yet, however, when your mother forced you to go to woke therapy, the therapist said, 'Your life is not a game. It is a nightmare. Your mother constantly worries about your mental health.' Now, he has incarcerated you in one of his dark satanic mills, and you must escape back to your mother and save her from the woke mind virus infecting the world.")
    print(f"You are currently in {player.location.name}.")
    #line autocompleted by Claude-3.5
    print(player.location.description)

    game_end = False
    #autocompleted by Claude-3.5

    while game_end == False:
        if gamer_life in therapist.inventory:
            print("You thank Dr. Soychild for saving you from your video game addiction. Your mother welcomes you back into her home with open arms. God is in his heaven. Everything is normal on Earth.")
            break
            game_end = True
        if normal_pills in receptionist.inventory:
            print("She sits you down, forcefeeding you the pills one by one while cooing and infantilizing you. You feel yourself getting chemically lobotomized, your gamer gland calcifying. You spent the rest of your days in an institution, silently planning your retribution on society.")
            game_end = True
        if normal_pills in jonkler.inventory:
            print("You give Jonkler the normal pills. He hastily opens the bottle and dumps it into his mouth, several pills falling to the ground. He swallows all of them dry, no water. He then, in a fit of uncontrollable rage, attacks the receptionist, mauling her to death.")
            scene2.remove_character(receptionist)
            jonker.inventory.remove(normal_pills)
            #autocompleted by Claude-3.5
        actions = input("What would you like to do next?\n1. Talk to NPCs\n2. Look around for items\n3. Move a Certain Direction\n4. Check Inventory\n")
        if actions == '1':
            input_npc = input(f"which NPC? \n{'\n'.join([str(char.name) for char in player.location.characters])}\n")
            if input_npc in [char.name for char in player.location.characters]:
                for char in player.location.characters:
                    if char.name == input_npc:
                        print(char.description)
                        input_dialogue = input(f"What do you want to say?\n{'\n'.join([str(line) for line in char.dialogue.keys()])}\n")
                        print(f"{char.name}: {char.get_dialogue_response(char.dialogue, input_dialogue)}")
            else:
                print("That NPC does not exist in this room.")
            #autogenerated by Claude-3.5
        elif actions == '2':
            print(f"In this room you see {' , '.join([str(item.name) for item in player.location.items])}.")
            pick_item = input("Would you like to pick up any of these items? ")
            if pick_item == "y":
                input_item = input("Which item?\n")
                if input_item in [item.name for item in player.location.items]:
                    for item in player.location.items:
                        if item.name == input_item:
                            player.add_item(item)
                else:
                    print("There is nothing like that here.")
            else:
                print("You leave the item where it is.")
                #autocompleted by Claude-3.5
        elif actions == '3':
            input_direction = input("Which direction?\nL\nR\nF\nB\n")
            player.move_location(player.location, input_direction, locales)
            print(player.location.description)
        elif actions == '4':
            print(f"You have {len(player.inventory)} items in your inventory.")
            for item in player.inventory:
                print(item.name)
            item_choice = input("You can:\nexamine (item)\ngive (item) to (char)\n")
            examine = "examine"
            give = "give"
            for item in player.inventory:
                if examine in item_choice:
                    print(item.description)
                    #autogenerated by Claude-3.5
                elif give in item_choice:
                    for char in player.location.characters:
                        if char.name in item_choice:
                            char.add_item(item)
                            player.remove_item(item)
                            print(f"You gave {item.name} to {char.name}.")
                            break
                    else:
                        print("That character does not exist in this room.")
                        #autocompleted by Claude-3.5
gameloop(locales)

    
    














