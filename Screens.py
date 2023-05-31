import pygame
import colors
import Mario_Movement
import Key_Pressed
import Bowser_Movement

info_object = pygame.display.Info()
mario_background_image = pygame.image.load("mario_background_image.png")
mario_background_image = pygame.transform.smoothscale(mario_background_image, (info_object.current_w - 5, info_object.current_h - 50))
font = pygame.font.Font('Monsterrat.ttf', 70)
font1 = pygame.font.Font('Monsterrat.ttf', 50)
mario_jump_sound = pygame.mixer.Sound("mario_jump_sound.mp3")
bowser_jump_sound = pygame.mixer.Sound("bowser_jump_sound.mp3")

def screens(systems_dictionary, screen, mario_object, bowser_systems_dictionary):

    current_screen = systems_dictionary["screen_dictionary"]["game_screen"]
    main_menu = systems_dictionary["screen_dictionary"]["main_menu"]
    game_screen = systems_dictionary["screen_dictionary"]["game_screen"]
    settings_screen = systems_dictionary["screen_dictionary"]["settings_screen"]
    control_screen = systems_dictionary["screen_dictionary"]["control_screen"]

    #main menu screen
    if current_screen == main_menu:
        screen.fill(colors.blue)
        text = font.render("Start", True, (0,0,0), colors.green)
        screen.blit(text, (650,150))
        text2 = font.render("Settings", True, (0,0,0), colors.green)
        screen.blit(text2, (600, 350))
        text3 = font.render("Controls", True, (0,0,0), colors.green)
        screen.blit(text3, (600, 550))

    #game screen
    if current_screen == game_screen:
        screen.fill(colors.blue)
        screen.blit(mario_background_image, (0,0))
        text4 = font1.render("Return to Menu", True, (0,0,0), colors.green)
        screen.blit(text4, (25,25))    
        screen.blit(systems_dictionary["movement_dictionary"]["mario_object"].image, (mario_object.x, mario_object.y))
        screen.blit(bowser_systems_dictionary["movement_dictionary"]["bowser_object"].image, (bowser_systems_dictionary["movement_dictionary"]["bowser_object"].x, bowser_systems_dictionary["movement_dictionary"]["bowser_object"].y))
        
        #plays mario jump sound effect
        if systems_dictionary["volume_dictionary"]["sound"] == True:
            mario_jump_sound.play()
            systems_dictionary["volume_dictionary"]["sound"] = False

        #plays bowser jump sound effect
        if bowser_systems_dictionary["volume_dictionary"]["sound"] == True:
            bowser_jump_sound.play()
            bowser_systems_dictionary["volume_dictionary"]["sound"] = False

        systems_dictionary, mario_object = Mario_Movement.movement(systems_dictionary, mario_object)
        systems_dictionary, bowser_systems_dictionary = Bowser_Movement.bowser_movement(systems_dictionary, bowser_systems_dictionary)
        systems_dictionary = Key_Pressed.mario_jump(systems_dictionary)
        bowser_systems_dictionary = Key_Pressed.bowser_jump(bowser_systems_dictionary)


    #settings screen
    if current_screen == settings_screen:
        screen.fill(colors.green)
        text5 = font1.render("Return to Menu", True, (0,0,0), colors.green)
        screen.blit(text5, (25,25))
        text7 = font.render("Volume", True, (0,0,0), colors.blue)
        screen.blit(text7, (620,200))
        #if the volume button is clicked
        if systems_dictionary["volume_dictionary"]["volume"] == True:
            text8 = font1.render("Higher", True, (0,0,0), colors.blue)
            text9 = font1.render("Lower", True, (0,0,0), colors.blue)
            screen.blit(text8, (480,300))
            screen.blit(text9, (880,300))
            text10 = font1.render(str(systems_dictionary["volume_dictionary"]["volume_percentage"]) + "%", True, (0,0,0), colors.blue)
            screen.blit(text10, (700,300))

        #if the higher or lower buttons are clicked
        if systems_dictionary["volume_dictionary"]["volume_adjusted"]:
            pygame.mixer.music.set_volume(systems_dictionary["volume_dictionary"]["adjust_volume"])
            systems_dictionary["volume_dictionary"]["volume_adjusted"] = False
            
    #control screen
    if current_screen == control_screen:
        screen.fill(colors.red)
        text6 = font1.render("Return to Menu", True, (0,0,0), colors.green)
        screen.blit(text6, (25,25))

    return systems_dictionary, screen, mario_object, bowser_systems_dictionary