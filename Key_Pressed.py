import pygame
import keyboard
pygame.init()

space_pressed = False
mario_images = ["mario_walking1", "mario_walking2", "mario_walking3"]
added = 0
subtracted = 0
MAX_UP = 15
MAX_DOWN = 30
Bowser_MAX_UP = 10
Bowser_MAX_DOWN = 20

#Allows mario to jump when space is pressed. He is allowed to jump for a set number of frames 
# and fall down for the same number of frames.
def mario_jump(systems_dictionary):
    jump_frame_counter = systems_dictionary["movement_dictionary"]["jump_frame_counter"]

    #checks how many frames have passed since space was pressed.
    if jump_frame_counter <= MAX_UP and systems_dictionary["movement_dictionary"]["space"] == True:
        systems_dictionary["movement_dictionary"]["mario_object"].y -= 30
        systems_dictionary["movement_dictionary"]["jump"] = True

    #checks number of frames to allow mario to fall back down.
    elif MAX_DOWN >= jump_frame_counter > MAX_UP:
        systems_dictionary["movement_dictionary"]["mario_object"].y += 30
        systems_dictionary["movement_dictionary"]["jump"] = False

    #condition for when mario is not jumping. Sets mario jump image back to walking image. Resets frame counter.
    else:
        if systems_dictionary["movement_dictionary"]["space"] == True:
            systems_dictionary["movement_dictionary"]["mario_object"].image = systems_dictionary["misc_dictionary"]["mario_walking1"]
        systems_dictionary["movement_dictionary"]["space"] = False
        systems_dictionary["misc_dictionary"]["mario_jump_image"] = systems_dictionary["movement_dictionary"]["default_jump_image"]
        systems_dictionary["movement_dictionary"]["jump_frame_counter"] = 0


    return systems_dictionary

#Allows bowser to jump when space is pressed. He is allowed to jump for a set number of frames 
# and fall down for the same number of frames.
def bowser_jump(bowser_systems_dictionary):
    jump_frame_counter = bowser_systems_dictionary["movement_dictionary"]["jump_frame_counter"]

    #checks how many frames have passed since space was pressed.
    if jump_frame_counter <= Bowser_MAX_UP and bowser_systems_dictionary["movement_dictionary"]["space"] == True:
        bowser_systems_dictionary["movement_dictionary"]["bowser_object"].y -= 30
        bowser_systems_dictionary["movement_dictionary"]["jump"] = True

    #checks number of frames to allow mario to fall back down.
    elif Bowser_MAX_DOWN >= jump_frame_counter > Bowser_MAX_UP:
        bowser_systems_dictionary["movement_dictionary"]["bowser_object"].y += 30
        bowser_systems_dictionary["movement_dictionary"]["jump"] = False

    #condition for when mario is not jumping. Sets mario jump image back to walking image. Resets frame counter.
    else:
        if bowser_systems_dictionary["movement_dictionary"]["space"] == True:
            bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = bowser_systems_dictionary["misc_dictionary"]["bowser_walking1"]
        bowser_systems_dictionary["movement_dictionary"]["space"] = False
        bowser_systems_dictionary["misc_dictionary"]["bowser_jump_image"] = bowser_systems_dictionary["movement_dictionary"]["default_jump_image"]
        bowser_systems_dictionary["movement_dictionary"]["jump_frame_counter"] = 0

    return bowser_systems_dictionary

#Keeps track of all keys that have been pressed and allows characters to move/jump.
def key_Pressed(systems_dictionary, bowser_systems_dictionary):
    mario_object = systems_dictionary["movement_dictionary"]["mario_object"]
    bowser_object = bowser_systems_dictionary["movement_dictionary"]["bowser_object"]
    keys = pygame.key.get_pressed()

    #checks if "w" has been pressed and mario is not already jumping.
    if keys[pygame.K_w] and systems_dictionary["movement_dictionary"]["space"] == False:
        systems_dictionary["volume_dictionary"]["sound"] = True
        systems_dictionary["movement_dictionary"]["time_since_last_jumped"] = pygame.time.get_ticks()
        systems_dictionary["movement_dictionary"]["space"] = True

        #checks if mario is moving left and flips jump image
        if systems_dictionary["movement_dictionary"]["move_left"] == True:
            systems_dictionary["movement_dictionary"]["mario_object"].image = pygame.transform.flip(systems_dictionary["movement_dictionary"]["default_jump_image"], True, False)
        
        #checks if mario is moving right and keeps jump image facing right
        else:
            systems_dictionary["movement_dictionary"]["mario_object"].image = systems_dictionary["misc_dictionary"]["mario_jump_image"]

    #checks if "up arrow" has been pressed and bowser is not already jumping.
    if keys[pygame.K_UP] and bowser_systems_dictionary["movement_dictionary"]["space"] == False:
        bowser_systems_dictionary["volume_dictionary"]["sound"] = True
        bowser_systems_dictionary["movement_dictionary"]["time_since_last_jumped"] = pygame.time.get_ticks()
        bowser_systems_dictionary["movement_dictionary"]["space"] = True

        #checks if bowser is moving left and flips jump image
        if bowser_systems_dictionary["movement_dictionary"]["move_left"] == True:
            bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = pygame.transform.flip(bowser_systems_dictionary["movement_dictionary"]["default_jump_image"], True, False)
        
        #checks if bowser is moving right and keeps jump image facing right
        else:
            bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = bowser_systems_dictionary["misc_dictionary"]["bowser_jump_image"]

    #mario move right
    if keys[pygame.K_d]:
        systems_dictionary["movement_dictionary"]["move_right"] = True
        systems_dictionary["movement_dictionary"]["move_left"] = False

    #mario move left
    if keys[pygame.K_a]:
        systems_dictionary["movement_dictionary"]["move_left"] = True
        systems_dictionary["movement_dictionary"]["move_right"] = False

    #bowser move right
    if keys[pygame.K_RIGHT]:
        bowser_systems_dictionary["movement_dictionary"]["move_right"] = True
        bowser_systems_dictionary["movement_dictionary"]["move_left"] = False
    
    #bowser move left
    if keys[pygame.K_LEFT]:
        bowser_systems_dictionary["movement_dictionary"]["move_left"] = True
        bowser_systems_dictionary["movement_dictionary"]["move_right"] = False

    return systems_dictionary, bowser_systems_dictionary