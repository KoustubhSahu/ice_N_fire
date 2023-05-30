import gui.gui_function
import player
import pygame

pygame.init()

player_list = list()
dice_pos = (375, 350)


def demo_attack(damage, attacker, target, images, texts):
    gui.gui_function.dice_image[damage - 1].draw_change_pos_once(dice_pos)
    gui.gui_function.simulate_attack(player_list[attacker], player_list[target], player_list, images, texts)
    player_list[target].attack(damage, player_list[attacker])


def game_intro():
    # homepage_0, tutorial_1, tutorial_2, tutorial_3
    state, frame = 0, 0
    player_health = {1: (-10, 10, -10), 2: (-10, 10, -10), 3: (-10, 10, -10), 4: (-10, 3, -5), 5: (-5, 3, -5)}
    gui.gui_function.back_button.set_pos(gui.gui_function.back_button_pos)
    for i in range(3):
        pow_num = i % 2
        player_list.append(player.Player(i, f"Player {i}", pow_num, gui.gui_declaration.player_pos_selector[3][i]))

    # Game Loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()

                if state == 0:
                    if gui.gui_function.homepage_button[0].clicked(mouse_pos):
                        return
                    elif gui.gui_function.homepage_button[1].clicked(mouse_pos):
                        state = 1
                    elif gui.gui_function.homepage_button[2].clicked(mouse_pos):
                        pygame.quit()

                # listening for Next button and Back button
                else:
                    if gui.gui_function.next_button.clicked(mouse_pos):
                        state += 1
                        frame = 0
                        if state > 5:
                            state = 0
                        else:
                            for p in player_list:
                                p.set_health(player_health[state][p.get_player_num()])


                    elif gui.gui_function.back_button.clicked(mouse_pos) and state > 1:
                        state -= 1
                        frame = 0
                        for p in player_list:
                            p.set_health(player_health[state][p.get_player_num()])

                # test
                for j in range(3):
                    if gui.gui_function.homepage_button[j].clicked(mouse_pos):
                        print(f"Button {j} was clicked")

        # Update game logic
        gui.gui_function.bg_image.draw()

        if state == 0:
            gui.gui_function.title_image.draw()
            for i in range(3):
                gui.gui_function.homepage_button[i].draw()

        else:
            gui.gui_function.draw_basics(player_list)
            gui.gui_function.health_scale.draw()
            gui.gui_function.next_button.draw()
            if state > 1:
                gui.gui_function.back_button.draw()

            if state == 1:
                texts = (("Player starts max power health", (450, 220), 3),
                         ("-10 for ICE power", (450, 280), 3),
                         ("+10 for FIRE power", (450, 340), 3))
                # gui.gui_function.DrawText.draw_center("Player starts max power health", (450, 220), 3)
                # gui.gui_function.DrawText.draw_center("-10 for ICE power", (450, 280), 3)
                # gui.gui_function.DrawText.draw_center("+10 for FIRE power", (450, 340), 3)
                for t in texts:
                    gui.gui_function.DrawText.draw_center(t[0], t[1], t[2])

            elif state == 2:
                damage, attacker, target = 3, 0, 2
                texts = (("When attacked", (450, 220), 3),
                         ("health moves towards zero", (450, 280), 3))
                dice_tuple = (gui.gui_function.dice_image[damage - 1], dice_pos)
                images = [gui.gui_function.health_scale, gui.gui_function.next_button, gui.gui_function.back_button,
                          dice_tuple]

                if frame == 0:
                    images.pop()
                    gui.gui_function.dice_roll(player_list, dice_pos, images, texts)
                    images.append(dice_tuple)

                elif frame == 20:
                    demo_attack(damage, attacker, target, images, texts)

                else:
                    for t in texts:
                        gui.gui_function.DrawText.draw_center(t[0], t[1], t[2])
                    gui.gui_function.dice_image[damage - 1].draw_change_pos_once(dice_pos)
                frame += 1

                if frame == 300:
                    frame = 0
                    for p in player_list:
                        p.set_health(player_health[state][p.get_player_num()])

            elif state == 3:
                damage, attacker, target = 5, 0, (1, 2)
                dice_tuple = (gui.gui_function.dice_image[damage - 1], dice_pos)
                texts = (("If Target has different power than Attacker", (450, 220), 3),
                         ("attack causes 1.5x damage", (450, 280), 3))
                images = [gui.gui_function.health_scale, gui.gui_function.next_button, gui.gui_function.back_button,
                          dice_tuple]

                if frame == 0:
                    images.pop()
                    gui.gui_function.dice_roll(player_list, dice_pos, images, texts)
                    images.append(dice_tuple)

                elif frame == 20:
                    demo_attack(damage, attacker, target[0], images, texts)

                # elif frame == 40:
                #     images.pop()
                #     gui.gui_function.dice_roll(player_list, dice_pos, images, texts)
                #     images.append(dice_tuple)

                elif frame == 40:
                    demo_attack(damage, attacker, target[1], images, texts)

                else:
                    for t in texts:
                        gui.gui_function.DrawText.draw_center(t[0], t[1], t[2])
                    gui.gui_function.dice_image[damage - 1].draw_change_pos_once(dice_pos)
                frame += 1

                if frame == 300:
                    frame = 0
                    for p in player_list:
                        p.set_health(player_health[state][p.get_player_num()])

            elif state == 4:
                damage, attacker, target = 6, 0, 2
                texts = (("If damage is greater than the player health", (450, 220), 3),
                         ("Player switches the power", (450, 280), 3))

                dice_tuple = (gui.gui_function.dice_image[damage - 1], dice_pos)
                images = [gui.gui_function.health_scale, gui.gui_function.next_button, gui.gui_function.back_button,
                          dice_tuple]

                if frame == 0:
                    images.pop()
                    gui.gui_function.dice_roll(player_list, dice_pos, images, texts)
                    images.append(dice_tuple)

                elif frame == 20:
                    demo_attack(damage, attacker, target, images, texts)

                else:
                    for t in texts:
                        gui.gui_function.DrawText.draw_center(t[0], t[1], t[2])
                    gui.gui_function.dice_image[damage - 1].draw_change_pos_once(dice_pos)
                frame += 1

                if frame == 300:
                    frame = 0
                    for p in player_list:
                        p.set_health(player_health[state][p.get_player_num()])

            elif state == 5:
                damage, attacker = 6, 0
                texts = (("You can choose to heal instead of attack", (450, 220), 3),
                         ("However you can't exceed the max health", (450, 280), 3))

                images = [gui.gui_function.health_scale, gui.gui_function.next_button, gui.gui_function.back_button, ]

                if frame == 0:
                    gui.gui_function.dice_roll(player_list, dice_pos, images, texts)


                elif frame == 20:
                    player_list[attacker].heal(damage)
                    gui.gui_function.dice_image[damage - 1].draw_change_pos_once(dice_pos)

                elif 20 < frame < 30:
                    player_list[attacker].player_image.draw_green()
                    gui.gui_function.dice_image[damage - 1].draw_change_pos_once(dice_pos)

                else:
                    for t in texts:
                        gui.gui_function.DrawText.draw_center(t[0], t[1], t[2])
                    gui.gui_function.dice_image[damage - 1].draw_change_pos_once(dice_pos)
                frame += 1

                if frame == 300:
                    frame = 0
                    for p in player_list:
                        p.set_health(player_health[state][p.get_player_num()])

        pygame.display.update()
    # gui.gui.function.draw_basics(player_list)
    # gui.gui_class.DrawText.draw_center(turn_msg, turn_msg_pos)


# game_intro()
