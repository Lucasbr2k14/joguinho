from pygame import Surface,draw,image

class Hud:

    def __init__(self,surface:Surface):

        self.mana = 100
        self.life = 100
        self.surface=surface
        self.load_visuals()
        
    def load_visuals(self):
        self.sprites = image.load_extended("./Sprites/teste.png")
        
    def draw(self):
        draw.rect(self.surface,'red',[(0,0),(self.life,16)])
        draw.rect(self.surface,'blue',[(0,18),(self.mana,16)])
        self.surface.blit(self.sprites,[0,0],[[0,432],[101,16]])
        self.surface.blit(self.sprites,[0,18],[[0,432],[101,16]])
        
    def new_mana(self):
        self.mana -= 10
    
    def recharge_mana(self):
        if self.mana < 100:
            self.mana += 0.05
            
    def return_mana(self):
        return self.mana