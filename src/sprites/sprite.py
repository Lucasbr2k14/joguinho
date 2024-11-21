from pygame import Surface, transform, image

class Sprite:
    def __init__(self, life:int, velocity:int, position:list, screen:Surface, scale_factor:int, sprite_sheet:str, sprite_sheet_size:tuple):
        self.life:int = life
        self.velocity:float = velocity
        self.position:int = position
        self.screen:Surface = screen
        self.scale_factor:int = scale_factor
        self.collision:tuple[bool] = (False, False, False, False)
        self.looking:str = "down"
        self.cooldown:float = 0.0
        self.sprite_sheet:str = sprite_sheet
        self.sprite_sheet_size = sprite_sheet_size


    def load_visuals(self):
        scale = (self.sprite_sheet_size[0]*self.scale_factor,self.sprite_sheet_size[1]*self.scale_factor)
        self.sprites = image.load_extended(self.sprite_sheet)
        self.sprites = transform.scale(self.sprites, scale)


    def draw(self):
        pass


    def walk_up(self):
        if not self.collision[0]:
            self.position[1] -= self.velocity
        self.looking = "up"

    def walk_down(self):
        if not self.collision[1]:
            self.position[1] += self.velocity
        self.looking = "down"
    
    def walk_left(self):
        if not self.collision[2]:
            self.position[0] -= self.velocity
        self.looking = "left"

    def walk_right(self):
        if not self.collision[3]:
            self.position[0] += self.velocity
        self.looking = "right"