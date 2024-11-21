 
from pygame import Surface
from .sprite import Sprite

class Player(Sprite):

    def __init__(self, screen:Surface): # E porque o cooldown vira time?

        super().__init__(
            life = 100,
            velocity = 2,
            position = [screen.get_width()/2, screen.get_height()/2],
            screen = screen,
            scale_factor = 2,
            sprite_sheet = "./Sprites/teste.png",
            sprite_sheet_size = (448,448)
        )

        self.mana:float = 100.0 
        self.walk:bool = False
        self.pose:float = 0.0
        self.load_visuals()
    
    def get_hitbox(self) -> tuple[tuple[int], tuple[int]]:
        return ( 
            (self.position[0]+(2*self.scale_factor), self.position[1]+(18*self.scale_factor)),
            (self.position[0]+(14*self.scale_factor), self.position[1]+(32*self.scale_factor))
        )


    def get_hud(self) -> tuple[int, int]:
        return self.life, self.mana

    def mcpose(self):
        if self.walk:
            if self.looking == "up" or self.looking == "down":
                self.pose += 100
            else:
                self.pose += 50
            
        else:
            self.pose += 25
            
        if self.pose >= 4000:
            self.pose = 0

    def shot(self) -> tuple:
        if self.cooldown <= 0 and self.mana >= 10:
            self.cooldown = 3
            self.mana -= 10
            return (self.position[0]+8,(self.position[1]+16))
        else:
            return ()
    

    def update(self):
        self.cooldown -= 0.1        
        if self.mana < 100:
            self.mana += 0.1
        

    def walk_up(self, cooldown_shot:bool):
        if not self.collision[0] and self.cooldown <= 0: 
            self.position[1] -= self.velocity
            if cooldown_shot:
                self.looking = "up"


    def walk_down(self, cooldown_shot:bool):
        if not self.collision[1] and self.cooldown <= 0:
            self.position[1] += self.velocity
            if cooldown_shot:
                self.looking = "down"


    def walk_left(self, cooldown_shot:bool): 
        if not self.collision[2] and self.cooldown <= 0 :
            self.position[0] -= self.velocity
            if cooldown_shot:
                self.looking = "left"


    def walk_right(self, cooldown_shot:bool):
        if not self.collision[3] and self.cooldown <= 0:
            self.position[0] += self.velocity
            if cooldown_shot:
                self.looking = "right"


    def walking(self, walk:bool):
        self.walk = walk


    def draw(self):

        self.mcpose()

        if self.cooldown <= 0:  
            if self.looking == "right":
                if self.walk:
                   position = [(256+16*(self.pose//1000))*self.scale_factor,0]
                else:
                   position = [(192+16*(self.pose//1000))*self.scale_factor,0]
            if self.looking == "left":
                if self.walk:
                   position = [(368+16+16*(self.pose//1000))*self.scale_factor,0]
                else:
                   position = [(288+32+16*(self.pose//1000))*self.scale_factor,0]
            if self.looking == "up":
                if self.walk:
                   position = [(160+16*(self.pose//2000))*self.scale_factor,0]
                else:
                   position = [(96+16*(self.pose//1000))*self.scale_factor,0]
            if self.looking == "down":
                if self.walk:
                   position = [(64+16*(self.pose//2000))*self.scale_factor,0]
                else:
                   position = [(0+16*(self.pose//1000))*self.scale_factor,0]
                
        else:
           position = [(0+16*((3-self.cooldown)//1))*self.scale_factor,32*self.scale_factor]

        self.screen.blit(self.sprites, self.position,[position,[16*self.scale_factor,32*self.scale_factor]])
