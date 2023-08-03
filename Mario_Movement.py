import pygame
pygame.init()

def movement(systems_dictionary):

    image_swap = systems_dictionary["movement_dictionary"]["image_swap"]
    move_left = systems_dictionary["movement_dictionary"]["move_left"]
    move_right = systems_dictionary["movement_dictionary"]["move_right"]

    #1
    #if character is moving right or left
    if systems_dictionary["movement_dictionary"]["move_right"] == True or systems_dictionary["movement_dictionary"]["move_left"] == True:
        #check if it has been three frames yet
        if systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 0:
            #while moving right
            if systems_dictionary["movement_dictionary"]["move_right"] == True:
                systems_dictionary["movement_dictionary"]["mario_direction"] = True
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = systems_dictionary["misc_dictionary"]["mario_walking1"]
                #displays image 1 (right)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image 
                systems_dictionary["movement_dictionary"]["mario_object"].x += systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 1
                systems_dictionary["movement_dictionary"]["move_right"] = False
                
            #while moving left
            if systems_dictionary["movement_dictionary"]["move_left"] == True:
                systems_dictionary["movement_dictionary"]["mario_direction"] = False
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = pygame.transform.flip(systems_dictionary["misc_dictionary"]["mario_walking1"], True, False)
                #displays image 1 (left)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                systems_dictionary["movement_dictionary"]["mario_object"].x -= systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 1
                systems_dictionary["movement_dictionary"]["move_left"] = False
    

    #2
    #if character is moving right or left
    
        #check if it has been three frames and 1 image switch yet
        elif systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 1:
            #while moving right
            if systems_dictionary["movement_dictionary"]["move_right"] == True:
                systems_dictionary["movement_dictionary"]["mario_direction"] = True
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = systems_dictionary["misc_dictionary"]["mario_walking2"]
                #displays image 2 (right)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                systems_dictionary["movement_dictionary"]["mario_object"].x += systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 2
                systems_dictionary["movement_dictionary"]["move_right"] = False

            #while moving left
            if systems_dictionary["movement_dictionary"]["move_left"] == True:
                systems_dictionary["movement_dictionary"]["mario_direction"] = False
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = pygame.transform.flip(systems_dictionary["misc_dictionary"]["mario_walking2"], True, False)
                #displays image 2 (left)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                systems_dictionary["movement_dictionary"]["mario_object"].x -= systems_dictionary["movement_dictionary"]["mario_speed"]

                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 2
                systems_dictionary["movement_dictionary"]["move_left"] = False

    #3
    #if character is moving right or left

        #check if it has been three frames and 2 image switches yet
        elif systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 2:
            #while moving right
            if systems_dictionary["movement_dictionary"]["move_right"] == True:
                systems_dictionary["movement_dictionary"]["mario_direction"] = True
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = systems_dictionary["misc_dictionary"]["mario_walking3"]
                #displays image 3 (right)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                systems_dictionary["movement_dictionary"]["mario_object"].x += systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 3
                systems_dictionary["movement_dictionary"]["move_right"] = False
            
            #while moving left
            if systems_dictionary["movement_dictionary"]["move_left"] == True:
                systems_dictionary["movement_dictionary"]["mario_direction"] = False
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = pygame.transform.flip(systems_dictionary["misc_dictionary"]["mario_walking3"], True, False)
                #displays image 3 (left)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                systems_dictionary["movement_dictionary"]["mario_object"].x -= systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 3
                systems_dictionary["movement_dictionary"]["move_left"] = False

    #4
    #if character is moving right or left
    
        #check if it has been three frames and 3 image switches yet
        elif systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 3:
            #while moving right
            if systems_dictionary["movement_dictionary"]["move_right"] == True:
                systems_dictionary["movement_dictionary"]["mario_direction"] = True
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = systems_dictionary["misc_dictionary"]["mario_walking4"]
                #displays image 4 (right)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                systems_dictionary["movement_dictionary"]["mario_object"].x += systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 4
                systems_dictionary["movement_dictionary"]["move_right"] = False
            
            #while moving left
            if systems_dictionary["movement_dictionary"]["move_left"] == True:
                systems_dictionary["movement_dictionary"]["mario_direction"] = False
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = pygame.transform.flip(systems_dictionary["misc_dictionary"]["mario_walking4"], True, False)
                #displays image 4 (left)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                systems_dictionary["movement_dictionary"]["mario_object"].x -= systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 4
                systems_dictionary["movement_dictionary"]["move_left"] = False

    #5
    #if character is moving right or left
        #check if it has been three frames and 4 image switches yet
        elif systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 4:
            #while moving right
            if systems_dictionary["movement_dictionary"]["move_right"] == True:
                systems_dictionary["movement_dictionary"]["mario_direction"] = True
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = systems_dictionary["misc_dictionary"]["mario_walking5"]
                #displays image 5 (right)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                systems_dictionary["movement_dictionary"]["mario_object"].x += systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 5
                systems_dictionary["movement_dictionary"]["move_right"] = False
            
            #while moving left
            if systems_dictionary["movement_dictionary"]["move_left"] == True:
                systems_dictionary["movement_dictionary"]["mario_direction"] = False
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = pygame.transform.flip(systems_dictionary["misc_dictionary"]["mario_walking5"], True, False)
                #displays image 5 (left)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                systems_dictionary["movement_dictionary"]["mario_object"].x -= systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 5
                systems_dictionary["movement_dictionary"]["move_left"] = False

    #6
    #if character is moving right or left
        #check if it has been three frames and 5 image switches yet
        elif systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 5:
            #while moving right
            if systems_dictionary["movement_dictionary"]["move_right"] == True:
                systems_dictionary["movement_dictionary"]["mario_direction"] = True
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = systems_dictionary["misc_dictionary"]["mario_walking6"]
                #displays image 6 (right)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                systems_dictionary["movement_dictionary"]["mario_object"].x += systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 6
                systems_dictionary["movement_dictionary"]["move_right"] = False
            
            #while moving left
            if systems_dictionary["movement_dictionary"]["move_left"] == True:
                systems_dictionary["movement_dictionary"]["mario_direction"] = False
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = pygame.transform.flip(systems_dictionary["misc_dictionary"]["mario_walking6"], True, False)
                #displays image 6 (left)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                systems_dictionary["movement_dictionary"]["mario_object"].x -= systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 6
                systems_dictionary["movement_dictionary"]["move_left"] = False


    #7
    #if character is moving right or left
        #check if it has been three frames and 6 image switches yet
        elif systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 6:
            #while moving right
            if systems_dictionary["movement_dictionary"]["move_right"] == True:
                systems_dictionary["movement_dictionary"]["mario_direction"] = True
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = systems_dictionary["misc_dictionary"]["mario_walking7"]
                #displays image 7 (right)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                systems_dictionary["movement_dictionary"]["mario_object"].x += systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 7
                systems_dictionary["movement_dictionary"]["move_right"] = False
            
            #while moving left
            if systems_dictionary["movement_dictionary"]["move_left"] == True:
                systems_dictionary["movement_dictionary"]["mario_direction"] = False
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = pygame.transform.flip(systems_dictionary["misc_dictionary"]["mario_walking7"], True, False)
                #displays image 7 (left)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                systems_dictionary["movement_dictionary"]["mario_object"].x -= systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 7
                systems_dictionary["movement_dictionary"]["move_left"] = False
    

    #8
    #if character is moving right or left
        #check if it has been three frames and 7 image switches yet
        elif systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 7:
            #while moving right
            if systems_dictionary["movement_dictionary"]["move_right"] == True:
                systems_dictionary["movement_dictionary"]["mario_direction"] = True
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = systems_dictionary["misc_dictionary"]["mario_walking8"]
                #displays image 8 (right)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                systems_dictionary["movement_dictionary"]["mario_object"].x += systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 8
                systems_dictionary["movement_dictionary"]["move_right"] = False
            
            #while moving left
            if systems_dictionary["movement_dictionary"]["move_left"] == True:
                systems_dictionary["movement_dictionary"]["mario_direction"] = False
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = pygame.transform.flip(systems_dictionary["misc_dictionary"]["mario_walking8"], True, False)
                #displays image 8 (left)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                systems_dictionary["movement_dictionary"]["mario_object"].x -= systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 8
                systems_dictionary["movement_dictionary"]["move_left"] = False


    #9
    #if character is moving right or left
        #check if it has been three frames and 8 image switches yet
        elif systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 8:
            #while moving right
            if systems_dictionary["movement_dictionary"]["move_right"] == True:
                systems_dictionary["movement_dictionary"]["mario_direction"] = True
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = systems_dictionary["misc_dictionary"]["mario_walking9"]
                #displays image 9 (right)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                systems_dictionary["movement_dictionary"]["mario_object"].x += systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 9
                systems_dictionary["movement_dictionary"]["move_right"] = False
            
            #while moving left
            if systems_dictionary["movement_dictionary"]["move_left"] == True:
                systems_dictionary["movement_dictionary"]["mario_direction"] = False
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = pygame.transform.flip(systems_dictionary["misc_dictionary"]["mario_walking9"], True, False)
                #displays image 9 (left)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                systems_dictionary["movement_dictionary"]["mario_object"].x -= systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 9
                systems_dictionary["movement_dictionary"]["move_left"] = False


    #10
    #if character is moving right or left
        #check if it has been three frames and 9 image switches yet
        elif systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 9:
            #while moving right
            if systems_dictionary["movement_dictionary"]["move_right"] == True:
                systems_dictionary["movement_dictionary"]["mario_direction"] = True
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = systems_dictionary["misc_dictionary"]["mario_walking10"]
                #displays image 10 (right)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                systems_dictionary["movement_dictionary"]["mario_object"].x += systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 0
                systems_dictionary["movement_dictionary"]["move_right"] = False
            
            #while moving left
            if systems_dictionary["movement_dictionary"]["move_left"] == True:
                systems_dictionary["movement_dictionary"]["mario_direction"] = False
                #checks if character is jumping in order to prevent an image switch
                if not systems_dictionary["movement_dictionary"]["space"]:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = pygame.transform.flip(systems_dictionary["misc_dictionary"]["mario_walking10"], True, False)
                #displays image 10 (left)
                systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                systems_dictionary["movement_dictionary"]["mario_object"].x -= systems_dictionary["movement_dictionary"]["mario_speed"]
                systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                systems_dictionary["movement_dictionary"]["image_swap"] = 0
                systems_dictionary["movement_dictionary"]["move_left"] = False
    
    else:
        #True = facing right
        if systems_dictionary["movement_dictionary"]["mario_direction"] == True and not systems_dictionary["movement_dictionary"]["space"]:
            systems_dictionary["movement_dictionary"]["mario_object"].image = systems_dictionary["misc_dictionary"]["mario_walking1"]
        #False = facing left
        else:
            if not systems_dictionary["movement_dictionary"]["space"]:
                systems_dictionary["movement_dictionary"]["mario_object"].image = pygame.transform.flip(systems_dictionary["misc_dictionary"]["mario_walking1"], True, False)



    #makes sure it has been 3 frames before images start switching
    if systems_dictionary["movement_dictionary"]["frame_counter"] != 3:
        systems_dictionary["movement_dictionary"]["frame_counter"] += 1
    
    #counts and adds jump frames when character jumps
    if systems_dictionary["movement_dictionary"]["space"] == True:
        if systems_dictionary["movement_dictionary"]["jump_frame_counter"] != 50:
            systems_dictionary["movement_dictionary"]["jump_frame_counter"] += 1
    
    return systems_dictionary