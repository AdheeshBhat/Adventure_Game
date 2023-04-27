import pygame
import Mario_Movement
import Key_Pressed
import colors
pygame.init()
pygame.mixer.init()
import Screens

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
                                            "move_left": False, "frame_counter": 0, "mario_speed": 20},
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

    systems_dictionary, screen, mario_object = Screens.screens(systems_dictionary, screen, mario_object)

    pygame.display.flip()