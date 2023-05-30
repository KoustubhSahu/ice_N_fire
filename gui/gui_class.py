import os.path

import pygame


# Class for Position of an image
class Position:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_pos(self):
        return self.x, self.y

    def get_dim(self):
        return self.width, self.height

    def get_boundary(self):
        return self.x, self.x + self.width, self.y, self.y + self.height

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_pos(self, x, y=None, width=None, height=None):
        if type(x) == tuple:
            self.x, self.y = x[0], x[1]
            self.width, self.height = x[2], x[3]
        else:
            self.x, self.y = x, y
            self.width, self.height = width, height


class Image(Position):
    image_address = ""
    image = None
    display = True
    @classmethod
    def set_screen(cls, print_screen):
        cls.print_screen = print_screen

    def __init__(self, image_address: str, x, y=0, width=0, height=0):
        if type(x) is tuple:
            super().__init__(x[0], x[1], x[2], x[3])
        else:
            super().__init__(x, y, width, height)
        self.set_image_address(image_address)

    def draw(self):
        if self.display:
            self.print_screen.blit(self.image, super().get_pos())

    def opacity(self, alpha):
        self.image.convert_alpha()
        self.image.set_alpha(alpha)

    def duplicate(self):
        return Image(self.image_address, self.x, self.y, self.width, self.height)

    def draw_red(self):
        if self.display:
            rect_color = (255, 0, 0)  # Red
            rect = pygame.Rect(self.x, self.y, self.width, self.height)
            pygame.draw.rect(self.print_screen, rect_color, rect)
            self.print_screen.blit(self.image, super().get_pos())

    def draw_green(self):
        if self.display:
            rect_color = (0, 255, 0)  # Green
            rect = pygame.Rect(self.x, self.y, self.width, self.height)
            pygame.draw.rect(self.print_screen, rect_color, rect)
            self.print_screen.blit(self.image, super().get_pos())

    def clicked(self, pos):
        if (self.x < pos[0] < self.x + self.width) and (self.y < pos[1] < self.y + self.height):
            return True
        return False

    def toggle_display(self):
        self.display = not self.display

    def set_image_address(self, image_address):
        self.image_address = image_address
        self.image = pygame.image.load(self.image_address)

    def get_stage_tuple(self, stage_width=120, stage_height=55):
        return self.x - 10, self.y + (self.height * 0.65), stage_width, stage_height

    def get_player_power_pos(self):
        power_x, power_y, x_pad_left, x_pad_right, y_pad = 42, 60, -7, -35, 3
        if self.x < 450:
            return self.x + self.width + x_pad_left, self.y + y_pad, power_x, power_y
        else:
            return self.x + x_pad_right, self.y + y_pad, power_x, power_y

    def get_name_pos(self):
        y_pad = 25
        return self.x + (self.width/2), self.y + self.height + y_pad

    def get_health_text_pos(self):
        x_pad_left, x_pad_right, y_pad = 30, -30, 10
        if self.x < 450:
            return self.x + self.width + x_pad_left, self.y + self.height - y_pad
        else:
            return self.x + x_pad_right, self.y + self.height - y_pad

    def draw_change_pos(self, x, y=None, width=None, height=None):
        if type(x) is tuple and y is None:
            self.set_pos(x[0], x[1], x[2], x[3])
        else:
            self.set_pos(x, y, width, height)
        self.draw()

    def draw_change_pos_once(self, x, y=None):
        if type(x) is tuple and y is None:
            self.print_screen.blit(self.image, x)
        else:
            self.print_screen.blit(self.image, (x, y))



class TextInput(Image):
    def __init__(self, player_num: int, image_address: str, x, y=0, width=0,
                 height=0):
        super().__init__(image_address, x, y, width, height)
        self.player_num = player_num
        self.player_name = ""
        self.selected = False
        
        
    def draw_player_name(self):
        self.draw()
        if self.player_name == "" and not self.selected:
            DrawText.draw(f"Player {self.player_num}", self.get_player_name_text_pos(), 1, 1)
        else:
            DrawText.draw(self.player_name, self.get_player_name_text_pos(), 1)
            
    def clicked(self, pos):
        return super().clicked(pos)

    def append_player_name(self, char):
        self.player_name += char

    def del_player_name(self):
        self.player_name = self.player_name[:-1]

    def get_player_name(self):
        if self.player_name == "":
            return f"Player {self.player_num}"
        else:
            return self.player_name

    def set_selected(self, selected: bool):
        self.selected = selected

    def get_add_button_pos(self):
        add_player_width = 40
        x_pad = 20
        y_pad = 5
        # return self.x + self.width - add_player_width, self.y + self.height + y_pad, 40, 40
        return self.x + x_pad, self.y + self.height + y_pad, 40, 40

    def get_remove_button_pos(self):
        remove_player_width = 40
        x_pad = 30
        y_pad = 5
        return self.x + self.width - remove_player_width - x_pad, self.y + self.height + y_pad, 40, 40

    def get_player_name_text_pos(self):
        x_pad = 20
        y_pad = 7
        return self.x + x_pad, self.y + y_pad

    def get_player_power_pos(self):
        power_x, power_y, x_pad = 42, 60, 10
        return self.x - power_x - x_pad, self.y, power_x, power_y

    def set_player_pos(self, pos):
        self.x, self.y = pos[0], pos[1]

    def set_player_num(self, num):
        self.player_num = num


class DrawText(TextInput):
    # Font Address
    default_font_address = os.path.join("fonts", "Metal_Mania", "MetalMania_Regular.ttf")
    player_font_address = os.path.join("fonts", "Road_Rage", "RoadRage_Regular.ttf")

    # Fonts Initialisation
    pygame.font.init()
    default_font = pygame.font.Font(default_font_address, 40)
    player_font = pygame.font.Font(player_font_address, 40)
    player_font_small = pygame.font.Font(player_font_address, 35)
    player_font_big = pygame.font.Font(player_font_address, 55)
    font = (default_font, player_font, player_font_small, player_font_big)
    font_color = ((70, 50, 50), (200, 200, 200))

    @classmethod
    def draw(cls, text, text_pos, font_selector=0, font_color_selector=0):
        if type(text) is not str:
            text = str(text)

        text_surface = cls.font[font_selector].render(text, True, cls.font_color[font_color_selector])
        cls.print_screen.blit(text_surface, text_pos)
        
    @classmethod
    def draw_center(cls, text, text_center_pos, font_selector=0, font_color_selector=0):
        if type(text) is not str:
            text = str(text)

        text_surface = cls.font[font_selector].render(text, True, cls.font_color[font_color_selector])
        text_rect = text_surface.get_rect()
        text_rect.center = text_center_pos
        cls.print_screen.blit(text_surface, text_rect)

    @classmethod
    def draw_notification(cls, msg, mid_x=450, mid_y=350):
        text_surface = cls.font[0].render(msg, True, cls.font_color[0])
        notification_image_address = os.path.join('images', 'button', 'text_notification.png')
        notification_image = pygame.image.load(notification_image_address)
        image_rect = notification_image.get_rect()
        text_rect = text_surface.get_rect()
        image_rect.center, text_rect.center = (mid_x, mid_y), (mid_x, mid_y)
        cls.print_screen.blit(notification_image, image_rect)
        cls.print_screen.blit(text_surface, text_rect)