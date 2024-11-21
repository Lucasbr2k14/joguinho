from .sprite import Sprite
from pygame import Surface

class Slime(Sprite):
    def __init__(self, screen:Surface, position:tuple):
        super().__init__(
            life = 100,
            velocity = 1,
            position = position,
            screen = screen,
            scale_factor = 4,
            sprite_sheet = "./Sprites/teste.png",
            sprite_sheet_size = (448,448)
        )

        self.load_visuals()

    def draw(self, position:tuple):
        self.screen.blit(self.sprites, self.position,[[0 * self.scale_factor,128 * self.scale_factor],[16 * self.scale_factor,16 * self.scale_factor]])
        
    def follow_player(self, player_pos:tuple):
        if self.position[0] +8 < player_pos[0]:
           self.walk_right()
        elif self.position[0] +8 >= player_pos[0]:
            self.walk_left()

        if self.position[1] +13 < player_pos[1]:
            self.walk_down()
        elif self.position[1] + 13 >= player_pos[1]:
            self.walk_up()



