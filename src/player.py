 
from pygame import image, Surface, transform

# Tamnho 14X26

x = 0
y = 1

class Player:

    def __init__(self, screen:Surface): # E porque o cooldown vira time?
        self.screen      = screen
        self.velocity    = 2
        self.position    = [screen.get_width()/2, screen.get_height()/2]
        self.radius      = 0
        self.walk        = False
        self.pose        = 0
        self.collision   = (False, False, False, False)
        self.player_looking = "down"

        self.scale_factor= 2
        self.sprite_sheet_size = (448,448)
        self.load_visuals()
    

    def load_visuals(self):
        scale = (self.sprite_sheet_size[0]*self.scale_factor,self.sprite_sheet_size[1]*self.scale_factor)
        self.sprites = image.load_extended("./Sprites/teste.png")
        self.sprites = transform.scale(self.sprites, scale)
    

    def get_hitbox(self):
        return ( 
            (self.position[x]+(2*self.scale_factor), self.position[y]+(18*self.scale_factor)),
            (self.position[x]+(14*self.scale_factor), self.position[y]+(32*self.scale_factor))
        )


    def mcpose(self):
        if self.walk:
            if self.player_looking == "up" or self.player_looking == "down":
                self.pose += 100
            else:
                self.pose += 50
            
        else:
            self.pose += 25
            
        if self.pose >= 4000:
            self.pose = 0

    def shot(self):
        # Animações tiro
        # Retornar posição inicial do tiro
        return (self.position[x]+8,(self.position[y]+16))
    

    def walk_up(self, cooldown_shot:bool):
        if not self.collision[0]: 
            self.position[y] -= self.velocity
            if cooldown_shot:
                self.player_looking = "up"


    def walk_down(self, cooldown_shot:bool):
        if not self.collision[1]:
            self.position[y] += self.velocity
            if cooldown_shot:
                self.player_looking = "down"


    def walk_left(self, cooldown_shot:bool): 
        if not self.collision[2]:
            self.position[x] -= self.velocity
            if cooldown_shot:
                self.player_looking = "left"


    def walk_right(self, cooldown_shot:bool):
        if not self.collision[3]:
            self.position[x] += self.velocity
            if cooldown_shot:
                self.player_looking = "right"


    def walking(self, walk:bool):
        self.walk = walk


    def draw(self, cooldown_frames:float):

        self.mcpose()

        if cooldown_frames <= 0:  
            if self.player_looking == "right":
                if self.walk:
                   position = [(256+16*(self.pose//1000))*self.scale_factor,0]
                else:
                   position = [(192+16*(self.pose//1000))*self.scale_factor,0]
            if  self.player_looking == "left":
                if self.walk:
                   position = [(368+16+16*(self.pose//1000))*self.scale_factor,0]
                else:
                   position = [(288+32+16*(self.pose//1000))*self.scale_factor,0]
            if  self.player_looking == "up":
                if self.walk:
                   position = [(160+16*(self.pose//2000))*self.scale_factor,0]
                else:
                   position = [(96+16*(self.pose//1000))*self.scale_factor,0]
            if  self.player_looking == "down":
                if self.walk:
                   position = [(64+16*(self.pose//2000))*self.scale_factor,0]
                else:
                   position = [(0+16*(self.pose//1000))*self.scale_factor,0]
                
        else:
           position = [(0+16*((3-cooldown_frames)//1))*self.scale_factor,32*self.scale_factor]

        self.screen.blit(self.sprites, self.position,[position,[16*self.scale_factor,32*self.scale_factor]])
