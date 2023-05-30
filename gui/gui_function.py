from gui.gui_declaration import *
from gui.gui_class import *
import player


# Supporting functions


# Supporting functions
def player_action():
    # poiret one, Metal Mania
    heal_button.draw()
    attack_button.draw()


def draw_basics(player_list, images=None, texts=None):
    screen.fill((250, 240, 230))  # Fill screen with black color
    bg_image.draw()
    for p in player_list:
        p.stage_image.draw()
        p.player_image.draw()
        p.power_image.draw()
        DrawText.draw_center(p.get_health(), p.player_image.get_health_text_pos())
        DrawText.draw_center(p.get_name(), p.player_image.get_name_pos(), 2)
    if images is not None:
        for img in images:
            if type(img) is tuple:
                img[0].draw_change_pos_once(img[1])
            else:
                img.draw()
    if texts is not None:
        for t in texts:
            DrawText.draw_center(t[0], t[1], t[2])


def dice_roll(player_list, change_pos=None, images=None, texts=None):
    delay_time = 40
    action_frame = 8
    if change_pos is None:
        for frame in range(action_frame):
            draw_basics(player_list)
            dice_45d_image[random.randint(0, 5)].draw()
            pygame.display.update()
            pygame.time.delay(delay_time)

            draw_basics(player_list)
            dice_image[random.randint(0, 5)].draw()
            pygame.display.update()
            pygame.time.delay(delay_time)
    else:
        for frame in range(action_frame):
            draw_basics(player_list, images, texts)
            dice_45d_image[random.randint(0, 5)].draw_change_pos_once(change_pos[0], change_pos[1])
            pygame.display.update()
            pygame.time.delay(delay_time)

            draw_basics(player_list, images, texts)
            dice_image[random.randint(0, 5)].draw_change_pos_once(change_pos[0], change_pos[1])
            pygame.display.update()
            pygame.time.delay(delay_time)


def get_player_image_address(file_num):
    return os.path.join(player_image_100px_base_address, player_image_100px_file_name + str(file_num + 1) + ".png")


def next_player(curr, player_list):
    total = len(player_list)
    while True:
        curr += 1
        if curr == total:
            curr = 0
        if player_list[curr].get_health() != 0:
            return curr, player_list[curr].get_name() + "'s Turn"


def get_clicked_player(pos, player_list):
    for clicked_player in player_list:
        if clicked_player.player_image.clicked(pos):
            return clicked_player

    return None


def get_clicked_player_name_input(pos):
    for p in player_name_input:
        if p.clicked(pos):
            p.set_selected(True)
            return p.player_num

    return None


def check_player_power_change(pos):
    change = {0: 1, 1: 0}
    l = len(player_power_select_image)

    for p in range(l):
        if player_power_select_image[p].clicked(pos):
            player_power_select_num[p] = change[player_power_select_num[p]]
            player_power_select_image[p].set_image_address(power_60px_addr[player_power_select_num[p]])
            return


def simulate_attack(attacker, target, player_list, images=None, texts=None):
    attacker_power = attacker.power_image
    action_frame = 20
    shot = attacker_power.duplicate()
    shot_x, shot_y = shot.get_pos()
    speed_x = (target.player_image.get_x() - shot_x) / action_frame
    speed_y = (target.player_image.get_y() - shot_y) / action_frame
    delay_time = 30

    for frame in range(action_frame):
        draw_basics(player_list, images, texts)
        shot.draw_change_pos(shot_x, shot_y)
        pygame.display.update()
        shot_x += speed_x
        shot_y += speed_y
        pygame.time.delay(delay_time)

    draw_basics(player_list, images, texts)
    target.player_image.draw_red()
    pygame.display.update()
    pygame.time.delay(delay_time * 2)


def heal_player_display(healing_player):
    delay_time = 60
    healing_player.player_image.draw_green()
    pygame.display.update()
    pygame.time.delay(delay_time)
