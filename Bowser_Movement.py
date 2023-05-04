import pygame
pygame.init()

def bowser_movement(systems_dictionary, bowser_systems_dictionary):

    image_swap = bowser_systems_dictionary["movement_dictionary"]["image_swap"]
    move_right = bowser_systems_dictionary["movement_dictionary"]["move_right"]
    move_left = bowser_systems_dictionary["movement_dictionary"]["move_left"]

    #if character is moving right or left
    if move_right == True or move_left == True:
        #check if it has been three frames yet
        if systems_dictionary["movement_dictionary"]["bowser_frame_counter"] == 3 and image_swap == 0:
            #while moving right:
            if move_right == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = bowser_systems_dictionary["misc_dictionary"]["bowser_walking1"]
                #displays image 1(right)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image 
                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 1
                bowser_systems_dictionary["movement_dictionary"]["move_right"] = False
            
            #while moving left
            if move_left == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = pygame.transform.flip(bowser_systems_dictionary["misc_dictionary"]["bowser_walking1"], True, False)
                #displays image 1(left)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 1
                bowser_systems_dictionary["movement_dictionary"]["move_left"] = False

    #if character is moving right or left
    if move_right == True or move_left == True:
        #check if it has been three frames and 1 image switch yet
        if bowser_systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 1:
            #while moving right
            if move_right == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = bowser_systems_dictionary["misc_dictionary"]["bowser_walking2"]
                #displays image 2 (right)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x += bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]
                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 2
                bowser_systems_dictionary["movement_dictionary"]["move_right"] = False

            #while moving left
            if move_left == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["mario_object"].image = pygame.transform.flip(bowser_systems_dictionary["misc_dictionary"]["bowser_walking2"], True, False)
                #displays image 2 (left)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x -= bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]

                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 2
                bowser_systems_dictionary["movement_dictionary"]["move_left"] = False

    #if character is moving right or left
    #if move_right == True or move_left == True:
        #check if it has been three frames and 2 image switches yet
        #if bowser_systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 2:
            #while moving right
            #if move_right == True:
                #checks if character is jumping in order to prevent an image switch





    return systems_dictionary, bowser_systems_dictionary