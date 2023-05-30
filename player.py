# -*- coding: utf-8 -*-
import gui

"""
Created on Wed Apr 14 02:45:44 2021

@author: 52ako
"""


class Player:
    health = 0
    max_health = (-10, 10)

    def __init__(self, num, name, pow_num, pos_num):
        self.player_num = num
        self.name = name
        self.power_num = pow_num
        self.health = Player.max_health[self.power_num]
        self.player_image = gui.gui_class.Image(gui.gui_function.get_player_image_address(pos_num),
                                                gui.gui_declaration.player_position_100px[pos_num])
        self.power_image = gui.gui_class.Image(gui.gui_function.power_60px_addr[self.power_num],
                                               self.player_image.get_player_power_pos())
        self.stage_image = gui.gui_class.Image(gui.gui_declaration.stage_image_address,
                                               self.player_image.get_stage_tuple())

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health
        self.set_pow()

    def get_name(self):
        return self.name

    def get_player_num(self):
        return self.player_num

    def set_pow(self):
        if self.health > 0:
            self.power_num = 1
            self.power_image.set_image_address(gui.gui_declaration.power_60px_addr[self.power_num])

        elif self.health < 0:
            self.power_num = 0
            self.power_image.set_image_address(gui.gui_declaration.power_60px_addr[self.power_num])

    def heal(self, health_boost):
        # if ice powered
        if self.power_num == 0:
            self.health -= health_boost
            if self.health < Player.max_health[self.power_num]:
                self.health = Player.max_health[self.power_num]

        # if fire powered
        else:
            self.health += health_boost
            if self.health > Player.max_health[self.power_num]:
                self.health = Player.max_health[self.power_num]

    def attack(self, health_lost, attacker):
        lost_factor = 1.5
        if self.power_num == attacker.power_num:
            lost_factor = 1

        # if ice powered
        if self.power_num == 0:
            self.health += int(health_lost * lost_factor)
            self.set_pow()

        # if fire powered
        else:
            self.health -= int(health_lost * lost_factor)
            self.set_pow()

        if self.health == 0:
            self.player_image.set_image_address(gui.gui_declaration.dead_image_address)
            self.power_image.toggle_display()
