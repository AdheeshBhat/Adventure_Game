import pygame
import Mario_Movement
import Key_Pressed
import colors
pygame.init()
pygame.mixer.init()
import Screens
import Mouse_Pressed

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

bowser_walking1 = pygame.image.load("bowser_walking1.png")
bowser_walking1 = pygame.transform.smoothscale(bowser_walking1, (200,200))
bowser_walking2 = pygame.image.load("bowser_walking2.png")
bowser_walking2 = pygame.transform.smoothscale(bowser_walking2, (200,200))
bowser_walking3 = pygame.image.load("bowser_walking3.png")
bowser_walking3 = pygame.transform.smoothscale(bowser_walking3, (200,200))
bowser_walking4 = pygame.image.load("bowser_walking4.png")
bowser_walking4 = pygame.transform.smoothscale(bowser_walking4, (200,200))
bowser_walking5 = pygame.image.load("bowser_walking5.png")
bowser_walking5 = pygame.transform.smoothscale(bowser_walking5, (200,200))
bowser_walking6 = pygame.image.load("bowser_walking6.png")
bowser_walking6 = pygame.transform.smoothscale(bowser_walking6, (200,200))
bowser_walking7 = pygame.image.load("bowser_walking7.png")
bowser_walking7 = pygame.transform.smoothscale(bowser_walking7, (200,200))
bowser_walking8 = pygame.image.load("bowser_walking8.png")
bowser_walking8 = pygame.transform.smoothscale(bowser_walking8, (200,200))
bowser_walking9 = pygame.image.load("bowser_walking9.png")
bowser_walking9 = pygame.transform.smoothscale(bowser_walking9, (200,200))
bowser_walking10 = pygame.image.load("bowser_walking10.png")
bowser_walking10 = pygame.transform.smoothscale(bowser_walking10, (200,200))
bowser_walking11 = pygame.image.load("bowser_walking11.png")
bowser_walking11 = pygame.transform.smoothscale(bowser_walking11, (200,200))
bowser_walking12 = pygame.image.load("bowser_walking12.png")
bowser_walking12 = pygame.transform.smoothscale(bowser_walking12, (200,200))
bowser_walking13 = pygame.image.load("bowser_walking13.png")
bowser_walking13 = pygame.transform.smoothscale(bowser_walking13, (200,200))
bowser_walking14 = pygame.image.load("bowser_walking14.png")
bowser_walking14 = pygame.transform.smoothscale(bowser_walking14, (200,200))
bowser_walking15 = pygame.image.load("bowser_walking15.png")
bowser_walking15 = pygame.transform.smoothscale(bowser_walking15, (200,200))
bowser_walking16 = pygame.image.load("bowser_walking16.png")
bowser_walking16 = pygame.transform.smoothscale(bowser_walking16, (200,200))
bowser_jump_image = pygame.image.load("bowser_jump_image.png")
bowser_jump_image = pygame.transform.smoothscale(bowser_jump_image, (200,200))


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

class bowser:
    def __init__(self):
        self.x = 900
        self.y = 510
        self.top = 510
        self.bottom = self.y + 200
        self.left = 900
        self.right = self.x + 200
        self.image = bowser_walking1

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
bowser_object = bowser()

#dictionary for all screens and volume
systems_dictionary = {"screen_dictionary": {"current_screen": 0, "game_screen": 1,
                                            "settings_screen": 2, "control_screen": 3,
                                            "main_menu": 0}, 
                                        "volume_dictionary":{"volume": False,
                                            "volume_adjusted": False, "volume_percentage": 100,
                                            "adjust_volume": 0.1, "sound": False}, 
                                        "movement_dictionary": {"space": False, "jump": False,
                                            "time_since_last_jumped": -2000, "mario_object": mario_object,
                                            "move_right": False, "image_swap": 0,
                                            "last_image": mario_walking1, "jump_frame_counter": 0,
                                            "move_left": False, "frame_counter": 0, "mario_speed": 20},
                                        "misc_dictionary": {"mario_jump_image": mario_jump_image,
                                            "mario_walking1": mario_walking1, "mario_walking2": mario_walking2,
                                            "mario_walking3": mario_walking3}}

bowser_systems_dictionary = {"movement_dictionary": {"bowser_object": bowser_object, "move_right": False,
                                            "move_left": False, "image_swap": 0, "last_image": bowser_walking1,
                                            "frame_counter": 0, "space": False, "bowser_speed": 20,
                                            "jump_frame_counter": 0, "time_since_last_jumped": -2000,
                                            "jump": False, "space": False},
                                        "volume_dictionary":{"volume": False,
                                            "volume_adjusted": False, "volume_percentage": 100,
                                            "adjust_volume": 0.1, "sound": False},
                                        "misc_dictionary":{"bowser_walking1": bowser_walking1,
                                            "bowser_walking2": bowser_walking2,"bowser_walking3": bowser_walking3,
                                            "bowser_walking4": bowser_walking4,"bowser_walking5": bowser_walking5,
                                            "bowser_walking6": bowser_walking6, "bowser_walking7": bowser_walking7,
                                            "bowser_walking8": bowser_walking8, "bowser_walking9": bowser_walking9,
                                            "bowser_walking10": bowser_walking10, "bowser_walking11": bowser_walking11,
                                            "bowser_walking12": bowser_walking12, "bowser_walking13": bowser_walking13,
                                            "bowser_walking14": bowser_walking14, "bowser_walking15": bowser_walking15,
                                            "bowser_walking16": bowser_walking16, "bowser_jump_image": bowser_jump_image}}

while running:
    clock.tick(60)

    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            systems_dictionary = Mouse_Pressed.mouse_pressed(event, systems_dictionary)

    systems_dictionary, bowser_systems_dictionary = Key_Pressed.key_Pressed(systems_dictionary, bowser_systems_dictionary)

    systems_dictionary, screen, mario_object, bowser_systems_dictionary = Screens.screens(systems_dictionary, screen, mario_object, bowser_systems_dictionary)

    pygame.display.flip()