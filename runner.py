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
gamer_life = Item("your gamer life", "This is the only thing you have left that hasn't been tainted by the Matrix. It is your lifeblood, your will-to-power, your gamer life; to give it away would be like selling your soul to Woke Satan.", 5000, [])
scene1 = Location("Therapy", "You awake in a bleak white lounging room. Walking corpses of men stand all around you. The windows to the outside world, meatspace, have all been shuttered. Welcome to your new personal gamer Hell.", [], [], ['F'])
#L, R, F, B
scene1.add_item(gamer_life)
scene1.add_character(therapist)
normal_pills = Item("normal pills", "These pills will make you normal. These pills will make you conform. These pills WILL make you live in a society, and you WILL BE HAPPY.", 1000, [])
receptionist = Character("Receptionist", "It's a devil wearing the skin of a woman wearing a blindingly white labcoat. She stares into your soul with eyes of pure sadism and wanton contempt. Her smile is slightly too wide for her face. She speaks in a condescending, infantilizing tone. She does not have your best intentions in mind.", [], dialogue["reception"])
scene2 = Location("Pharmacy", "This room is a room of darkness, where liberty and freedom go to die. The gamer's worst nightmare is here - being nerfed - taking normal pills. The workers stand in their red, white, and blue scrubs, staring you down with garish, soulless grins. It is a sterile white, with a counter where the receptionist stands.", [], [], ['B','L'])
scene2.add_item(normal_pills)
scene2.add_character(receptionist)
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

    actions = input("What would you like to do next?\n1. Talk to NPCs\n2. Look around for items\n3. Move a Certain Direction\n")
    if actions == '1':
        input_npc = input(f"which NPC? \n{'\n'.join([str(char.name) for char in player.location.characters])}\n")
    elif actions == '2':
        print(f"In this room you see {' , '.join([str(item.name) for item in player.location.items])}.")
    elif actions == '3':
        input_direction = input("Which direction?\nL\nR\nF\nB\n")
        player.move_location(player.location, input_direction, locales)
        print(player.location.description)

    
    














