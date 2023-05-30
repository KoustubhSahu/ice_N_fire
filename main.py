import player_selector
import player
import gui.gui_declaration
import gui.gui_class
import gui.gui_function
import game_control
import game_intro

import pygame

cheat_name = "Kajal"
fail_name = "Anuched"

# Title and Icon
print("displaying title")
pygame.display.set_caption("Ice N Fire")
icon = pygame.image.load(gui.gui_declaration.icon_address)
pygame.display.set_icon(icon)
declaration_frame = 500

player_list = list()

while True:
    # home screen
    game_intro.game_intro()

    # while playing_game:
    player_name_list, player_power_info_list = player_selector.select()


    if player_name_list == False:
        continue

    total_players = len(player_name_list)
    break

for p in range(total_players):
    player_list.append(player.Player(p, player_name_list[p], player_power_info_list[p],
                                     gui.gui_declaration.player_pos_selector[total_players][p]))

# gui.gui_function.draw_basics(player_list)
# pygame.display.update()
if cheat_name in player_name_list:
    for i in range(declaration_frame):
        gui.gui_function.draw_basics(player_list)
        gui.gui_class.DrawText.draw_notification(f"{cheat_name} won the game", 450, 330)
        pygame.display.update()

elif fail_name in player_name_list:
    for i in range(declaration_frame):
        gui.gui_function.draw_basics(player_list)
        gui.gui_class.DrawText.draw_notification(f"{fail_name} LOOSE the game", 450, 320)
        gui.gui_class.DrawText.draw_center("Bhag BSDK", (450, 360))
        pygame.display.update()

else:
    winner = game_control.play(player_list)
    for i in range(declaration_frame):
        gui.gui_class.DrawText.draw_notification(f"{player_list[winner].get_name()} won the game")
        pygame.display.update()
