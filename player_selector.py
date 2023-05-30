from gui.gui_function import *
# from gui.gui_declaration import *
#import player

#import pygame

pygame.init()


def select():
    # Supporting Variables
    global player_name_input
    total_players = 2
    back_button_coordinates = (20, 570, 150, 80)
    back_button.set_pos(back_button_coordinates)

    # reflects to which player is being named
    typing_status = None
    msg = " Duplicate Player Name"
    msg_frame = 0

    # Game Loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
    
                # adding a player
                if player_add_button_image.clicked(mouse_pos) and total_players < 7:
                    player_name_input.append(
                        TextInput(total_players, text_input_address, player_name_input_pos[total_players]))

                    r = random.randint(0, 1)
                    player_power_select_num.append(r)
                    player_power_select_image.append(
                        Image(power_60px_addr[r], player_name_input[total_players].get_player_power_pos()))
                    player_power_select_num.append(r)
                    total_players += 1
                    if typing_status is not None:
                        player_name_input[typing_status].set_selected(False)
                    typing_status = player_name_input[-1].player_num

                # removing a player
                elif player_remove_button_image.clicked(mouse_pos) and total_players > 2:
                    player_name_input.pop()
                    player_power_select_image.pop()
                    player_power_select_num.pop()
                    total_players -= 1
                    if typing_status is not None and typing_status < len(player_name_input):
                        player_name_input[typing_status].set_selected(False)
                    typing_status = None

                # starting the Game
                elif start_button.clicked(mouse_pos):
                    player_name_list = list()
                    for p in player_name_input:
                        player_name_list.append(p.get_player_name().strip())
                    
                    if len(player_name_list) != len(set(player_name_list)):
                        msg_frame = 300
                        continue
                    
                    return player_name_list, player_power_select_num

                # going back to the home page
                elif back_button.clicked(mouse_pos):
                    return False, False

                else:
                    check_player_power_change(mouse_pos)
                    # dis-selecting any player input
                    if typing_status is not None:
                        player_name_input[typing_status].set_selected(False)
                    typing_status = get_clicked_player_name_input(mouse_pos)

            elif event.type == pygame.KEYDOWN and typing_status is not None:
                # Check for backspace key
                if event.key == pygame.K_BACKSPACE:
                    player_name_input[typing_status].del_player_name()

                # Check for return key
                elif event.key == pygame.K_RETURN:
                    typing_status = None

                else:
                    player_name_input[typing_status].append_player_name(event.unicode)
                

        # Update game logic
        bg_image.draw()
        title_image.draw()
        start_button.draw()
        back_button.draw()

        for i in range(total_players):
            player_name_input[i].draw_player_name()
            player_power_select_image[i].draw()

        if len(player_name_input) < 7:
            player_add_button_image.draw_change_pos(player_name_input[-1].get_add_button_pos())
        if len(player_name_input) > 2:
            player_remove_button_image.draw_change_pos(player_name_input[-1].get_remove_button_pos())
        
        if msg_frame > 0:
            DrawText.draw_center(msg, dup_player_name_msg_pos)
            msg_frame -= 1

        #print(f" Selector Status = {typing_status}")

        pygame.display.update()  # Update display

