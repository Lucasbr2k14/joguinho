 
from pygame import image, Surface

# Tamnho 14X26

class Player:


    def __init__(self, screen:Surface, time): # E porque o cooldown vira time?

        self.screen   = screen
        self.velocity = 2
        self.position = [screen.get_width()/2, screen.get_height()/2]
        self.radius   = 0
        self.walk     = False
        self.pose     = 0
        self.player_looking = "down"
        self.load_visuals()
        self.time = time
    
    
    def mcpose(self):
        
        if self.walk:
            if self.player_looking == "up" or self.player_looking == "down":
                self.pose += 0.1
            else:
                self.pose += 0.05
            
        else:
            self.pose += 0.025
            
        if self.pose >= 4:
            self.pose = 0


    def load_visuals(self):
        self.sprites = [image.load_extended("./Sprites/teste.png")]
        # self.sprites = transform.scale(self.sprites, (128,128))
    
    def shot(self):
        # Animações tiro
        # Retornar posição inicial do tiro
        return (self.position[0]+8,self.position[1]+16)
    

    def walk_up(self):
        if ((self.position[1]) > (0 + self.radius)): 
            self.position[1] -= self.velocity
            self.player_looking = "up"


    def walk_down(self):
        if((self.position[1]) < (self.screen.get_height() - self.radius -16)):
            self.position[1] += self.velocity
            if self.time <= 0:
                self.player_looking = "down"


    def walk_right(self):
        if((self.position[0]) < (self.screen.get_width() - self.radius-16)):
            self.position[0] += self.velocity
            if self.time <= 0:
                self.player_looking = "right"


    def walk_left(self): 
        if ((self.position[0]) > (0 + self.radius)):
            self.position[0] -= self.velocity
            if self.time <= 0:
                self.player_looking = "left"
    

    def walking(self, walk:bool):
        self.walk = walk


    def draw(self ,time):
        if time <= 0:  
            if self.player_looking == "right":
                if self.walk:
                    self.screen.blit(self.sprites[0], self.position,[[256+16*(self.pose//1),0],[16,32]])
                else:
                    self.screen.blit(self.sprites[0], self.position,[[192+16*(self.pose//1),0],[16,32]])
            if  self.player_looking == "left":
                if self.walk:
                    self.screen.blit(self.sprites[0], self.position,[[368+16+16*(self.pose//1),0],[16,32]])
                else:
                    self.screen.blit(self.sprites[0], self.position,[[288+32+16*(self.pose//1),0],[16,32]])
            if  self.player_looking == "up":
                if self.walk:
                    self.screen.blit(self.sprites[0], self.position,[[160+16*(self.pose//2),0],[16,32]])
                else:
                    self.screen.blit(self.sprites[0], self.position,[[96+16*(self.pose//1),0],[16,32]])
            if  self.player_looking == "down":
                if self.walk:
                    self.screen.blit(self.sprites[0], self.position,[[64+16*(self.pose//2),0],[16,32]])
                else:
                    self.screen.blit(self.sprites[0], self.position,[[0+16*(self.pose//1),0],[16,32]])
                
        else:
            self.screen.blit(self.sprites[0], self.position,[[0+16*((3-time)//1),32],[16,32]])
            