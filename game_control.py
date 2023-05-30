from gui.gui_function import *

pygame.init()


def play(player_list):
    # Supporting Variables
    # Action, Attack, Waiting
    status = "Waiting"
    dice_num = 1
    player_turn = 0
    # target_player = None
    turn_msg = player_list[player_turn].get_name() + "'s Turn"
    attack_msg = "click on player to Attack"
    notification_msg = ""
    notification_frame = 0
    max_notification_frame = 300
    alive_player_list = player_list.copy()
    self_harm = False
    game_over = False

    # Game Loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                print(f"Playing_Status = {status}")

                if self_harm_toggle_boundary[0] < mouse_pos[0] < self_harm_toggle_boundary[1] and \
                        self_harm_toggle_boundary[2] < mouse_pos[1] < self_harm_toggle_boundary[3]:
                    self_harm = not self_harm
                    print(f"self harm toggle is on and self_harm = {self_harm}")

                # dice_roll Button Clicked
                elif status == "Waiting" and dice_roll_button.clicked(mouse_pos):
                    dice_num = random.randint(1, 6)
                    status = "Action"
                    dice_roll(player_list)

                # Heal Button Clicked
                elif status == "Action" and heal_button.clicked(mouse_pos):
                    status = "Waiting"
                    player_list[player_turn].heal(dice_num)
                    heal_player_display(player_list[player_turn])
                    # next alive player's turn
                    player_turn, turn_msg = next_player(player_turn, player_list)


                # Attack Button Clicked
                elif status == "Action" and attack_button.clicked(mouse_pos):
                    status = "Attack"
                    if len(alive_player_list) == 2:
                        target_player_index, turn_msg = next_player(player_turn, alive_player_list)
                        target_player = player_list[target_player_index]
                        simulate_attack(player_list[player_turn], target_player, player_list)
                        target_player.attack(dice_num, player_list[player_turn])
                        if target_player.get_health() == 0:
                            alive_player_list.remove(target_player)
                        status = "Waiting"
                        # next alive player's turn
                        player_turn  = target_player_index
                        if len(alive_player_list) == 1:
                            game_over = True

                # choosing the target
                elif status == "Attack":
                    target_player = get_clicked_player(mouse_pos, player_list)
                    if target_player is None:
                        continue
                    elif target_player not in alive_player_list:
                        notification_msg = "Can't attack a dead player"
                        notification_frame = max_notification_frame
                        continue
                    elif (not self_harm) and (target_player is player_list[player_turn]):
                        notification_msg = "Can't attack yourself"
                        notification_frame = max_notification_frame
                        continue

                    simulate_attack(player_list[player_turn], target_player, player_list)
                    target_player.attack(dice_num, player_list[player_turn])
                    if target_player.get_health() == 0:
                        alive_player_list.remove(target_player)
                    status = "Waiting"
                    # next alive player's turn
                    player_turn, turn_msg = next_player(player_turn, alive_player_list)
                    if len(alive_player_list) == 1:
                        game_over = True

        # Update game logic

        draw_basics(player_list)
        DrawText.draw_center(turn_msg, turn_msg_pos)

        # Draw graphics
        if status == "Waiting":
            dice_roll_button.draw()

        elif status == "Action":
            player_action()

        elif status == "Attack":
            DrawText.draw_center(attack_msg, attack_msg_pos)
            if notification_frame > 0:
                notification_frame -= 1
                DrawText.draw_center(notification_msg, notification_msg_pos)

        dice_image[dice_num - 1].draw()

        pygame.display.update()

        if game_over:
            return alive_player_list[0].get_player_num()
        #print(f"Playing_Status = {status}")
