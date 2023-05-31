import pygame
pygame.init()

def mouse_pressed(event, systems_dictionary):
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