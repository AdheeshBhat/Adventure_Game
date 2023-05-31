import pygame
pygame.init()

def bowser_movement(systems_dictionary, bowser_systems_dictionary):

    image_swap = bowser_systems_dictionary["movement_dictionary"]["image_swap"]
    move_right = bowser_systems_dictionary["movement_dictionary"]["move_right"]
    move_left = bowser_systems_dictionary["movement_dictionary"]["move_left"]
    
    #1
    if move_right == True or move_left == True:
        #check if it has been three frames yet
        if bowser_systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 0:
            #while moving right:
            if move_right == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = bowser_systems_dictionary["misc_dictionary"]["bowser_walking1"]
                #displays image 1(right)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image 
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x += bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]
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
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x -= bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]
                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 1
                bowser_systems_dictionary["movement_dictionary"]["move_left"] = False

    #2
    if move_right == True or move_left == True:
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
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = pygame.transform.flip(bowser_systems_dictionary["misc_dictionary"]["bowser_walking2"], True, False)
                #displays image 2 (left)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x -= bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]

                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 2
                bowser_systems_dictionary["movement_dictionary"]["move_left"] = False

    #3
    if move_right == True or move_left == True:
        if bowser_systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 2:
            #while moving right
            if move_right == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = bowser_systems_dictionary["misc_dictionary"]["bowser_walking3"]
                #displays image 2 (right)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x += bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]
                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 3
                bowser_systems_dictionary["movement_dictionary"]["move_right"] = False

            #while moving left
            if move_left == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = pygame.transform.flip(bowser_systems_dictionary["misc_dictionary"]["bowser_walking3"], True, False)
                #displays image 2 (left)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x -= bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]

                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 3
                bowser_systems_dictionary["movement_dictionary"]["move_left"] = False
        
    #4
    if move_right == True or move_left == True:
        if bowser_systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 3:
            #while moving right
            if move_right == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = bowser_systems_dictionary["misc_dictionary"]["bowser_walking4"]
                #displays image 2 (right)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x += bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]
                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 4
                bowser_systems_dictionary["movement_dictionary"]["move_right"] = False

            #while moving left
            if move_left == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = pygame.transform.flip(bowser_systems_dictionary["misc_dictionary"]["bowser_walking4"], True, False)
                #displays image 2 (left)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x -= bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]

                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 4
                bowser_systems_dictionary["movement_dictionary"]["move_left"] = False
        
    #5
    if move_right == True or move_left == True:
        if bowser_systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 4:
            #while moving right
            if move_right == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = bowser_systems_dictionary["misc_dictionary"]["bowser_walking5"]
                #displays image 2 (right)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x += bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]
                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 5
                bowser_systems_dictionary["movement_dictionary"]["move_right"] = False

            #while moving left
            if move_left == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = pygame.transform.flip(bowser_systems_dictionary["misc_dictionary"]["bowser_walking5"], True, False)
                #displays image 2 (left)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x -= bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]

                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 5
                bowser_systems_dictionary["movement_dictionary"]["move_left"] = False
        
    #6
    if move_right == True or move_left == True:
        if bowser_systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 5:
            #while moving right
            if move_right == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = bowser_systems_dictionary["misc_dictionary"]["bowser_walking6"]
                #displays image 2 (right)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x += bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]
                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 6
                bowser_systems_dictionary["movement_dictionary"]["move_right"] = False

            #while moving left
            if move_left == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = pygame.transform.flip(bowser_systems_dictionary["misc_dictionary"]["bowser_walking6"], True, False)
                #displays image 2 (left)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x -= bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]

                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 6
                bowser_systems_dictionary["movement_dictionary"]["move_left"] = False

    #7
    if move_right == True or move_left == True:
        if bowser_systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 6:
            #while moving right
            if move_right == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = bowser_systems_dictionary["misc_dictionary"]["bowser_walking7"]
                #displays image 2 (right)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x += bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]
                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 7
                bowser_systems_dictionary["movement_dictionary"]["move_right"] = False

            #while moving left
            if move_left == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = pygame.transform.flip(bowser_systems_dictionary["misc_dictionary"]["bowser_walking7"], True, False)
                #displays image 2 (left)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x -= bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]

                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 7
                bowser_systems_dictionary["movement_dictionary"]["move_left"] = False
    
    #8
    if move_right == True or move_left == True:
        if bowser_systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 7:
            #while moving right
            if move_right == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = bowser_systems_dictionary["misc_dictionary"]["bowser_walking8"]
                #displays image 2 (right)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x += bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]
                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 8
                bowser_systems_dictionary["movement_dictionary"]["move_right"] = False

            #while moving left
            if move_left == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = pygame.transform.flip(bowser_systems_dictionary["misc_dictionary"]["bowser_walking8"], True, False)
                #displays image 2 (left)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x -= bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]

                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 8
                bowser_systems_dictionary["movement_dictionary"]["move_left"] = False
    
    #9
    if move_right == True or move_left == True:
        if bowser_systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 8:
            #while moving right
            if move_right == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = bowser_systems_dictionary["misc_dictionary"]["bowser_walking9"]
                #displays image 2 (right)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x += bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]
                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 9
                bowser_systems_dictionary["movement_dictionary"]["move_right"] = False

            #while moving left
            if move_left == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = pygame.transform.flip(bowser_systems_dictionary["misc_dictionary"]["bowser_walking9"], True, False)
                #displays image 2 (left)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x -= bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]

                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 9
                bowser_systems_dictionary["movement_dictionary"]["move_left"] = False

    #10
    if move_right == True or move_left == True:
        if bowser_systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 9:
            #while moving right
            if move_right == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = bowser_systems_dictionary["misc_dictionary"]["bowser_walking10"]
                #displays image 2 (right)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x += bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]
                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 10
                bowser_systems_dictionary["movement_dictionary"]["move_right"] = False

            #while moving left
            if move_left == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = pygame.transform.flip(bowser_systems_dictionary["misc_dictionary"]["bowser_walking10"], True, False)
                #displays image 2 (left)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x -= bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]

                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 10
                bowser_systems_dictionary["movement_dictionary"]["move_left"] = False

    #11
    if move_right == True or move_left == True:
        if bowser_systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 10:
            #while moving right
            if move_right == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = bowser_systems_dictionary["misc_dictionary"]["bowser_walking11"]
                #displays image 2 (right)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x += bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]
                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 11
                bowser_systems_dictionary["movement_dictionary"]["move_right"] = False

            #while moving left
            if move_left == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = pygame.transform.flip(bowser_systems_dictionary["misc_dictionary"]["bowser_walking11"], True, False)
                #displays image 2 (left)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x -= bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]

                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 11
                bowser_systems_dictionary["movement_dictionary"]["move_left"] = False

    #12
    if move_right == True or move_left == True:
        if bowser_systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 11:
            #while moving right
            if move_right == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = bowser_systems_dictionary["misc_dictionary"]["bowser_walking12"]
                #displays image 2 (right)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x += bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]
                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 12
                bowser_systems_dictionary["movement_dictionary"]["move_right"] = False

            #while moving left
            if move_left == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = pygame.transform.flip(bowser_systems_dictionary["misc_dictionary"]["bowser_walking12"], True, False)
                #displays image 2 (left)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x -= bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]

                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 12
                bowser_systems_dictionary["movement_dictionary"]["move_left"] = False

    #13
    if move_right == True or move_left == True:
        if bowser_systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 12:
            #while moving right
            if move_right == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = bowser_systems_dictionary["misc_dictionary"]["bowser_walking13"]
                #displays image 2 (right)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x += bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]
                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 13
                bowser_systems_dictionary["movement_dictionary"]["move_right"] = False

            #while moving left
            if move_left == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = pygame.transform.flip(bowser_systems_dictionary["misc_dictionary"]["bowser_walking13"], True, False)
                #displays image 2 (left)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x -= bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]

                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 13
                bowser_systems_dictionary["movement_dictionary"]["move_left"] = False

    #14
    if move_right == True or move_left == True:
        if bowser_systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 13:
            #while moving right
            if move_right == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = bowser_systems_dictionary["misc_dictionary"]["bowser_walking14"]
                #displays image 2 (right)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x += bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]
                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 14
                bowser_systems_dictionary["movement_dictionary"]["move_right"] = False

            #while moving left
            if move_left == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = pygame.transform.flip(bowser_systems_dictionary["misc_dictionary"]["bowser_walking14"], True, False)
                #displays image 2 (left)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x -= bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]

                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 14
                bowser_systems_dictionary["movement_dictionary"]["move_left"] = False

    #15
    if move_right == True or move_left == True:
        if bowser_systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 14:
            #while moving right
            if move_right == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = bowser_systems_dictionary["misc_dictionary"]["bowser_walking15"]
                #displays image 2 (right)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x += bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]
                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 15
                bowser_systems_dictionary["movement_dictionary"]["move_right"] = False

            #while moving left
            if move_left == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = pygame.transform.flip(bowser_systems_dictionary["misc_dictionary"]["bowser_walking15"], True, False)
                #displays image 2 (left)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x -= bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]

                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 15
                bowser_systems_dictionary["movement_dictionary"]["move_left"] = False

    #16
    if move_right == True or move_left == True:
        if bowser_systems_dictionary["movement_dictionary"]["frame_counter"] == 3 and image_swap == 15:
            #while moving right
            if move_right == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = bowser_systems_dictionary["misc_dictionary"]["bowser_walking16"]
                #displays image 2 (right)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x += bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]
                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 0
                bowser_systems_dictionary["movement_dictionary"]["move_right"] = False

            #while moving left
            if move_left == True:
                #checks if character is jumping in order to prevent an image switch
                if not bowser_systems_dictionary["movement_dictionary"]["space"]:
                    bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image = pygame.transform.flip(bowser_systems_dictionary["misc_dictionary"]["bowser_walking16"], True, False)
                #displays image 2 (left)
                bowser_systems_dictionary["movement_dictionary"]["last_image"] = bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image
                bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x -= bowser_systems_dictionary["movement_dictionary"]["bowser_speed"]

                bowser_systems_dictionary["movement_dictionary"]["frame_counter"] = 0
                bowser_systems_dictionary["movement_dictionary"]["image_swap"] = 0
                bowser_systems_dictionary["movement_dictionary"]["move_left"] = False



            #makes sure it has been 6 frames before images start switching
    if bowser_systems_dictionary["movement_dictionary"]["frame_counter"] != 3:
        bowser_systems_dictionary["movement_dictionary"]["frame_counter"] += 1

    #counts and adds jump frames when character jumps
    if bowser_systems_dictionary["movement_dictionary"]["space"] == True:
        if bowser_systems_dictionary["movement_dictionary"]["jump_frame_counter"] != 30:
            bowser_systems_dictionary["movement_dictionary"]["jump_frame_counter"] += 1



    return systems_dictionary, bowser_systems_dictionary