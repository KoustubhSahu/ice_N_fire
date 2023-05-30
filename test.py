from gui.gui_function import *
#import gui.gui_declaration
import player

pygame.init()


# necessary Image initialisation


# Supporting Variables
# -Dice Rolled-, Action, Attack, Shoot, Waiting
status = "Waiting"
dice_num = 1
attacker_player = None
target_player = None

# test
player_list = list()
for p in range(7):
    player_list.append(player.Player(
        p, f"Player {p}", (0, Image(power_60px_addr[0], (0,0,0,0))), p)
        )
    

# Game Loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
    

    # Update game logic

    draw_basics(player_list)

    dice_image[dice_num - 1].draw()

    pygame.display.update()  # Update display
