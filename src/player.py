 
from pygame import image, Surface, transform

# Tamnho 14X26

x = 0
y = 1

class Player:

    def __init__(self, screen:Surface): # E porque o cooldown vira time?

        self.velocity:int = 2
        self.life:int = 100
        self.mana:float = 100.0 
        self.cooldown:float = 0.0

        self.screen = screen
        self.position:list[float,float] = [screen.get_width()/2, screen.get_height()/2]
        self.walk:bool = False
        self.pose:float = 0.0
        self.collision:tuple[bool] = (False, False, False, False)
        self.player_looking = "down"

        self.scale_factor= 2
        self.sprite_sheet_size = (448,448)
        self.load_visuals()
    

    def load_visuals(self):
        scale = (self.sprite_sheet_size[0]*self.scale_factor,self.sprite_sheet_size[1]*self.scale_factor)
        self.sprites = image.load_extended("./Sprites/teste.png")
        self.sprites = transform.scale(self.sprites, scale)
    

    def get_hitbox(self) -> tuple[tuple[int], tuple[int]]:
        return ( 
            (self.position[x]+(2*self.scale_factor), self.position[y]+(18*self.scale_factor)),
            (self.position[x]+(14*self.scale_factor), self.position[y]+(32*self.scale_factor))
        )


    def get_hud(self) -> tuple[int, int]:
        return self.life, self.mana

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

    def shot(self) -> tuple:
        if self.cooldown <= 0 and self.mana >= 10:
            self.cooldown = 3
            self.mana -= 10
            return (self.position[x]+8,(self.position[y]+16))
        else:
            return ()
    

    def update(self):
        self.cooldown -= 0.1        
        if self.mana < 100:
            self.mana += 0.1
        

    def walk_up(self, cooldown_shot:bool):
        if not self.collision[0] and self.cooldown <= 0: 
            self.position[y] -= self.velocity
            if cooldown_shot:
                self.player_looking = "up"


    def walk_down(self, cooldown_shot:bool):
        if not self.collision[1] and self.cooldown <= 0:
            self.position[y] += self.velocity
            if cooldown_shot:
                self.player_looking = "down"


    def walk_left(self, cooldown_shot:bool): 
        if not self.collision[2] and self.cooldown <= 0 :
            self.position[x] -= self.velocity
            if cooldown_shot:
                self.player_looking = "left"


    def walk_right(self, cooldown_shot:bool):
        if not self.collision[3] and self.cooldown <= 0:
            self.position[x] += self.velocity
            if cooldown_shot:
                self.player_looking = "right"


    def walking(self, walk:bool):
        self.walk = walk


    def draw(self):

        self.mcpose()

        if self.cooldown <= 0:  
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
           position = [(0+16*((3-self.cooldown)//1))*self.scale_factor,32*self.scale_factor]

        self.screen.blit(self.sprites, self.position,[position,[16*self.scale_factor,32*self.scale_factor]])
