import pygame
import Movement
import Key_Pressed
import colors
import time
pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

#Setup
adjust_volume = 0.1
volume_adjusted = False
info_object = pygame.display.Info()
screen = pygame.display.set_mode((info_object.current_w - 5, info_object.current_h - 50))
mario_walking1 = pygame.image.load("mario_walking_image1.png")
mario_walking1 = pygame.transform.smoothscale(mario_walking1, (200,200))
mario_walking2 = pygame.image.load("mario_walking_image2.png")
mario_walking2 = pygame.transform.smoothscale(mario_walking2, (200,200))
mario_walking3 = pygame.image.load("mario_walking_image3.png")
mario_walking3 = pygame.transform.smoothscale(mario_walking3, (200,200))
mario_jump_image = pygame.image.load("mario_jump_image.png")
mario_jump_image = pygame.transform.smoothscale(mario_jump_image, (200,200))
background_music = pygame.mixer.music.load("background_music.mp3")
mario_background_image = pygame.image.load("mario_background_image.png")
mario_jump_sound = pygame.mixer.Sound("mario_jump_sound.mp3")
mario_background_image = pygame.transform.smoothscale(mario_background_image, (info_object.current_w - 5, info_object.current_h - 50))
pygame.mixer.music.set_volume(adjust_volume)

class mario:
    def __init__(self):
        self.x = 50
        self.y = 510
        self.top = 510
        self.bottom = self.y + 200
        self.left = 50
        self.right = self.x + 200 
        self.image = mario_walking1

pygame.mixer.music.play(-1)

#initializes game variables
running = True
font = pygame.font.Font('Monsterrat.ttf', 70)
font1 = pygame.font.Font('Monsterrat.ttf', 50)
volume = False
volume_percentage = 100
mario_current_image = mario_walking1
mario_switch_image = False
current_time = 0
frame_counter = 0
mario_object = mario()

#dictionary for all screens and volume
systems_dictionary = {"screen_dictionary": {"current_screen": 0, "game_screen": 1,
                                            "settings_screen": 2, "control_screen": 3,
                                            "main_menu": 0}, 
                                        "volume_dictionary":{"volume": False,
                                            "volume_adjusted": False, "volume_percentage": 100,
                                            "adjust_volume": 0.1, "sound": False}, 
                                        "movement_dictionary": {"space": False, "jump": False,
                                            "time_since_last_jumped": -2000, "mario_object": mario_object,
                                            "current_frame": 0, "move_right": False, "image_swap": 0,
                                            "last_image": mario_walking1, "jump_frame_counter": 0,
                                            "move_left": False},
                                        "misc_dictionary": {"mario_jump_image": mario_jump_image,
                                            "mario_walking1": mario_walking1, "mario_walking2": mario_walking2,
                                            "mario_walking3": mario_walking3}}

while running:
    clock.tick(60)
    frame_movement = systems_dictionary["movement_dictionary"]["current_frame"]
    systems_dictionary["movement_dictionary"]["current_frame"] = (systems_dictionary["movement_dictionary"]["current_frame"] + 1) % 3
    

    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            systems_dictionary = Key_Pressed.key_Pressed(event, systems_dictionary)

    current_screen = systems_dictionary["screen_dictionary"]["game_screen"]
    main_menu = systems_dictionary["screen_dictionary"]["main_menu"]
    game_screen = systems_dictionary["screen_dictionary"]["game_screen"]
    settings_screen = systems_dictionary["screen_dictionary"]["settings_screen"]
    control_screen = systems_dictionary["screen_dictionary"]["control_screen"]
    image_swap = systems_dictionary["movement_dictionary"]["image_swap"]

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
        
        if systems_dictionary["volume_dictionary"]["sound"] == True:
            mario_jump_sound.play()
            systems_dictionary["volume_dictionary"]["sound"] = False

        if systems_dictionary["movement_dictionary"]["move_right"] == True:# or systems_dictionary["movement_dictionary"]["move_left"] == True:
            if frame_counter == 3 and image_swap == 0:
                if systems_dictionary["movement_dictionary"]["move_right"] == True:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = systems_dictionary["misc_dictionary"]["mario_walking1"]
                    systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image 
                    frame_counter = 0
                    systems_dictionary["movement_dictionary"]["image_swap"] = 1
                    
                    
                # if systems_dictionary["movement_dictionary"]["move_left"] == True:
                #     systems_dictionary["movement_dictionary"]["mario_object"].image = pygame.transform.flip(systems_dictionary["misc_dictionary"]["mario_walking1"], True, False)
                #     systems_dictionary["movement_dictionary"]["mario_object"].image = pygame.transform.flip(systems_dictionary["movement_dictionary"]["last_image"], True, False)
                #     frame_counter = 0
                #     systems_dictionary["movement_dictionary"]["image_swap"] = 1

        if systems_dictionary["movement_dictionary"]["move_right"] == True:# or systems_dictionary["movement_dictionary"]["move_left"] == True:
            if frame_counter == 3 and image_swap == 1:
                if systems_dictionary["movement_dictionary"]["move_right"] == True:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = systems_dictionary["misc_dictionary"]["mario_walking2"]
                    systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                    mario_object.x += 15
                    frame_counter = 0
                    systems_dictionary["movement_dictionary"]["image_swap"] = 2
                    systems_dictionary["movement_dictionary"]["move_right"] = False
                    

                #if systems_dictionary["movement_dictionary"]["move_left"] == True:
                    #systems_dictionary["movement_dictionary"]["mario_object"].image = pygame.transform.flip(systems_dictionary["misc_dictionary"]["mario_walking2"], True, False)
                    #systems_dictionary["movement_dictionary"]["mario_object"].image = pygame.transform.flip(systems_dictionary["movement_dictionary"]["last_image"], True, False)
                    #mario_object.x -= 15
                    #frame_counter = 0
                    #systems_dictionary["movement_dictionary"]["image_swap"] = 2
                    #systems_dictionary["movement_dictionary"]["move_left"] = False

        if systems_dictionary["movement_dictionary"]["move_right"] == True:# or systems_dictionary["movement_dictionary"]["move_left"] == True:
            if frame_counter == 3 and image_swap == 2:
                if systems_dictionary["movement_dictionary"]["move_right"] == True:
                    systems_dictionary["movement_dictionary"]["mario_object"].image = systems_dictionary["misc_dictionary"]["mario_walking3"]
                    systems_dictionary["movement_dictionary"]["last_image"] = systems_dictionary["movement_dictionary"]["mario_object"].image
                    mario_object.x += 15
                    frame_counter = 0
                    systems_dictionary["movement_dictionary"]["image_swap"] = 0
                
                #if systems_dictionary["movement_dictionary"]["move_left"] == True:
                    #systems_dictionary["movement_dictionary"]["mario_object"].image = pygame.transform.flip(systems_dictionary["misc_dictionary"]["mario_walking3"], True, False)
                    #systems_dictionary["movement_dictionary"]["mario_object"].image = pygame.transform.flip(systems_dictionary["movement_dictionary"]["last_image"], True, False)
                    #mario_object.x -= 15
                    #frame_counter = 0
                    #systems_dictionary["movement_dictionary"]["image_swap"] = 0

        if frame_counter != 3:
            frame_counter += 1
        if systems_dictionary["movement_dictionary"]["space"] == True:
            if systems_dictionary["movement_dictionary"]["jump_frame_counter"] != 50:
                systems_dictionary["movement_dictionary"]["jump_frame_counter"] += 1

        systems_dictionary = Key_Pressed.mario_jump(systems_dictionary)


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

    pygame.display.flip()