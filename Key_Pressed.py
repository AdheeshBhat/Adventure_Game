import pygame
import keyboard
pygame.init()

space_pressed = False
mario_images = ["mario_walking1", "mario_walking2", "mario_walking3"]
added = 0
subtracted = 0
MAX_UP = 15
MAX_DOWN = 30

def mario_jump(systems_dictionary):
    jump_frame_counter = systems_dictionary["movement_dictionary"]["jump_frame_counter"]
    if keyboard.is_pressed("d"):
        systems_dictionary["movement_dictionary"]["move_right"] = True
    
    if keyboard.is_pressed("a"):
        systems_dictionary["movement_dictionary"]["move_left"] = True

    if jump_frame_counter <= MAX_UP and systems_dictionary["movement_dictionary"]["space"] == True:
        systems_dictionary["movement_dictionary"]["mario_object"].y -= 30
        systems_dictionary["movement_dictionary"]["jump"] = True

    elif MAX_DOWN >= jump_frame_counter > MAX_UP:
        systems_dictionary["movement_dictionary"]["mario_object"].y += 30
        systems_dictionary["movement_dictionary"]["jump"] = False

    else:
        systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image# = systems_dictionary["movement_dictionary"]["last_image"]
        
        systems_dictionary["movement_dictionary"]["space"] = False
        systems_dictionary["movement_dictionary"]["jump_frame_counter"] = 0

    return systems_dictionary

def key_Pressed(event, systems_dictionary):
    mario_object = systems_dictionary["movement_dictionary"]["mario_object"]
    if keyboard.is_pressed("space") and systems_dictionary["movement_dictionary"]["space"] == False:
        systems_dictionary["volume_dictionary"]["sound"] = True
        systems_dictionary["movement_dictionary"]["time_since_last_jumped"] = pygame.time.get_ticks()
        systems_dictionary["movement_dictionary"]["space"] = True
        mario_object.image = pygame.transform.flip(systems_dictionary["misc_dictionary"]["mario_jump_image"], True, False)
            
    if keyboard.is_pressed("d"):
        systems_dictionary["movement_dictionary"]["move_right"] = True

    if keyboard.is_pressed("a"):
        systems_dictionary["movement_dictionary"]["move_left"] = True

    if event.type == pygame.MOUSEBUTTONDOWN:
        x,y = pygame.mouse.get_pos()
        #print ("x is " + str(x))
        #print ("y is " + str(y))

        #get to game_screen
        if 650 <= x <= 838 and 150 <= y <= 237 and systems_dictionary["screen_dictionary"]["current_screen"] == systems_dictionary["screen_dictionary"]["main_menu"]:
            systems_dictionary["screen_dictionary"]["current_screen"] = systems_dictionary["screen_dictionary"]["game_screen"]
        
        #get to settings_screen
        elif 600 <= x <= 918 and 350 <= y <= 437 and systems_dictionary["screen_dictionary"]["current_screen"] == systems_dictionary["screen_dictionary"]["main_menu"]:
            systems_dictionary["screen_dictionary"]["current_screen"] = systems_dictionary["screen_dictionary"]["settings_screen"]

        #get to control_screen
        elif 600 <= x <= 922 and 550 <= y <= 636 and systems_dictionary["screen_dictionary"]["current_screen"] == systems_dictionary["screen_dictionary"]["main_menu"]:
            systems_dictionary["screen_dictionary"]["current_screen"] = systems_dictionary["screen_dictionary"]["control_screen"]

        #return to menu
        elif ((25 <= x <= 449 and 25 <= y <= 86) and (systems_dictionary["screen_dictionary"]["current_screen"] == systems_dictionary["screen_dictionary"]["game_screen"])
        or ((25 <= x <= 449 and 25 <= y <= 86) and systems_dictionary["screen_dictionary"]["current_screen"] == systems_dictionary["screen_dictionary"]["settings_screen"])
        or ((25 <= x <= 449 and 25 <= y <= 86) and systems_dictionary["screen_dictionary"]["current_screen"] == systems_dictionary["screen_dictionary"]["control_screen"])):
            systems_dictionary["screen_dictionary"]["current_screen"] = systems_dictionary["screen_dictionary"]["main_menu"]
            systems_dictionary["volume_dictionary"]["volume"] = False
        
        #volume button
        elif 620 <= x <= 915 and 200 <= y <= 284 and systems_dictionary["screen_dictionary"]["current_screen"] == systems_dictionary["screen_dictionary"]["settings_screen"]:
            systems_dictionary["volume_dictionary"]["volume"] = True

        #higher volume button
        elif (480 <= x <= 663 and 300 <= y <= 360) and systems_dictionary["screen_dictionary"]["current_screen"] == systems_dictionary["screen_dictionary"]["settings_screen"]:
            #checks if volume can be changed
            if systems_dictionary["volume_dictionary"]["volume_percentage"] < 100 and systems_dictionary["volume_dictionary"]["volume_percentage"] >= 0:
                systems_dictionary["volume_dictionary"]["volume_percentage"] += 5
                systems_dictionary["volume_dictionary"]["adjust_volume"] += 0.005
                systems_dictionary["volume_dictionary"]["volume_adjusted"] = True


        #lower volume button
        elif (880 <= x <= 1051 and 300 <= y <= 363) and systems_dictionary["screen_dictionary"]["current_screen"] == systems_dictionary["screen_dictionary"]["settings_screen"]:
            #checks if volume can be changed
            if systems_dictionary["volume_dictionary"]["volume_percentage"] > 0 and systems_dictionary["volume_dictionary"]["volume_percentage"] <= 100:
                systems_dictionary["volume_dictionary"]["volume_percentage"] -= 5
                systems_dictionary["volume_dictionary"]["adjust_volume"] -= 0.005
                systems_dictionary["volume_dictionary"]["volume_adjusted"] = True


    return systems_dictionary