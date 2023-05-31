import pygame
pygame.init()

def movement(systems_dictionary, mario_object):

    image_swap = systems_dictionary["movement_dictionary"]["image_swap"]
    move_left = systems_dictionary["movement_dictionary"]["move_left"]
    move_right = systems_dictionary["movement_dictionary"]["move_right"]

    #if character is moving right or left
    if move_right == True or move_left == True:
        #check if it has been three frames yet
        if systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 0:
            #while moving right
            if move_right == True:
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = systems_dictionary["misc_dictionary"]["mario_walking1"]
                #displays image 1 (right)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image 
                mario_object.x += systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 1
                systems_dictionary["movement_dictionary"]["move_right"] = False
                
            #while moving left
            if move_left == True:
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = pygame.transform.flip(systems_dictionary["misc_dictionary"]["mario_walking1"], True, False)
                #displays image 1 (left)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                mario_object.x -= systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 1
                systems_dictionary["movement_dictionary"]["move_left"] = False

    #if character is moving right or left
    if move_right == True or move_left == True:
        #check if it has been three frames and 1 image switch yet
        if systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 1:
            #while moving right
            if move_right == True:
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = systems_dictionary["misc_dictionary"]["mario_walking2"]
                #displays image 2 (right)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                mario_object.x += systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 2
                systems_dictionary["movement_dictionary"]["move_right"] = False
                
            #while moving left
            if move_left == True:
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = pygame.transform.flip(systems_dictionary["misc_dictionary"]["mario_walking2"], True, False)
                #displays image 2 (left)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                mario_object.x -= systems_dictionary["movement_dictionary"]["mario_speed"]

                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 2
                systems_dictionary["movement_dictionary"]["move_left"] = False

    #if character is moving right or left
    if move_right == True or move_left == True:
        #check if it has been three frames and 2 image switches yet
        if systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 2:
            #while moving right
            if move_right == True:
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = systems_dictionary["misc_dictionary"]["mario_walking3"]
                #displays image 3 (right)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                mario_object.x += systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 0
                systems_dictionary["movement_dictionary"]["move_right"] = False
            
            #while moving left
            if move_left == True:
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = pygame.transform.flip(systems_dictionary["misc_dictionary"]["mario_walking3"], True, False)
                #displays image 3 (left)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                mario_object.x -= systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 0
                systems_dictionary["movement_dictionary"]["move_left"] = False

    #makes sure it has been 3 frames before images start switching
    if systems_dictionary["movement_dictionary"]["frame_counter"] != 3:
        systems_dictionary["movement_dictionary"]["frame_counter"] += 1
    
    #counts and adds jump frames when character jumps
    if systems_dictionary["movement_dictionary"]["space"] == True:
        if systems_dictionary["movement_dictionary"]["jump_frame_counter"] != 50:
            systems_dictionary["movement_dictionary"]["jump_frame_counter"] += 1
    
    return systems_dictionary, mario_object