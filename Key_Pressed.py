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

def mario_jump(systems_dictionary):
    jump_frame_counter = systems_dictionary["movement_dictionary"]["jump_frame_counter"]

    if jump_frame_counter <= MAX_UP and systems_dictionary["movement_dictionary"]["space"] == True:
        systems_dictionary["movement_dictionary"]["mario_object"].y -= 30
        systems_dictionary["movement_dictionary"]["jump"] = True

    elif MAX_DOWN >= jump_frame_counter > MAX_UP:
        systems_dictionary["movement_dictionary"]["mario_object"].y += 30
        systems_dictionary["movement_dictionary"]["jump"] = False

    else:
        if systems_dictionary["movement_dictionary"]["space"] == True:
            systems_dictionary["movement_dictionary"]["mario_object"].image = systems_dictionary["misc_dictionary"]["mario_walking1"]
        systems_dictionary["movement_dictionary"]["space"] = False
        systems_dictionary["movement_dictionary"]["jump_frame_counter"] = 0


    return systems_dictionary

def bowser_jump(bowser_systems_dictionary):
    jump_frame_counter = bowser_systems_dictionary["movement_dictionary"]["jump_frame_counter"]

    if jump_frame_counter <= Bowser_MAX_UP and bowser_systems_dictionary["movement_dictionary"]["space"] == True:
        bowser_systems_dictionary["movement_dictionary"]["bowser_object"].y -= 30
        bowser_systems_dictionary["movement_dictionary"]["jump"] = True

    elif Bowser_MAX_DOWN >= jump_frame_counter > Bowser_MAX_UP:
        bowser_systems_dictionary["movement_dictionary"]["bowser_object"].y += 30
        bowser_systems_dictionary["movement_dictionary"]["jump"] = False

    else:
        if bowser_systems_dictionary["movement_dictionary"]["space"] == True:
            bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = bowser_systems_dictionary["misc_dictionary"]["bowser_walking1"]
        bowser_systems_dictionary["movement_dictionary"]["space"] = False
        bowser_systems_dictionary["movement_dictionary"]["jump_frame_counter"] = 0

    return bowser_systems_dictionary

def key_Pressed(systems_dictionary, bowser_systems_dictionary):
    mario_object = systems_dictionary["movement_dictionary"]["mario_object"]
    bowser_object = bowser_systems_dictionary["movement_dictionary"]["bowser_object"]
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and systems_dictionary["movement_dictionary"]["space"] == False:
        systems_dictionary["volume_dictionary"]["sound"] = True
        systems_dictionary["movement_dictionary"]["time_since_last_jumped"] = pygame.time.get_ticks()
        systems_dictionary["movement_dictionary"]["space"] = True
        if systems_dictionary["movement_dictionary"]["move_left"] == True:
            systems_dictionary["misc_dictionary"]["mario_jump_image"] = pygame.transform.flip(systems_dictionary["misc_dictionary"]["mario_jump_image"], True, False)
        else:
            systems_dictionary["misc_dictionary"]["mario_jump_image"] = systems_dictionary["misc_dictionary"]["mario_jump_image"]

    if keys[pygame.K_UP] and bowser_systems_dictionary["movement_dictionary"]["space"] == False:
        bowser_systems_dictionary["volume_dictionary"]["sound"] = True
        bowser_systems_dictionary["movement_dictionary"]["time_since_last_jumped"] = pygame.time.get_ticks()
        bowser_systems_dictionary["movement_dictionary"]["space"] = True
        if bowser_systems_dictionary["movement_dictionary"]["move_left"] == True:
            bowser_systems_dictionary["misc_dictionary"]["bowser_jump_image"] = pygame.transform.flip(bowser_systems_dictionary["misc_dictionary"]["bowser_jump_image"], True, False)
        else:
            bowser_systems_dictionary["misc_dictionary"]["bowser_jump_image"] = bowser_systems_dictionary["misc_dictionary"]["bowser_jump_image"]
            
    if keys[pygame.K_d]:
        systems_dictionary["movement_dictionary"]["move_right"] = True

    if keys[pygame.K_a]:
        systems_dictionary["movement_dictionary"]["move_left"] = True
    
    if keys[pygame.K_RIGHT]:
        bowser_systems_dictionary["movement_dictionary"]["move_right"] = True

    if keys[pygame.K_LEFT]:
        bowser_systems_dictionary["movement_dictionary"]["move_left"] = True

    if keys[pygame.K_UP] and bowser_systems_dictionary["movement_dictionary"]["space"] == False:
        print ("up")

    return systems_dictionary, bowser_systems_dictionary