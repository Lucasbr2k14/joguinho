from pygame import image,Surface

class Enemy:
    def __init__(self, screen:Surface):
        self.pos    = [200,200]
        self.screen = screen
        self.speed  = 1
        self.load_image()
        
    def load_image(self):
        self.sprites = image.load_extended("./Sprites/teste.png")
        
    def draw(self):
        self.screen.blit(self.sprites, self.pos,[[0,128],[16,16]])
        
    def follow_player(self,player_pos:tuple):
        if self.pos[0]+8<player_pos[0]:
            self.pos[0]+=self.speed
        elif self.pos[0]+8>=player_pos[0]:
            self.pos[0]-=self.speed
        if self.pos[1]+13<player_pos[1]:
            self.pos[1]+=self.speed
        elif self.pos[1]+13>=player_pos[1]:
            self.pos[1]-=self.speed