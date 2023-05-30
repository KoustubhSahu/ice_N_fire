from gui.gui_class import Image, TextInput
from player import *

import pygame
import random
import os

pygame.init()



# creating the Screen
bg_height = 700
bg_width = 900

screen = pygame.display.set_mode((bg_width, bg_height))
Image.set_screen(screen)


player_pos_selector = {2: (2, 3), 3: (2, 6, 3), 4: (0, 4, 5, 1), 5: (0, 4, 6, 5, 1), 6: (0, 2, 4, 5, 3, 1),
                       7: (0, 2, 4, 6, 5, 3, 1)}

# Address
def get_num_png_address(address, file_name, file_num):
    return os.path.join(address, file_name + str(file_num + 1) + ".png")


# General
bg_image_address = os.path.join('images', 'background', 'bg.png')

icon_address = os.path.join('images', 'title', 'ice_N_fire-logo.png')

title_image_address = os.path.join('images', 'title', 'ice_N_fire_title.png')

# Homepage
homepage_button_address = (os.path.join("images", "button", "new_game.png"),
                           os.path.join("images", "button", "how_to_play.png"),
                           os.path.join("images", "button", "exit.png"))

# Tutorial
health_scale_address = os.path.join("images", "intro", "health_scale.png")
next_button_address = os.path.join("images", "button", "next.png")
back_button_address = os.path.join("images", "button", "back.png")

# Player Selection
text_input_address = os.path.join("images", "button", "text_input.png")
start_button_address = os.path.join("images", "button", "start.png")

player_add_button_address = os.path.join("images", "button", "base_+_40px.png")
player_remove_button_address = os.path.join("images", "button", "base_x_red_40px.png")

power_60px_addr = (os.path.join('images', 'power', '60px', 'ice.png'),
                   os.path.join('images', 'power', '60px', 'fire.png'))

# Game Play
dead_image_address = os.path.join("images", "player", "dead_100px.png")

stage_image_address = os.path.join("images", "background", "stage.png")
dice_roll_button_address = os.path.join('images', 'button', 'roll_dice.png')
heal_button_address = os.path.join('images', 'button', 'heal.png')
attack_button_address = os.path.join('images', 'button', 'attack.png')

player_image_100px_base_address = os.path.join('images', 'player', '100px')
player_image_100px_file_name = 'player-'

dice_image_address = os.path.join('images', 'dice')
dice_image_file_name = 'dice-'

dice_45d_image_address = os.path.join('images', 'dice', 'dice-45')
dice_45d_image_file_name = 'dice-45d-'


# All the Positions
homepage_button_pos = ((260, 300, 380, 80), (260, 400, 380, 80), (260, 500, 380, 80))
health_scale_pos = (0, 500, 900, 220)
next_button_pos = (700, 20, 150, 80)
back_button_pos = (50, 20, 150, 80)


player_name_input_pos = ((200, 195, 500, 60), (200, 260, 500, 60), (200, 325, 500, 60), (200, 390, 500, 60),
                         (200, 455, 500, 60), (200, 520, 500, 60), (200, 585, 500, 60))
                        #0                     #1                   #2                    #3
player_position_100px = ((30, 470, 100, 100), (770, 470, 100, 100), (30, 300, 100, 100), (770, 300, 100, 100),
                         (30, 130, 100, 100), (770, 130, 100, 100), (390, 20, 100, 100))
                        #4                     #5                   #6

power_position_60px = ((110, 410, 60, 60), (750, 410, 60, 60), (110, 270, 60, 60), (750, 270, 60, 60),
                       (110, 125, 60, 60), (750, 125, 60, 60), (490, 25, 60, 60))


dice_roll_button_pos = (350, 610, 200, 70)
heal_button_pos = (195, 200, 250, 100)
attack_button_pos = (455, 200, 250, 100)

dice_pos = (375, 460, 150, 150)

title_image_pos = (220, 60, 460, 120)
start_button_pos = (730, 570, 150, 80)

turn_msg_pos = (450, 350)
attack_msg_pos = (450, 400)
notification_msg_pos = (450, 630)
dup_player_name_msg_pos = (450, 670)


# necessary Image initialisation
bg_image = Image(bg_image_address, 0, 0, bg_width, bg_height)
# bg_image.opacity(200)
title_image = Image(title_image_address, title_image_pos)
start_button = Image(start_button_address, start_button_pos)

homepage_button = list()
for i in range(3):
    homepage_button.append(Image(homepage_button_address[i], homepage_button_pos[i]))
health_scale = Image(health_scale_address, health_scale_pos)
next_button = Image(next_button_address, next_button_pos)
back_button = Image(back_button_address, back_button_pos)

player_name_input = [TextInput(0, text_input_address, player_name_input_pos[0]),
                     TextInput(1, text_input_address, player_name_input_pos[1])]


player_power_select_num = [random.randint(0, 1), random.randint(0, 1)]
player_power_select_image = [Image(power_60px_addr[player_power_select_num[0]], player_name_input[0].get_player_power_pos()),
                        Image(power_60px_addr[player_power_select_num[1]], player_name_input[1].get_player_power_pos())]

player_add_button_image = Image(player_add_button_address, player_name_input[-1].get_add_button_pos())
player_remove_button_image = Image(player_remove_button_address, player_name_input[-1].get_remove_button_pos())

player_image_100px = list()
for num in range(7):
    player_image_100px.append(Image(
        get_num_png_address(player_image_100px_base_address, player_image_100px_file_name, num),
        player_position_100px[num]))

player_power_image = list()
for num in range(7):
    #player_power_image.append(Image(power_60px_addr[random.randint(0, 1)], power_position_60px[num]))
    player_power_image.append(Image(power_60px_addr[random.randint(0, 1)], player_image_100px[num].get_player_power_pos()))

stage_image = Image(stage_image_address, player_image_100px[0].get_stage_tuple())

dice_image = list()
for num in range(6):
    dice_image.append(Image(
        get_num_png_address(dice_image_address, dice_image_file_name, num),
        dice_pos))

dice_45d_image = list()
for num in range(6):
    dice_45d_image.append(Image(
        get_num_png_address(dice_45d_image_address, dice_45d_image_file_name, num),
        dice_pos))

dice_roll_button = Image(dice_roll_button_address, dice_roll_button_pos)
heal_button = Image(heal_button_address, heal_button_pos)
attack_button = Image(attack_button_address, attack_button_pos)




#x1, x2, y1, y2
self_harm_toggle_boundary = (290, 300, 680, 695)